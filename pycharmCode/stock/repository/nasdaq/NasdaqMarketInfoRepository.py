from stock.repository import Repo

class NasdaqMarketInfoRepository(Repo):

    def __init__(self):
        self.table = "NasdaqCompanyMarketInfo"
        Repo.__init__(self, self.table)

    def updateIfIn(self, entries, mysql):
        fields = ["industry", "sector"]
        Repo._update(self,entries, mysql, fields, "symbol")

    def insertIfNotIn(self, entries, mysql):
        Repo._insert(self, entries, mysql, "symbol")
