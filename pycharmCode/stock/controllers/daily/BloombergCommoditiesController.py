from pycharmCode.temp.scrape import BloombergCommodities

from pycharmCode.stock.repository.daily import CommodityListingRepo
from ..InsertModels import *


class BloombergCommoditiesController:

    def __init__(self, stream):
        self.mysql = stream
        self.scrape = BloombergCommodities()
        self.repo = CommodityListingRepo()

    def run(self):
        self.scrape.run()
        for model in self.scrape.listingModels:
            self.repo.insertIfNotIn(model , self.mysql)
        for model in self.scrape.pricingModels:
            insertModelList(model, self.mysql)
        self.mysql.commit()
