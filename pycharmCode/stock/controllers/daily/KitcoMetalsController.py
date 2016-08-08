from ...models import Model
from ...utility import Filter

from pycharmCode.stock.scrape import KitcoMetals


class KitcoMetalsController:

    def __init__(self, stream):
        self.scrape = KitcoMetals()
        self.mysql = stream
        self.f = Filter()

    def run(self):
        self.scrape.getMetalPrices()
        for info in self.scrape.information:
            self.insertPriceInfo(info)
        self.mysql.commit()

    def insertPriceInfo(self, info):
        model = Model("MetalPrice")
        model.addFieldValue("name", info["name"])
        model.addFieldValue("bid", info["bid"])
        model.addFieldValue("date", self.f.convertDate(info["date"]))
        self.mysql.insert(model).queue()
