from ..InsertModels import *
from ...scrape.nasdaq import NasdaqUpcomingIPOS
from ...models.ModelAlgorithms import getDifference
from ...repository.nasdaq import NasdaqUpcomingIPOSRepository


class NasdaqUpcomingIPOSController:
    def __init__(self, stream):
        self.mysql = stream
        self.scrape = NasdaqUpcomingIPOS()

    def run(self):
        models = self.scrape.run()
        approved = self.filterModels(models)
        insertModelList(approved, self.mysql)
        #TODO get new listed and put on Company Listing
        # or at least check that they have passed on
        #TODO do we want to change the data of the database?  update it

    def filterModels(self, insertModels):
        oldModels = NasdaqUpcomingIPOSRepository().selectWithIn30Days(self.mysql)
        fields = ["symbol"]
        return getDifference(oldModels, insertModels, fields)
