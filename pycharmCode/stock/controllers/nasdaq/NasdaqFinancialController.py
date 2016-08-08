from pycharmCode.stock.streams.mysql import DB, Ops
from pycharmCode.stock.streams.mysql.connections import Connections
from pycharmCode.stock.streams.models import Model

class NasdaqFinancialController:

    def __init__(self):
        self.mysql = DB(Connections.STOCK)

    def getCompanySymbols(self, letter):
        model = Model("NasdaqListingReference")
        self.mysql.select(model).where("Reference", Ops.EQUALS, letter).execute()
        return model

    def insertNasdaqAnnualBalanceSheet(self, item):
        self.mysql.insertNasdaqAnnualBalanceSheet(item)

    def insertNasdaqQarterlyBalanceSheet(self, item):
        self.mysql.insertNasdaqQuarterlyBalanceSheet(item)

    def insertNasdaqAnnualCashFlow(self, item):
        self.mysql.insertNasdaqAnnualCashFlow(item)

    def insertNasdaqQuarterlyCashFlow(self, item):
       self.mysql.insertNasdaqQuarterlyCashFlo(item)

    def insertNasdaqAnnualIncomeStatement(self, item):
       self.mysql.insertNasdaqAnnualIncomeStatemen(item)

    def insertNasdaqQuarterlyIncomeStatement(self, item):
       self.mysql.insertNasdaqQuarterlyIncomeStatemen(item)
