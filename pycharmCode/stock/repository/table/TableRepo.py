from stock.repository import RepoI

class TableRepo(RepoI):

    def __init__(self, table, db):
        RepoI.__init__(self, table, db)
        self.db = db
        self.table = table

    def getDescription(self):
        return self.db.describe(self.table)
