from stock.repository import Repo

class NasdaqCompanyListingRepository(Repo):
    def __init__(self):
        self.table = "NasdaqCompanyListing"
        Repo.__init__(self, self.table)

    def updateIfIn(self, entries, mysql, fields = ["exchange", "name"]):
        Repo._update(self, entries, mysql, fields, "symbol")

    def insertIfNotIn(self, entries, mysql):
        Repo._insert(self, entries, mysql, "symbol")
