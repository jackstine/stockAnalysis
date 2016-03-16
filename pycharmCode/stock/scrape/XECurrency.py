import urllib2, subprocess
from stock.streams.models import InsertModel
from scrapy.selector import Selector
from stock.common.utility import Filter


class XECurrency:
    tableListing = "XECurrencyListing"
    tablePricing = "XECurrencyPricing"

    def __init__(self):
        self.f = Filter()

    def run(self):
        information = subprocess.Popen("curl http://www.xe.com/currencytables/?from=USD", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        html , errors = information.communicate()
        response = Selector(text = html, type = "html")
        headers = response.xpath("//div[@class='ICTtableDiv']/table/thead/tr/th/text()").extract()
        codes = response.xpath("//div[@class='ICTtableDiv']/table/tbody/tr/td/a/text()").extract()
        data = response.xpath("//div[@class='ICTtableDiv']/table/tbody/tr/td/text()").extract()

        self.pricingModels = []
        self.listingModels = []
        d = 0
        for c in codes:
            m = InsertModel(self.tablePricing)
            y = InsertModel(self.tableListing)
            for index,h in enumerate(headers):
                if (index == 0):
                    head = self.f.filterNewLine(h)
                    CODE = self.f.filterNonListedData(c)
                    m.insert("Code", CODE)
                    y.insert("Code", CODE)
                elif (index == 1 or index== 3):
                    continue
                elif (index == 2):
                    head = self.f.filterNewLine(h)
                    NAME = self.f.filterForSQL(self.f.filterNonListedData(data[d]))
                    y.insert("Name", NAME)
                    d += 1
                else:
                    m.insert(self.f.mushString(self.f.filterNewLine(h)), self.f.filterNonListedData(data[d]))
                    d += 1
            self.listingModels.append(y)
            self.pricingModels.append(m)
