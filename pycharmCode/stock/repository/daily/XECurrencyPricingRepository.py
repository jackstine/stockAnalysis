from stock.repository import Repo

class XECurrencyPricingRepository(Repo):

    def __init__(self):
        self.table = "XECurrencyPricing"
        Repo.__init__(self, self.table)

