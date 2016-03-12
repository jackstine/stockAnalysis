from ..InsertModels import *
from ...models.ModelAlgorithms import getDifference
from ...scrape.nasdaq import NasdaqPricedIPOS
from ...repository.nasdaq import NasdaqPricedIPOSRepository

class NasdaqPricedIPOSController:

    def __init__(self, stream):
        self.mysql = stream
        self.scrape = NasdaqPricedIPOS()

    def run(self):
        #should reflect IPOS off upcoming IPOS
        models = self.scrape.run()
        approved = self.getFilteredModels(models)
        insertModelList(approved, self.mysql)
        #the Priced IPOS show up the day after they are priced

    def getFilteredModels(self, insertModels):
        dbModels = NasdaqPricedIPOSRepository().selectWithIn30Days(self.mysql)
        fields = ["symbol", "DatePriced"]
        return getDifference(dbModels, insertModels, fields)
