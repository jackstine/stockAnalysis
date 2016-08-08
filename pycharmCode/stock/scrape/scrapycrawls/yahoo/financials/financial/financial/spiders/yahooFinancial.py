# -*- coding: utf-8 -*-
import sys, datetime, os
sys.path.insert(1, os.path.expanduser("~") + "/Dropbox/Programs/Stock/code/")
from pycharmCode.stock.utility import Filter
from pycharmCode.stock.controllers.financials import FinancialController
from pycharmCode.stock.models import InsertModel
from pycharmCode.stock.scrape import StockScrapy

class YahoofinancialSpider(StockScrapy):
    name = "yahooFinancial"
    BalanceType = "BalanceSheet"
    IncomeType = "IncomeSheet"

    def __init__(self, *args, **kwargs):
        super(YahoofinancialSpider, self).__init__(controlTable = FinancialController.YAHOO, directory=__file__, *args, **kwargs)

    def changeSymbol(self, s):
        newWord = s.replace(".", "-")
        #dont know what to about ^
        return newWord

    def _addURLS(self, index, s):
        s = s.upper()
        s = self.changeSymbol(s)
        if (s != None):
            self.start_urls += ["http://finance.yahoo.com/q/bs?s="+ s +"+Balance+Sheet&annual"]
            self.start_urls += ["http://finance.yahoo.com/q/bs?s="+ s +"+Balance+Sheet&quarterly"]
            self.start_urls += ["http://finance.yahoo.com/q/is?s="+ s +"+Income+Statement&annual"]
            self.start_urls += ["http://finance.yahoo.com/q/is?s="+ s +"+Income+Statement&quarterly"]
            self.start_urls += ["http://finance.yahoo.com/q/cf?s="+ s +"+Cash+Flow&annual"]
            self.start_urls += ["http://finance.yahoo.com/q/cf?s="+ s +"+Cash+Flow&quarterly"]
        return True

    def parsing(self, response):
        financeType = self.getFinanceType(response._url)
        self.runFinanceType(financeType, response)

    def runFinanceType(self, financeType, response):
        if (financeType == self.BalanceType):
            self.runBalanceAndCashFlow(response)
        else:
            self.runIncomeStatement(response)

    def getCurrency(self, response):
        return response.xpath("//div[@id='rightcol']/table[@id='yfncsumtab']/tr/td/table/tr/td/small/text()").extract()[0]

    def runBalanceAndCashFlow(self, response):
        symbol = self.getSymbol(response)
        currency = self.getCurrency(response)
        colHeaders = response.xpath("//table[@class='yfnc_tabledata1']/tr/td/table/tr/td[@class='yfnc_modtitle1']/b/text()").extract()
        data = response.xpath("//table[@class='yfnc_tabledata1']/tr/td/table/tr/td/text()").extract()
        boldData = response.xpath("//table[@class='yfnc_tabledata1']/tr/td/table/tr/td/strong/text()").extract()
        models = []
#        print symbol + " this is the symbol "  + str(len(colHeaders))

        for colIndex, col in enumerate(colHeaders):
            m = InsertModel(self.table)
            m.insert("Date", self.convertDate(col))
            m.insert("symbol", symbol)
            m.insert("currency", currency)
            dataCount = 0
            while(dataCount < len(data)):
                d = self.f.filterNonListedData(data[dataCount])
                dataCount += 1
                if (self.headerIsBoldBalanceAndCashFlow(d)):
                    continue
                elif (d == ""):
                    continue
                else:
                    header = d
                    DATA = self.f.fixNumber(self.f.filterNonListedData(data[dataCount + colIndex]))
#                    print header + "    " + DATA
                    m.insert(header, DATA)
                    dataCount += len(colHeaders)
            boldCount = 0
            while(boldCount < len(boldData)):
                bold = self.f.filterNonListedData(boldData[boldCount])
                boldCount += 1
                if (bold == ""):
                    continue
                elif (self.headerIsBoldBalanceAndCashFlow(bold)):
                    continue
                else:
                    header = bold
                    DATA = self.f.fixNumber(self.f.filterNonListedData(boldData[boldCount + colIndex]))
