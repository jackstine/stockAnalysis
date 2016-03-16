from stock.repository import Repo

class NasdaqPricedIPOSRepository(Repo):

    def __init__(self):
        Repo.__init__(self, "NasdaqPricedIPOS", queryWithIn30Days = "DatePriced")
        self.table = "NasdaqPricedIPOS"
