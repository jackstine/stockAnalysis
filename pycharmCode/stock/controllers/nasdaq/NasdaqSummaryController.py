from stock.stockinfo.api import StockInfoAPI
from stock.streams.mysql import DB
from stock.streams.models import Model
from stock.streams.mysql.connections import Connections
from stock.streams.mysql import Ops
import datetime, string, os

class NasdaqSummaryController:

    def __init__(self):
        self.mysql = DB(Connections.STOCK)
        self.api = StockInfoAPI(self.mysql)
        self.ids = self.api.getAllSymbolToID()

    def getCompanySymbols(self,letter):
        return self.api.getSymbolsWithReference(letter)

    def insertNasdaqSummaryQuote(self, item):
        self.insertExchange(item)
        self.insertQuote(item)

    def insertExchange(self, info):
        #TODO change this up NOW
        id = self.ids[info["Symbol"]]
        model = Model("NasdaqCompanyListing")
        model.addFieldValue("exchange", info["Exchange"])
        self.mysql.update(model).where("symbol", Ops.EQUALS, info["Symbol"]).queue()

    def insertQuote(self, item):
        id = self.ids[item["Symbol"]]
        model = Model("NasdaqSummaryQuote")
        model.addFieldValue("id", id)
        model.addFieldValue("date", str(datetime.date.today()))
        model.addFieldValue("quote", item["LastSale"])
        model.addFieldValue("volume", item["Volume"])
        model.addFieldValue("low", item["TodayLow"])
        model.addFieldValue("high", item["TodayHigh"])
        model.addFieldValue("outstandingShares", item["TotalSharesOutstanding"])
        self.mysql.insert(model).queue()

    def commit(self):
        self.mysql.commit()
        self.mysql.close()
