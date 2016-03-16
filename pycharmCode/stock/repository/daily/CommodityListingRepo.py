from stock.repository import Repo

class CommodityListingRepo(Repo):

    def __init__(self):
        self.table = "CommodityListings"
        Repo.__init__(self, self.table)

    def insertIfNotIn(self, models, mysql):
        Repo._insert(self, models, mysql, "CIndex")
        mysql.commit()
