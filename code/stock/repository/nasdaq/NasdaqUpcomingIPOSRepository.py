from ...models import Model
from ...streams.mysql import Ops
from ..Repo import Repo

class NasdaqUpcomingIPOSRepository(Repo):
    def __init__(self):
        Repo.__init__(self, "NasdaqUpcomingIPOS", queryWithIn30Days = "dateInserted")
        self.table = "NasdaqUpcomingIPOS"
