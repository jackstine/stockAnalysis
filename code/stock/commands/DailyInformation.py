from ..controllers.daily import XECurrencyController, BloombergCommoditiesController
from ..controllers.daily import KitcoMetalsController
from ..streams.mysql import DB


class DailyInformation():

    def __init__(self):
        self.mysql = DB(DB.Connections.STOCK)

    def run(self):
        XECurrencyController(self.mysql).run()
#        KitcoMetalsController(self.mysql).run()
        BloombergCommoditiesController(self.mysql).run()
        self.mysql.close()
