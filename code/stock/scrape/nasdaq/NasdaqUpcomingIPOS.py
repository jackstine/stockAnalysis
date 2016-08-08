from scrapy.selector import Selector
from Common.utility import Filter
from stock.streams.models import InsertModel
import urllib2

class NasdaqUpcomingIPOS:
    table = "NasdaqUpcomingIPOS"

    def __init__(self):
        self.f = Filter()

    def run(self):
        site = urllib2.urlopen('http://www.nasdaq.com/markets/ipos/activity.aspx?tab=upcoming')
        html = site.read()
        response = Selector(text=html, type='html')

        headers = response.xpath("//div[@class='genTable']/table/thead/tr/th/text()").extract()
        headers = self.f.mushList(headers)
        companyNamesAndSymbols = response.xpath("//div[@class='genTable']/table/tbody/tr/td/a/text()").extract()
        data = response.xpath("//div[@class='genTable']/table/tbody/tr/td/text()").extract()
        return self._setModels(headers, companyNamesAndSymbols, data)

    def _setModels(self, headers, companyNamesAndSymbols, data):
        models = []
        d = 0
        c = 0
        while (d != len(data)):
            m = InsertModel(self.table)
            for index,h in enumerate(headers):
                if (index >= 0 and index <= 2):
                    if (index == 1 and (not self.isSymbol(companyNamesAndSymbols[c]))):
                        m.insert(h, "NULL")
                        continue
                    m.insert(h, self.f.filterForSQL(companyNamesAndSymbols[c]))
                    c += 1
                    continue 
                elif (index == 3):
                    if ("-" in data[d]):
                        prices = data[d].split("-")
                        m.insert("LowPrice", prices[0])
                        m.insert("HighPrice", prices[1])
                    else:
                        price = self.f.filterNonListedData(data[d])
                        m.insert("LowPrice", price)
                        m.insert("HighPrice", price)
                elif (index == 6):
                    m.insert(h, self.f.convertDate(data[d]))
                else:
                    m.insert(h, self.f.filterNonListedData(data[d]))
                d += 1
            models.append(m)
        return models

    def isSymbol(self, com):
        if (com == "NASDAQ" or com == "New York Stock Exchange" or com == "American Stock Exchange"):
            return False
        return True
