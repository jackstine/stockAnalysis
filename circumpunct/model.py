from Common.U import getFromDict as vjson

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

    def canBuy(self):
        return self.summary.price <= self.buyPrice

    def isLow(self):
        return self.summary.price <= self.targetPriceLow

    def isHigh(self):
        return self.summary.price >= self.targetPriceHigh

    def getSymbol(self):
        return self.summary.symbol

class Stock:
    def __init__(self, json):
        self.isDelisted = vjson(json, "isDelisted")
        self.ID = vjson(json,"Id")
        self.symbol = vjson(json, "currentSymbol")