import inspect
import os
import string
import sys

THIS_FILE_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
DEFAULT_PATH = string.join(THIS_FILE_DIR.split("/")[:-7],"/")
print DEFAULT_PATH
sys.path.insert(1,DEFAULT_PATH)
from pycharmCode.stock.controllers.financials import FinancialController
from pycharmCode.stock.streams.models import InsertModel
from pycharmCode.stock.scrape import StockScrapy

from .state import IncomeState, BalanceState, CashState


class FinancialSpider(StockScrapy):
    name = "FinancialSpider"
    start_urls = []
    headers = []
    state=IncomeState()	#<---  this is the default state

    def __init__(self,*args,**kwargs):
        super(FinancialSpider,self).__init__(controlTable = FinancialController.NASDAQ, directory=__file__, *args,**kwargs)

    def parsing(self,response):
        table = self.getTable(response._url)
        symbol = response.xpath('//div[@class="qbreadcrumb"]/span/a[3]/text()').extract()[0]
        currency = self.f.filterForSQL(self.f.filterNonListedData(response.xpath('//div[@class="genTable"]/h3[@class="table-headtag"]/text()').extract()).strip())
        # Period Ending :    Trend :   are not counted  so we go up 2 in the headers
        headers = response.xpath('//div[@class="genTable"]/table/thead/tr/th/text()').extract()[2:]
        rowHeaders = response.xpath('//div[@class="genTable"]/table/tr/th/text()').extract()
        data = response.xpath('//div[@class="genTable"]/table/tr/td/text()').extract()

        headerStart = self.findQuarterlyHeaders(headers)
        headers = headers[headerStart:]
        models = []
        for hIndex, h in enumerate(headers):
            dOff = hIndex
            rIndex = 0
            m = InsertModel(table)
            m.insert("symbol", symbol)
            m.insert("date", self.f.convertDate(h))
            m.insert("currency", currency)
            for r in rowHeaders:
                if (self.headerRowWithNoData(r)):
                    continue
                m.insert(self.f.filterHeader(self.f.filterForSQL(self.f.mushString(r))),
                    str(self.f.convertToNeg(self.f.filterNonListedData(data[dOff + (rIndex * len(headers))]))))
                rIndex += 1
#            print m
            models.append(m)
        self.controller.insert(symbol, models)

    def getTable(self, url):
        if ("annual" in url):
            if ("income" in url):
                return "NasdaqAnnualIncomeStatements"
            elif ("balance" in url):
                return "NasdaqAnnualBalanceSheets"
            elif ("flow" in url):
                return "NasdaqAnnualCashFlowStatements"
        if ("quarterly" in url):
            if ("income" in url):
                return "NasdaqQuarterlyIncomeStatements"
            elif ("balance" in url):
                return "NasdaqQuarterlyBalanceSheets"
            elif ("flow" in url):
                return "NasdaqQuarterlyCashFlowStatements"

    def headerRowWithNoData(self, r):
        if (("Operating Expense" in r) or ("Current Liabilities" in r) or ("Current Assets" in r) or ("Long-Term Assets" in r)
            or ("Stock Holders Equity" in r) or ("Cash Flows-Operating Activities" in r) or ("Changes in Operating Activities" in r)
            or ("Cash Flows-Investing Activities" in r) or ("Cash Flows-Financing Activities" in r)):
            return True
        return False

    def findQuarterlyHeaders(self, headers):
        for index,h in enumerate(headers):
            if ("Quarter Ending:" in h):
                return index + 1
        return 0

    def _insertItems(self, items):
        for i in items:
            self.state.insert(self.controller, i)

    def _configureState(self):
        if(self.stateFlag == 'I'):
            self.state = IncomeState(self.time)
        elif(self.stateFlag == 'B'):
            self.state = BalanceState(self.time)
        elif(self.stateFlag == 'C'):
            self.state=CashState(self.time)
        else:
            self.state=IncomeState(self.time)

    def _addURLS(self, index, s):
        s = s.lower()
        s = s.replace(".", "-")
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=income-statement&data=annual"]
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=balance-sheet&data=annual"]
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=cash-flow&data=annual"]
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=income-statement&data=quarterly"]
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=balance-sheet&data=quarterly"]
        self.start_urls += ["http://www.nasdaq.com/symbol/"+ s +"/financials?query=cash-flow&data=quarterly"]
        return True

    def _getHeaders(self,header,sym):
        itemList=[]
        for index,head in enumerate(header[2:]):
            self.headers.append(head)
        return itemList

