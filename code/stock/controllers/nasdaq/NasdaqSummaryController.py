from ...streams.mysql import DB
from ...models import Model
from ...streams.mysql.connections import Connections
from ...streams.mysql import Ops
import datetime, string, os
from ...repository.nasdaq import NasdaqReferenceRepository

class NasdaqSummaryController:

    def __init__(self):
        self.reference = NasdaqReferenceRepository()
        self.mysql = DB(Connections.STOCK)

    def getCompanySymbols(self, letter):
        return self.reference.select(letter, self.mysql).getRows()

    def insertNasdaqSummaryQuote(self, item):
        self.insertExchange(item)
        self.insertQuote(item)

    def insertExchange(self, info):
        model = Model("NasdaqCompanyListing")
        model.addFieldValue("exchange", info["Exchange"])
        self.mysql.update(model).where("symbol", Ops.EQUALS, info["Symbol"]).queue()

    def insertQuote(self, item):
        model = Model("NasdaqSummaryQuote")
        model.addFieldValue("symbol", item["Symbol"])
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