#                    print header + "    " + DATA
                    m.insert(header, DATA)
                    boldCount += len(colHeaders)
#            print m
            models.append(m)
        self.controller.insert(symbol, models)

    def headerIsBoldBalanceAndCashFlow(self, d):
       return (("CurrentAssets" == d) or ("CurrentLiabilities" == d) or ("Assets" == d) 
            or ("Liabilities" == d) or ("Stockholders'Equity" == d) or ("OperatingActivitiesCashFlowsProvidedByorUsedIn" == d)
            or ("InvestingActivitiesCashFlowsProvidedByorUsedIn" == d) or ("FinancingActivitiesCashFlowsProvidedByorUsedIn" == d))

    def runIncomeStatement(self, response):
        symbol = self.getSymbol(response)
        currency = self.getCurrency(response)
        print symbol + " currency: " + str(currency)
        Colheaders = response.xpath('//table[@class="yfnc_tabledata1"]/tr/td/table/tr/th/text()').extract()
        strongHeaders = response.xpath('//table[@class="yfnc_tabledata1"]/tr/td/table/tr/td[@colspan="2"]/strong/text()').extract()
        strongData = response.xpath('//table[@class="yfnc_tabledata1"]/tr/td/table/tr/td[@align="right"]/strong/text()').extract()
        headers = response.xpath('//table[@class="yfnc_tabledata1"]/tr/td/table/tr/td/text()').extract()
        data = response.xpath('//table[@class="yfnc_tabledata1"]/tr/td/table/tr/td[@align="right"]/text()').extract()

        models = []
        for colIndex, col in enumerate(Colheaders):
            m = InsertModel(self.table)
#            print col
            m.insert("Date", self.convertDate(col))
            m.insert("symbol", symbol)
            m.insert("currency", currency)
            for shIndex, SH in enumerate(strongHeaders):
                header = self.f.filterNonListedData(SH)
                data = self.f.fixNumber(self.f.filterNonListedData(strongData[colIndex + (shIndex * len(Colheaders))]))
#                print header + "    " + data
                m.insert(header, data)
            hIndex = 0
            dataOff = 0
            headerSet = 1 + len(Colheaders)
            headerSetCount = 0
            while (headerSetCount < len(headers)):
                h = self.f.filterNonListedData(headers[headerSetCount])
                headerSetCount += 1
                if (self.headerIsBoldIncomeStatements(h)):
                    continue
                if (h == ""):
                    continue
                head = h
                headerCount = headerSetCount + colIndex
                theData = self.f.fixNumber(self.f.filterNonListedData(headers[headerCount]))
#                print head + "    " + theData
                m.insert(head, theData)
                headerSetCount += len(Colheaders)
            models.append(m)
        self.controller.insert(symbol, models)

    def headerIsBoldIncomeStatements(self, h):
        return ( ("OperatingExpenses" == h) or ("IncomefromContinuingOperations" in h)
            or ("Non-recurringEvents" in h) or ("-" in h) or ("CurrentAssets" in h) or 
            ("Current Liabilities" in h))

    def getSymbol(self, response):
        url = response._url
        startPlace = url.find("=")
        endPlace = url.find("+")
        return url[startPlace + 1: endPlace]

    def getFinanceType(self, url):
        if ("Balance+Sheet" in url):
            if ("quarterly" in url):
                self.table = "YahooQuarterlyBalanceSheets"
            else:
                self.table = "YahooAnnualBalanceSheets"
            return self.BalanceType
        elif ("Cash+Flow" in url):
            if ("quarterly" in url):
                self.table = "YahooQuarterlyCashFlowStatements"
            else:
                self.table = "YahooAnnualCashFlowStatements"
            return self.BalanceType
        else:
            if ("quarterly" in url):
                self.table = "YahooQuarterlyIncomeStatements"
            else:
                self.table = "YahooAnnualIncomeStatements"
            return self.IncomeType

    def convertDate(self, date):
        return str(datetime.datetime.strptime(date , "%b %d, %Y").date())
