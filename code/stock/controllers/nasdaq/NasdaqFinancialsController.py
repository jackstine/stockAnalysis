from stock.streams.mysql import DB
from stock.streams.mysql.connections import Connections
from stock.scrape.nasdaq import NasdaqFinancials


class NasdaqFinancialsController:

    def __init__(self):
        pass

    def run(self):
        self.getFinancials("PATK")


    def getFinancials(self, symbol):
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials", 
            "NasdaqAnnualIncomeStatements")
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=balance-sheet",
            "nope")
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=cash-flow&data=annual",
            "nope")
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=income-statement&data=quarterly",
            "nope")
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=balance-sheet&data=quarterly",
            "nope")
        self.spawnThread("http://www.nasdaq.com/symbol/" + symbol + "/financials?query=cash-flow&data=quarterly",
            "nope")


    def spawnThread(self, url, table):
        scrape = NasdaqFinancials(url, table)
        scrape.start()
