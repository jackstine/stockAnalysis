import urllib2
from ..utility import Filter
from scrapy.selector import Selector
from ..models import InsertModel
from datetime import datetime

class BloombergCommodities:
    tablePrice = "CommoditiesPrice"
    tableIndex = "CommodityListings"

    def __init__(self):
        self.f = Filter()

    def run(self):
        self.pricingModels = []
        self.listingModels = []
        self.parseCommodity("http://www.bloomberg.com/energy")
        self.pricingModels.append(self.pricingModel)
        self.listingModels.append(self.listingModel)
        self.parseCommodity("http://www.bloomberg.com/markets/commodities/futures/metals")
        self.pricingModels.append(self.pricingModel)
        self.listingModels.append(self.listingModel)
        self.parseCommodity("http://www.bloomberg.com/markets/commodities/futures/agriculture")
        self.pricingModels.append(self.pricingModel)
        self.listingModels.append(self.listingModel)

    def parseCommodity(self, site):
        html = urllib2.urlopen(site).read()
        response = Selector(text = html, type = "html")
        headers = response.xpath("//div[@class='data-tables']/div/table/thead/tr/th/text()").extract()
        data = response.xpath("//div[@class='data-tables']/div[@class='table-container']/table/tbody/tr/td/text()").extract()
        indexes = response.xpath("//div[@class='data-tables']/div[@class='table-container']/table/tbody/tr/td/a/div[@data-type = 'abbreviation']/text()").extract()
        indexNames = response.xpath("//div[@class='data-tables']/div[@class='table-container']/table/tbody/tr/td/a/div[@data-type = 'full']/text()").extract()
 
        self.pricingModel = []
        self.listingModel = []
        inN = 0
        x = 0
        d = 0
        self.parseWebsite(inN, x, d, indexes, indexNames, headers, data)

    def parseWebsite(self, inN, x, d, indexes, indexNames, headers, data):
        while (inN < len(indexNames)):
            d += 2
            m, y = self.createModels()
            for index,h in enumerate(headers[:7]):
                if (h == "%Change" or h == 'Time ET' or h == 'Change'):
                    d += 1
                    continue
                if (index == 0):
                    m.insert("CIndex", self.f.filterNonListedData(indexes[x]))
                    y.insert("Name", self.f.filterForSQL(self.f.filterNonListedData(indexNames[inN])))
                    y.insert("CIndex", self.f.filterNonListedData(indexes[x]))
                    inN += 1
                    x += 1 
                    if ("Wool" in y.getValue("Name")):
                        while("1000" not in data[d]):
                            d += 1
                        d -= 2
                        break
                    continue
                else:
                    isASpotAndHasNoUnit = "Spot" in y.getValue("Name") and index == 1 and self.f.isNumber(data[d])
                    if (isASpotAndHasNoUnit):
                        m.insert(h, "NULL")
                    elif (index == 2):
                        m.insert(h, self.f.filterNonListedData(data[d]))
                        d += 1
                    else:
                        m.insert(h, data[d])
                        d += 1
            if ("Wool" in y.getValue("Name")):
                continue
            self.listingModel.append(y)
            self.pricingModel.append(m)

    def createModels(self):
        m = InsertModel(self.tablePrice)
        y = InsertModel(self.tableIndex)
        m.insert("date", str(datetime.today()))
        return m, y
