from stock.repository import RepoI


class SymbolHistoryRepo(RepoI):
    def __init__(self, stream):
        self.table = "SymbolHistory"
        self.stream = stream
        RepoI.__init__(self, self.table, self.stream)

    def insertIfNotIn(self, models):
        RepoI._insert(self,models,"id")