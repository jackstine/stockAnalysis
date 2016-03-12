import sys, os
sys.path.insert(1,os.path.expanduser("~") + "/Dropbox/Programs/Stock/code/")
from stock.utility import Filter
from stock.controllers.financials import FinancialController
from stock.models import InsertModel
from stock.repository.scrape import ScrapyErrorLog
from stock.scrape import StockScrapy

from financials.spiders.state import GoogleFinState, ABalanceState, ACashState, AIncomeState, QBalanceState, QCashState, QIncomeState
import operator,os
from time import sleep

class GoogleFinancialSpider(StockScrapy):
    name = "GoogleFinancialSpider"
    currentSymbol=""
    start_urls=[]

    def __init__(self,*args,**kwargs):
        super(GoogleFinancialSpider,self).__init__(controlTable = FinancialController.GOOGLE, directory=__file__, *args,**kwargs)

    def _addURLS(self, index, s):
        s = s.replace("^", "-")
        self.start_urls+=["https://www.google.com/finance?q="+ s +"&fstype=ii"]
        return True

    def parsing(self, response):
        self._setCurrentSymbol(response)
        self._getQuartlyInfo(response)
        self._getAnnualInfo(response)

    def _setCurrentSymbol(self,response):
        """Gets the current symbol of the webpage that is being parsed
        and gets the information coresponding to that symbol
        """
        self.symbolInfo = []
        beg=response.url.find("q=")
        end=response.url.find("&")
        self.currentSymbol=response.url[beg+2:end]

    def _getQuartlyInfo(self,response):
        """This gives all the quarterly updates to the database
        """
        self.itemList = []
        self.state=QIncomeState()
        self._getInfo(response)
        self.state=QBalanceState()
        self._getInfo(response)
        self.state=QCashState()
        self._getInfo(response)
        self.controller.insert(self.currentSymbol, self.itemList)

    def _getAnnualInfo(self,response):
        """gets all the Annual info and updates the database
        """
        self.itemList = []
        self.state=AIncomeState()
        self._getInfo(response)
        self.state=ABalanceState()
        self._getInfo(response)
        self.state=ACashState()
        self._getInfo(response)
        self.controller.insert(self.currentSymbol, self.itemList)

    def _getInfo(self,response):
        """This method gets the data from everycall to get the info
        from the website
        """
        table = response.xpath(self.state.xpath)	#the table is the table off the website,  this response gets it
        headerCount, begin = self._getHeader(table)
        self._getData(table,headerCount, begin)
        #TODO make this only 1 type of parameter

    def _getHeader(self,table):
        """knows where the headers from the Google Finance website are
        c/ireates the IncomeItem for the information, puts in the Date of the Item
        """
        headers=table.xpath('thead/tr/th/text()').extract() #<-- this gets the headers
        currencyUnit=""
        currency=""
        count = len(self.itemList)
        begin = len(self.itemList)
        for index,he in enumerate(headers):
            if index==0: 
                #TODO create a test to make sure that this is "In 'currencyUnit' of 'currency' (except for per share items"
                #TODO will not convert the dollar amount, but will make a lookup table for the currencies accepted
                    #so that the main program can convert them need to add a currency to all Financial Database
                    # connections
                split=he.split()
                currencyUnit=split[1]
                currency=split[3]
                continue
            self.itemList+=[InsertModel(self.state.getTable())]
            self.state.formatDate( self.f.filterNewLine(he) , self.itemList[count] )
            self.itemList[count].insert("Symbol", self.currentSymbol)
            self.itemList[count].insert("Currency", currency)
            self.itemList[count].insert("CurrencyUnit", currencyUnit)
            count+=1
        return count, begin

    def _getData(self,table,dateCount, begin):
        """gets the data from the webpage,  separates 
        the header and and adds the data to it
        """
        header=""
        adjustedCount = dateCount - begin
        for index,sel in enumerate(table):
            selector=sel.xpath('tbody/tr/td')
            for i,data in enumerate(selector):
                data=self._findData(data)
                data=self.f.filterNewLine(data)
                if( i%(adjustedCount+1)==0):	#need to get the header for the data
                    header=self.f.filterHeader(data)
                    continue
                else:	#apply the header to the data
                    self.itemList[((i)%( adjustedCount + 1)) - 1 + begin].insert(header,self._filterData(data))

    def _filterData(self,data):
        """the data is filtered of non-necessary information and 
        then if it is a "-"  it is converted to 0
        """
        return self.f.getZero(self.f.filterNonListedData(data))

    def _findData(self,data):
        """Because some of the data has a span on it we will need 
        to identify which one to take
        """
        returnData=""
        tryData=data.xpath('span/text()').extract()
        if (len(tryData)!=0):
            returnData=tryData
        else:
            returnData=data.xpath('text()').extract()
        return returnData
