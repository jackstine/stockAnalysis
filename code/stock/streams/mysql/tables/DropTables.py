from .. import DB
from ..connections import Connections

class DropTables:
    drops = "DROP TABLE "

    def __init__(self):
        self.mysql = DB(Connections.STOCK)

    def drop(self, table):
        self.mysql.commitExecute(self.drops + table)

    def close(self):
        self.mysql.close()

    def hasNoTable(self, table):
	pass

    def run(self):
        #TODO for future reference we can just SHOW TABLES
        # foreach table in drop
        if ( self.hasNoTable("NasdaqCompanyListing")):
            self.drop("NasdaqCompanyListing")
        if ( self.hasNoTable("NasdaqCompanyMarketInfo")):
            self.drop("NasdaqCompanyMarketInfo")
        if ( self.hasNoTable("GoogleQuarterlyIncomeStatements")):
            self.drop("GoogleQuarterlyIncomeStatements")
        if ( self.hasNoTable("GoogleQuarterlyBalanceSheets")):
            self.drop("GoogleQuarterlyBalanceSheets")
        if ( self.hasNoTable("GoogleQuarterlyCashFlowStatements")):
            self.drop("GoogleQuarterlyCashFlowStatements")
        if ( self.hasNoTable("GoogleAnnualIncomeStatements")):
            self.drop("GoogleAnnualIncomeStatements")
        if ( self.hasNoTable("GoogleAnnualBalanceSheets")):
            self.drop("GoogleAnnualBalanceSheets")
        if ( self.hasNoTable("GoogleAnnualCashFlowStatements")):
            self.drop("GoogleAnnualCashFlowStatements")
#        if ( self.hasNoTable("NasdaqQuarterlyIncomeStatements")):
#            self.drop("NasdaqQuarterlyIncomeStatements")
#        if ( self.hasNoTable("NasdaqQuarterlyBalanceSheets")):
#            self.drop("NasdaqQuarterlyBalanceSheets")
#        if ( self.hasNoTable("NasdaqQuarterlyCashFlowStatements")):
#            self.drop("NasdaqQuarterlyCashFlowStatements")
#        if ( self.hasNoTable("NasdaqAnnualIncomeStatements")):
#            self.drop("NasdaqAnnualIncomeStatements")
#        if ( self.hasNoTable("NasdaqAnnualBalanceSheets")):
#            self.drop("NasdaqAnnualBalanceSheets")
#        if ( self.hasNoTable("NasdaqAnnualCashFlowStatements")):
#            self.drop("NasdaqAnnualCashFlowStatements")
#        if ( self.hasNoTable("YahooQuarterlyIncomeStatements")):
#            self.drop("YahooQuarterlyIncomeStatements")
#        if ( self.hasNoTable("YahooQuarterlyBalanceSheets")):
#            self.drop("YahooQuarterlyBalanceSheets")
#        if ( self.hasNoTable("YahooQuarterlyCashFlowStatements")):
#            self.drop("YahooQuarterlyCashFlowStatements")
#        if ( self.hasNoTable("YahooAnnualIncomeStatements")):
#            self.drop("YahooAnnualIncomeStatements")
#        if ( self.hasNoTable("YahooAnnualBalanceSheets")):
#            self.drop("YahooAnnualBalanceSheets")
#        if ( self.hasNoTable("YahooAnnualCashFlowStatements")):
#            self.drop("YahooAnnualCashFlowStatements")
        if ( self.hasNoTable("XECurrencyTable")):
            self.drop("XECurrencyTable")
        if (self.hasNoTable("NasdaqStockSplits")):
            self.drop("NasdaqStockSplits")
        if (self.hasNoTable("NasdaqHolidays")):
            self.drop("NasdaqHolidays")
        if (self.hasNoTable("NasdaqIPOS")):
            self.drop("NasdaqIPOS")
        if (self.hasNoTable("NasdaqSymbolChanges")):
            self.drop("NasdaqSymbolChanges")
        if (self.hasNoTable("NasdaqAcquisitions")):
            self.drop("NasdaqAcquisitions")
        if (self.hasNoTable("ChildrenStocks")):
            self.drop("ChildrenStocks")
        if (self.hasNoTable("NameChange")):
            self.drop("NameChange")
        if (self.hasNoTable("NasdaqDelisted")):
            self.drop("NasdaqDelisted")
        if (self.hasNoTable("NasdaqArchiveSymbols")):
            self.drop("NasdaqArchiveSymbols")
        if (self.hasNoTable("ExchangeChange")):
            self.drop("ExchangeChange")
        if (self.hasNoTable("CommodityListings")):
            self.drop("CommodityListings")
        if (self.hasNoTable("CommoditiesPrice")):
            self.drop("CommoditiesPrice")
        if (self.hasNoTable("Metals")):
            self.drop("Metals")
        if (self.hasNoTable("MetalPrice")):
            self.drop("MetalPrice")
