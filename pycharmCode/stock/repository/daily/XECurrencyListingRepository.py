from pycharmCode.stock.repository import Repo

class XECurrencyListingRepository(Repo):
    def __init__(self):
        self.table = "XECurrencyListing"
        Repo.__init__(self, self.table)

    def insertIfNotIn(self, models, mysql):
        Repo._insert(self, models, mysql, "code")
        mysql.commit()
