import urllib2
import time, datetime
from scrapy.selector import Selector

class SplitsScrape:
    def __init__(self):
        pass

    def run(self, symbols):
        for s in symbols:
            self.scrape(s)

    def scrape(self, s):
        html = urllib2.urlopen("https://www.stocksplithistory.com/?symbol=" + s).read()
        response = Selector(text = html, type = "html")
        splits = response.xpath("//center/div[@style='border: 1px solid #444444; background: #FFFFFF; width:1000px;']"
            + "/table[2]/tr/td[@width='208']/table[@style='font-family: Arial; font-size: 12px']/tr/td/text()").extract()
        dateI = 0
        splitInfoI = 1
        step = 2
        lengthOfSplits = len(splits)
        #DateI is the reference of the index that we are using
        while(dateI < lengthOfSplits):
            date = splits[dateI]
            splitInfo = splits[splitInfoI]
            ratio = self.getSplitRatio(splitInfo)
            print date + "      "  +  str(ratio)
            #now we have the splitInfo  and the ratio


            dateI += step
            splitInfoI += step

    def getSplitRatio(self, info):
        stringSplits = info.split(" ")
        numerator = stringSplits[0]
        denominator = stringSplits[2]
        return (float(numerator) / float(denominator))
