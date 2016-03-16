from stock.repository import RepoI
from stock.streams.models import Model

class NasdaqReferenceRepository(RepoI):
    STOCK_COLUMN = 0

    def __init__(self, stream):
        self.table = "NasdaqListingReference"
        self.stream = stream
        RepoI.__init__(self, self.table, self.stream)

    def select(self, letter):
        select = self.selectQuery(letter)
        select.execute()
        return select.model

    def updateLetterIfIn(self, entries):
        fields = ["reference"]
        RepoI._update(self, entries, fields, "symbol")

    def insertIfNotIn(self, entries):
        RepoI._insert(self, entries, "symbol")

    def selectQuery(self, letter):
        model = Model(self.table)
        return self.stream.select(model).where("reference", self.stream.Ops.EQUALS, letter)

    def leftJoinQuery(self, model2, letter):
        model = Model(self.table)
        return self.stream.leftJoin(model, model2, "symbol").where(self.table + ".reference", self.stream.Ops.EQUALS, letter)

