from Common.U import getFromDict as vjson
import datetime

class WatchList:
    def __init__(self, json):
        self.expiringDate = vjson(json,"expiringDate")
        self.dateIpdated = vjson(json,"dateUpdated")
        self.id = vjson(json,"Id")
        self.stockId = vjson(json,"StockId")
        self.buyPrice = vjson(json,"buyPrice")
        self.targetPriceLow = vjson(json,"targetPriceLow")
        self.targetPriceHigh = vjson(json,"targetPriceHigh")
        self.json = json

    def __str__(self):
        return self.json

    def setSummary(self,summary):
        self.summary = summary
        self.symbol = summary.symbol
        self.price = summary.price

    def canBuy(self):
        return self.price <= self.buyPrice

    def isLow(self):
        return self.price <= self.targetPriceLow

    def isHigh(self):
        return self.price >= self.targetPriceHigh

    def getSymbol(self):
        return self.symbol

    def setPriceModel(self, pricemodel):
        self.priceModel = pricemodel
        self.symbol = pricemodel.symbol
        self.price = pricemodel.price

class Stock:
    def __init__(self, json):
        self.isDelisted = vjson(json, "isDelisted")
        self.ID = vjson(json,"Id")
        self.symbol = vjson(json, "currentSymbol")

class StockData:
    def __init__(self, ID, price):
        self.stockId = ID
        self.price = price
        self.date = datetime.datetime.now()