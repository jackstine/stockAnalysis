from pycharmCode.stock.controllers.InsertModels import *
from pycharmCode.stock.streams.models.ModelAlgorithms import getDifference
from pycharmCode.stock.scrape.nasdaq import NasdaqPricedIPOS
from pycharmCode.stock.repository.nasdaq import NasdaqPricedIPOSRepository

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
