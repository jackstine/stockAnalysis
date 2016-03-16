import urllib2
import time, datetime
from scrapy.selector import Selector
from stock.streams.models import InsertModel

class SplitsScrape:
    def __init__(self):
        pass

    def run(self, stockInfos):
        for stockInfo in stockInfos:
            self.scrape(stockInfo)

    def scrape(self, stockInfo):
        s = stockInfo.symbol
        html = urllib2.urlopen("https://www.stocksplithistory.com/?symbol=" + s).read()
        response = Selector(text = html, type = "html")

        splits = response.xpath("//center/div[@style='border: 1px solid #444444; background: #FFFFFF; width:1000px;']"
            + "/table[2]/tr/td[@width='208']/table[@style='font-family: Arial; font-size: 12px']/tr/td/text()").extract()
        inModel = self.getModel(splits, stockInfo.id)


    def getModel(self, splits, id):
        inModels = []
        dateI = 0
        splitInfoI = 1
        step = 2
        lengthOfSplits = len(splits)
        #DateI is the reference of the index that we are using
        while(dateI < lengthOfSplits):
            inModel = InsertModel("StockSplitHistory")
            date = splits[dateI]
            splitInfo = splits[splitInfoI]
            ratio = self.getSplitRatio(splitInfo)
            print date + "      "  +  str(ratio)
            #now we have the splitInfo  and the ratio
            inModel.insert("date", date)
            inModel.insert("id", id)
            inModel.insert("ratio", ratio)
            dateI += step
            splitInfoI += step
            inModels.append(inModel)
        return inModels

    def getSplitRatio(self, info):
        stringSplits = info.split(" ")
        numerator = stringSplits[0]
        denominator = stringSplits[2]
        return (float(numerator) / float(denominator))
