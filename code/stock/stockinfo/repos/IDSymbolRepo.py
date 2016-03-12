from ...repository import RepoI
from ...models import InsertModel

class IDSymbolRepo(RepoI):

    def __init__(self, stream):
        self.table = "IDSymbol"
        self.stream = stream
        RepoI.__init__(self, self.table, stream,primary = "id")

    def insert(self, symbol):
        model = InsertModel(self.table)
        model.insert("symbol", symbol)
        self.insertSingle(model)
