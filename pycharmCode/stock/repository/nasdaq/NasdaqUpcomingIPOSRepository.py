from stock.streams.models import Model
from stock.streams.mysql import Ops
from stock.repository.Repo import Repo

class NasdaqUpcomingIPOSRepository(Repo):
    def __init__(self):
        Repo.__init__(self, "NasdaqUpcomingIPOS", queryWithIn30Days = "dateInserted")
        self.table = "NasdaqUpcomingIPOS"
