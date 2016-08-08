import os
import re
import scrapy
import string

from scrapy.selector import Selector

from Common.utility import Filter
from pycharmCode.stock.controllers.nasdaq import NasdaqSummaryController
from ..Quote import Quote


#TODO make sure that the Summary Quote has no errors
#TODO make error checking software,  that makes sure that I am getting the right data

class QuoteSpider(scrapy.Spider):
    #TODO the share volume is hidden away in the xpath
    name = "QuoteSpider"
    controller = NasdaqSummaryController()

    def __init__(self,category=None,letter=None,single=None,*args,**kwargs):
        self.f=Filter()
        if (single==None):
            super(QuoteSpider,self).__init__(*args,**kwargs)
            self.directory=os.path.dirname(os.path.realpath(__file__))
            letter=self._getLetter()
            symbols=self.controller.getCompanySymbols(letter)
            self._getStartingURLS(symbols)

    def parse(self,response):
        item = self.parseResponse(response)
        self.controller.insertNasdaqSummaryQuote(item)

    def parseResponse(self, response):
        item = Quote()
        self._fixDifficulties(item)
        regex = re.compile(r'<!--(.*)-->', re.DOTALL)
        comment = response.xpath("//div[@class='genTable thin']/table/tbody/comment()").re(regex)[3]
        commentSel = Selector(text = comment, type ="html")
        item["TotalSharesOutstanding"] = self.f.fixListedData(commentSel.xpath("//td[@align = 'right']/text()").extract())
        #print item["TotalSharesOutstanding"]
        item["Symbol"] = self.f.fixListedData(response.xpath('//div[@class="qbreadcrumb"]/span/b/text()').extract())
        #print item["Symbol"]
        item["Exchange"] = self.f.fixListedData(response.xpath('//div[@id = "qwidget-sector-wrap"]/span/text()').extract())
        #print item["Exchange"]
        item["Industry"] = self.f.fixListedData(response.xpath('//div[@id = "qwidget-sector-wrap"]/span/a/text()').extract())
        #print item["Industry"]
        item["LastSale"] = self.f.fixListedData(response.xpath('//div[@id="qwidget_lastsale"]/text()').extract())
        treePath=response.xpath('//div[@class="genTable thin"]/table/tbody/tr')
        for sel in treePath:
            data = self.f.fixListedData(sel.xpath('td[@align="right"]/text()').extract())
            header = self._fixHeader(sel.xpath('td[1]/text()').extract())
            otherHeader = self._fixOtherHeader(sel.xpath('td/a/text()').extract())
            header = self._collectHeader(header,otherHeader)
            #print header + '   ' + data
            item[header] = data
        highLowVolume = treePath.xpath('./td[@align = "right"]/label/text()').extract()   #<<this pulls the high low and the share volume of the day
        item["TodayHigh"] = self.f.fixNonListedData(highLowVolume[0])[1:]
        #print item["TodayHigh"]
        item["TodayLow"] = self.f.fixNonListedData(highLowVolume[1])[1:]
        #print item["TodayLow"]
        item["Volume"] = self.f.fixNonListedData(highLowVolume[2])
        #print item["Volume"]
        return item

    def closed(self,reason):
        self.controller.commit()

    def _getStartingURLS(self,symbols):
        self.start_urls=[]
        for index,sym in enumerate(symbols):
            self.start_urls+=["http://www.nasdaq.com/symbol/"+sym]

    def _getLetter(self):
        """
        Used to get the letter for the database
        """
        f=open(self.directory+"/letter.txt","r")
        letter=f.read()[0]	#we only need the first character
        f.close()
        return letter

    def _fixDifficulties(self,Quote):
        """This method fixes any problems that might arise when a Quote is not fully used. First case
        was when Marketcap was not instanstiated
        """
        Quote["Marketcap"]=0

    def _collectHeader(self,header,otherHeader):
        """ because of discrepancies we need to choose otherHeader only if it has a length
        """
        returnHeader=""
        if not len(otherHeader)>0:
            returnHeader=header[0]
        else:
            returnHeader=otherHeader
        return self._headerFilter(returnHeader)

    def _fixOtherHeader(self,otherHeader):
        """formats and strips the otherHeader
        """
        if (len(otherHeader)>1):
            return string.strip(otherHeader[0])
        else:
            return otherHeader

    def _fixHeader(self,header):
        """this is used to make the header better
        """
        if (len(header)==2):	#this makes some of it work
            return [""]
        else:
            return header

    def _headerFilter(self,header):
        """This is used to filter the header for the Fields in the Scrapy Items
        """
        if (len(header)==1):	#for some discrepancies it will come as a list,  need to shorten it to a string
            header=header[0]
        charactersToFilter="()'`1234567890 /.:"
        newHeader=''.join(c for c in header if c not in charactersToFilter)
        return newHeader
