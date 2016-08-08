from pycharmCode.stock.scrape.nasdaq import NasdaqDelisted
from pycharmCode.stock.controllers.InsertModels import *
from pycharmCode.stock.repository.nasdaq import NasdaqSuspensionRepository
from datetime import datetime
from pycharmCode.stock.streams.models.ModelAlgorithms import getDifference

class NasdaqDelistedController:

    def __init__(self, stream):
        self.mysql = stream
        self.scrape = NasdaqDelisted()

    def run(self):
        models = self.scrape.run()
        approved = self.filterModelList(models)
        insertModelList(approved, self.mysql)
        #TODO change company Listing
        #TODO add to Archive List
        self.mysql.commit()


    def filterModelList(self, models):
        #TODO refine to a date
        oldModels = NasdaqSuspensionRepository().select(self.mysql)
        fields = ["symbol", "effectivedate"]
        return getDifference(oldModels, models, fields)
