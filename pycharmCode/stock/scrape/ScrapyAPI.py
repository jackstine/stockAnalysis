from scrapy.selector import Selector
import urllib2

def getNasdaqSummary(symbol):
    response = getNasdaqResponse(symbol)
    from .scrapycrawls.nasdaq.summary.summary.spiders.QuoteSpider import QuoteSpider
    return QuoteSpider(single=True).parseResponse(response)

def getNasdaqResponse(symbol):
    url = "http://www.nasdaq.com/symbol/" + symbol
    return getResponse(url)

def getResponse(url):
    con = urllib2.urlopen(url)
    return Selector(text = con.read(), type = "html")
