from pycharmCode.stock.repository import RepoI
from pycharmCode.stock.streams.models import InsertModel, Model

class IDSymbolRepo(RepoI):
    STOCK_COLUMN = 1
    DELISTED_SYMBOL = "-----"

    def __init__(self, stream):
        self.table = "IDSymbol"
        self.stream = stream
        RepoI.__init__(self, self.table, stream,primary = "id")

    def insert(self, symbol):
        model = InsertModel(self.table)
        model.insert("symbol", symbol)
        self.insertSingle(model)

    def insertIfNotIn(self, models):
        RepoI._insert(self,models,"symbol")

    def delist(self,id):
        model = RepoI.getInsertModel(self)
        model.insert("id",id)
        model.insert("symbol",self.DELISTED_SYMBOL)
        self._update([model], ["symbol"], "id")

    def leftJoinQuery(self, model2, letter):
        model = Model(self.table)
        return self.stream.leftJoin(model, model2, "id").where(self.table + ".reference", self.stream.Ops.EQUALS, letter)