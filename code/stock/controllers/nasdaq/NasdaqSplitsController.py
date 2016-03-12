from ...scrape.nasdaq import NasdaqSplits
from ..InsertModels import *
from ...models.ModelAlgorithms import getDifference
from ...repository.nasdaq import NasdaqSplitsRepository

class NasdaqSplitsController():

    def __init__(self, stream):
        self.mysql = stream
        self.scrape = NasdaqSplits()

    def run(self):
        models = self.scrape.run()
        approvedModels = self.getFilteredModels(models)
        insertModelList(approvedModels, self.mysql)
        #TODO change the prices of the stocks that are having splits today
        #TODO might add a splits mark boolean to make sure the change is correct,
        # and that we are not adding a incorrect value
        self.mysql.commit()

    def getFilteredModels(self, models):
        modelInDB = NasdaqSplitsRepository().selectAll(self.mysql)
        fields = ["symbol", "exdate"]
        return getDifference(modelInDB, models, fields)
