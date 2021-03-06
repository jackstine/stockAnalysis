from pycharmCode.stock.repository import RepoI
from pycharmCode.stock.streams.mysql import DB

class ConsolidatedRepo(RepoI):

    def __init__(self):
        self.table = "ConsolidatedPrices"
        self.db = DB(DB.Connections.STOCK)
        RepoI.__init__(self, self.table, self.db)
