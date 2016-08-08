from Common.utility import Filter
from scrapy.selector import Selector
import urllib2

class NasdaqSymbolChange:
    def __init__(self):
        self.f = Filter()

    def run(self):
        proxy = urllib2.ProxyHandler({"http": ""})
        auth = urllib2.HTTPBasicAuthHandler()
        opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        html = urllib2.urlopen("http://www.google.com").read()
        response = Selector(text=html, type="html")
        #
        # response.xpath("//div[@class='genTable']/table/tr/td/text()").extract()
        # response.xpath("//ul[@class='pager']/li/a/text()").extract()
        headers = response.xpath("//div[@class='genTable']/table/tr/th/a/text()").extract()
        codes = response.xpath("//div[@class='genTable']/table/tr/td/text()").extract()
        data = response.xpath("//ul[@class='pager']/li/a/text()").extract()
        print headers
        print codes
        print data
