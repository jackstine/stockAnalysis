import urllib2

from scrapy.selector import Selector

from Common.utility import Filter
from pycharmCode.stock.streams.models import InsertModel


class NasdaqFinancials():
    def __init__(self):
        #super(NasdaqFinancials, self).__init__()
        self.table = ""
        self.f = Filter()

    def run(self):
        symbol = "patk"
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials")
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=balance-sheet")
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=cash-flow&data=annual")
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=income-statement&data=quarterly")
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=balance-sheet&data=quarterly")
        self.parse("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=cash-flow&data=quarterly")



#        self.parse(self.site)

    def parse(self, site):
#        cj = cookielib.CookieJar()
#        opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
        url = urllib2.urlopen(site)
        html = url.read()
        print
        print
        
        print site
        print
        response = Selector(text = html, type = "html")
        symbol = response.xpath('//div[@class="qbreadcrumb"]/span/a[3]/text()').extract()[0]
        # Period Ending :    Trend :   are not counted  so we go up 2 in the headers
        headers = response.xpath('//div[@class="genTable"]/table/thead/tr/th/text()').extract()[2:]
        rowHeaders = response.xpath('//div[@class="genTable"]/table/tr/th/text()').extract()
        data = response.xpath('//div[@class="genTable"]/table/tr/td/text()').extract()

        headerStart = self.findQuarterlyHeaders(headers)
        headers = headers[headerStart:]

        print symbol

        print data
        print
        print
        print len(headers)
        print
        print headers
        print

        models = []
        for hIndex, h in enumerate(headers):
            dOff = hIndex
            rIndex = 0
            m = InsertModel(self.table)
            m.insert("date", self.f.convertDate(h))
            for r in rowHeaders:
                if (self.headerRowWithNoData(r)):
                    continue
                m.insert(self.f.filterHeader(self.f.filterForSQL(self.f.mushString(r))), 
                    self.f.convertToNeg(self.f.filterNonListedData(data[dOff + (rIndex * len(headers))])))
                rIndex += 1
            print m
            models.append(m)

    def headerRowWithNoData(self, r):
        if (("Operating Expense" in r) or ("Current Liabilities" in r) or ("Current Assets" in r) or ("Long-Term Assets" in r)
            or ("Stock Holders Equity" in r) or ("Cash Flows-Operating Activities" in r) or ("Changes in Operating Activities" in r)
            or ("Cash Flows-Investing Activities" in r) or ("Cash Flows-Financing Activities" in r)):
            return True
        return False

    def findQuarterlyHeaders(self, headers):
        for index,h in enumerate(headers):
            if ("Quarter Ending:" in h):
                return index + 1
        return 0







class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print "Cookie Manip Right Here"
        print self.parent["http"]
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302



class NoRedirection(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        return response

    https_response = http_response
