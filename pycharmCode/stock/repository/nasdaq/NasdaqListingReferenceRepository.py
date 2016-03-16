from stock.repository import Repo

class NasdaqListingReferenceRepository(Repo):

    def __init__(self):
        self.table = "NasdaqListingReference"
        Repo.__init__(self, self.table)
