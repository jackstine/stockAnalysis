from Common.utility import Filter
from scrapy.selector import Selector
import urllib2
from pycharmCode.stock.models.SymbolChange import SymbolChange

class NasdaqSymbolChange:
    def __init__(self):
        self.f = Filter()

    def run(self, getAll = False):
        html = urllib2.urlopen("http://www.nasdaq.com/markets/stocks/symbol-change-history.aspx?sortby=EFFECTIVE&descending=Y").read()
        response = Selector(text=html, type="html")
        if (getAll):
            largeNum = str(self.getLargestPageNumber(response))
            return self.getAllSymbolChanges(largeNum)
        else:
            return self.getSymbolChanges(response)

    def getAllSymbolChanges(self, num):
        symbolChanges = list()
        for i in range(1, int(num) + 1):
            html = urllib2.urlopen("http://www.nasdaq.com/markets/stocks/symbol-change-history.aspx?sortby=EFFECTIVE&descending=Y&page=" + str(i)).read()
            response = Selector(text=html, type="html")
            symbolChanges.extend(self.getSymbolChanges(response))
        return symbolChanges

    def getLargestPageNumber(self, response):
        pages = response.xpath("//ul[@class='pager']/li/a/text()").extract()
        largestNumber = 0
        for i in pages:
            try:
                if (int(i)):
                    largestNumber = int(i)
            except:
                pass
        return largestNumber

    def getSymbolChanges(self, response):
        oldSymbolAndDate = response.xpath("//div[@class='genTable']/table/tr/td/text()").extract()
        newSymbols = response.xpath("//div[@class='genTable']/table/tr/td/a/text()").extract()
        changes = list()
        for i in range(0,len(newSymbols)):
            changes.append(SymbolChange())
        count = 0
        for i,symbolDate in enumerate(oldSymbolAndDate):
            if (i%2 ==0):
                changes[count].oldSymbol = symbolDate.strip()
            else:
                changes[count].date = self.f.convertDate(symbolDate.strip())
                count += 1
        for i, newSym in enumerate(newSymbols):
            changes[i].newSymbol = newSym.strip()
        return changes
