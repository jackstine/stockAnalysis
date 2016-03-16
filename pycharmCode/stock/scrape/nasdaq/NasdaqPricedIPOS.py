import urllib2
from scrapy.selector import Selector
from stock.common.utility import Filter
from stock.streams.models import InsertModel

class NasdaqPricedIPOS:
    table = "NasdaqPricedIPOS"

    def __init__(self):
        self.f = Filter()

    def run(self):
        site = urllib2.urlopen("http://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings")
        html = site.read()
        response = Selector(text = html, type = "html")

        header = response.xpath("//div[@class='genTable']/table/thead/tr/th/text()").extract()
        header = self.f.mushList(header)
        data = response.xpath("//div[@class='genTable']/table/tbody/tr/td/text()").extract()
        companyNamesAndSymbols = response.xpath("//div[@class='genTable']/table/tbody/tr/td/a/text()").extract()

        models = []
        c = 0
        d = 0
        while( d != len(data)):
            m = InsertModel(self.table)
            for index,h in enumerate(header):
                if ( index >= 0 and index <= 2):
                    if (index == 2 and (not self.isMarket(companyNamesAndSymbols[c]))):
                        m.insert(h, data[d])
                        d += 1
                        continue
                    m.insert(h, self.f.filterForSQL(companyNamesAndSymbols[c]))
                    c += 1
                    continue
                elif (index == 6):
                    m.insert(h, self.f.convertDate(data[d]))
                else:
                    m.insert(h, self.f.filterNonListedData(data[d]))
                d += 1
            print m
            models.append(m)
        return models

    def isMarket(self, com):
        if (com == "NASDAQ" or com == "New York Stock Exchange" or com == "American Stock Exchange"):
            return True
        return False
