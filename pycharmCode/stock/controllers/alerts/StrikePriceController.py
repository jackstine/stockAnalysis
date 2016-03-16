from ...repository.alerts import StrikePriceRepo
from ...streams.mysql import DB
from ...scrape.ScrapyAPI import *
from ...utility.Texting import *

class StrikePriceController:
    def __init__(self):
        self.stream = DB(DB.Connections.STOCK)
        self.repo = StrikePriceRepo()

    def run(self):
        models = self.repo.selectAll(self.stream).getDictRows()
        for m in models:
            self.validate(m)

    def validate(self, m):
        strike = m["quoteprice"]
        t = m["type"]
        symbol = m["symbol"]
        summ = getNasdaqSummary(symbol)
        price = summ["LastSale"]
        if (t == "below"):
            if (price < strike):
                message = "The Symbol " + symbol +" is doing BAD for you            It is currently at " + str(price)
                textMe(message)
        elif (t == "above"):
            if (price > strike):
                message = "The Symbol " + symbol +" is doing GREAT for you               It is currently at " + str(price)
                textMe(message)
        else:
            print "Validate in StrikePriceControlller is something wrong in DB for symbol " + m["symbol"]

