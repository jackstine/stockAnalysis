import urllib2
from scrapy.selector import Selector
from Common.utility import Filter
from stock.streams.models import InsertModel


class NasdaqDelisted:
    table = "NasdaqIssuedSuspension"

    def __init__(self):
        self.f = Filter()
        pass

    def run(self):
        site = urllib2.urlopen("https://listingcenter.nasdaq.com/IssuersPendingSuspensionDelisting.aspx")
        html = site.read()
        response = Selector(text = html, type = "html")
        headers = response.xpath("//div[@id='grdView']/div/div/table/thead/tr/th/a/text()").extract()
        headers = self.f.mushList(headers)
        data = response.xpath("//div[@id='grdView']/div/div/table/tbody/tr/td/text()").extract()

        models = []
        d = 0
        while (d != len(data)):
            m = InsertModel(self.table)
            for index,h in enumerate(headers):
                if (index == 4 or index == 5):
                    m.insert(h, self.f.convertDate(data[d]))
                else:
                    m.insert(h, data[d])
                d += 1
            models.append(m)
        return models
