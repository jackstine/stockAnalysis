from pycharmCode.stock.repository import Repo

class StrikePriceRepo(Repo):

    def __init__(self):
        self.table = "StrikePriceAlerts"
        Repo.__init__(self, self.table)

    def insertBelow(self, symbol, quote, stream):
        m = InsertModel(self.table)
        m.insert("type", "below")
        m.insert("symbol", symbol)
        m.insert("quotePrice", quote)
        stream.insert(m).queue()
