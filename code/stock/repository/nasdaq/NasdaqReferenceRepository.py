from ..Repo import Repo
from ...models import Model

class NasdaqReferenceRepository(Repo):
    STOCK_COLUMN = 0

    def __init__(self):
        self.table = "NasdaqListingReference"
        Repo.__init__(self, self.table)

    def select(self, letter, mysql):
        select = self.selectQuery(letter, mysql)
        select.execute()
        return select.model

    def updateLetterIfIn(self, entries, mysql):
        fields = ["reference"]
        Repo._update(self, entries, mysql, fields, "symbol")

    def insertIfNotIn(self, entries, mysql):
        Repo._insert(self, entries, mysql, "symbol")

    def selectQuery(self, letter, mysql):
        model = Model(self.table)
        return mysql.select(model).where("reference", mysql.Ops.EQUALS, letter)

    def leftJoinQuery(self, model2, letter, mysql):
        model = Model(self.table)
        return mysql.leftJoin(model, model2, "symbol").where(self.table + ".reference", mysql.Ops.EQUALS, letter)

