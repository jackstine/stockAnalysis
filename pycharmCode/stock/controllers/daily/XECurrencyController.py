from pycharmCode.temp.scrape import XECurrency

from pycharmCode.stock.repository.daily import XECurrencyPricingRepository, XECurrencyListingRepository
from ..InsertModels import *


class XECurrencyController:
    def __init__(self, stream):
        self.mysql = stream
        self.scrape = XECurrency()
        self.pricingRepo = XECurrencyPricingRepository()
        self.listingRepo = XECurrencyListingRepository()

    def run(self):
        self.scrape.run()
        self.listingRepo.insertIfNotIn(self.scrape.listingModels, self.mysql)
        insertModelList(self.scrape.pricingModels, self.mysql)
