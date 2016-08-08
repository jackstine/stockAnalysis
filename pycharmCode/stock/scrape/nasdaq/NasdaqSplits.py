import urllib2

from scrapy.selector import Selector

from Common.utility import Filter
from pycharmCode.stock.streams.models import InsertModel


class NasdaqSplits:
    table = "NasdaqSplits"

    def __init__(self):
        self.f = Filter()

    def run(self):
        site = urllib2.urlopen("http://www.nasdaq.com/markets/upcoming-splits.aspx")
        html = site.read()
        response = Selector(text = html, type = "html")

        #headers
        headers = response.xpath('//table[@rules="all"]/tr/th/text()').extract()
        headers = self.f.mushList(headers)
        #data
        data = response.xpath('//table[@rules="all"]/tr/td/text()').extract()
        #companyNames
        companyNames = response.xpath('//table[@rules="all"]/tr/td/a/text()').extract()

        models = []
        d = 0
        for com in companyNames:
            m = InsertModel(self.table)
            splits = self.splitName(com)
            for index,h in enumerate(headers):
                if (index == 0):
                    m.insert("CompanyName", self.f.filterForSQL(splits[1]))
                    m.insert("Symbol", splits[0])
                    continue
                elif (index == 1):
                    m.insert(h, self.getRatio(data[d]))
                else:
                    m.insert(self.f.headerFilter(h), self.f.convertDate(data[d]))
                d += 1
            models.append(m)
        return models

    def getRatio(self, ratio):
        if (":" in ratio):
            splits = ratio.split(":")
            splits[0] = splits[0].strip()
            splits[1] = splits[1].strip()
            ratio = float(splits[0]) / float(splits[1])
            return str(ratio)
        elif ("%" in ratio):
            nums = ratio.split(".")
            nums[1] = nums[1][:len(nums[1]) -1] # gets rid of %
            string = ""
            if (len(nums[0]) == 2):
                string = "0." + nums[0] + nums[1]
            elif (len(nums[0]) == 1):
                string = "0.0"+ nums[0] + nums[1]
            else:
                string = nums[0][:len(nums[0]) - 2] + "." + nums[len(nums[0]) -2:] + nums[1]
            return string

    def splitName(self, com):
        location = com.rfind("(")
        splits = ["",""]
        splits[1] = com[ : location - 1]
        splits[0] = com[location + 1 : -1 ]
        return splits
