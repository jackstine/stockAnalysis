import urllib2, json, requests
import circumpunct.model as m
from circumpunct.Auth import getBasicAuth
from circumpunct.model import Stock

def getWatchList():
    request = urllib2.urlopen("https://circumpunct.outsystemscloud.com/StockOpinions/rest/WatchList/get")
    html = request.read()
    watches = list()
    for i in json.loads(html):
        watches.append(m.WatchList(i))
    return watches

def getStocks():
    response = requests.get('https://circumpunct.outsystemscloud.com/StockOpinions/rest/Stock/getStocks',auth=getBasicAuth())
    stocks = list()
    for i in response.json():
        stocks.append(Stock(i))
    return stocks

def updateStockData(stockData):
    response = requests.post("https://circumpunct.outsystemscloud.com/StockOpinions/rest/Stock/updateStockPrice", auth=getBasicAuth(),
                             json = {"StockId":stockData.stockId, "price":stockData.price, "date":str(stockData.date)})
    return response

def insertSymbol(symbol):
    response = requests.put('https://circumpunct.outsystemscloud.com/StockOpinions/rest/Stock/insertSymbol', auth=getBasicAuth(), json = {"symbol":symbol})
    return response

def updateStock(stock):
    response = requests.put('https://circumpunct.outsystemscloud.com/StockOpinions/rest/Stock/updateSymbol', auth=getBasicAuth(),
        json = {"currentSymbol":stock.symbol,"isDelisted":stock.isDelisted, "Id":stock.ID})
    return response

def getStockOpinionWebPage(id):
    return "https://circumpunct.outsystemscloud.com/StockOpinions/StockOpinionDetail.aspx?Entry=1&StockOpinionId=" + str(id) + "&%28Not.Licensed.For.Production%29="

