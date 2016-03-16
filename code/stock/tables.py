from stock.streams.mysql import DB
from stock.streams.mysql.connections import Connections
from stock.streams.mysql.tables import CreateTables, DropTables

#NOTE if the command is in comments then it is not being used yet
# there are still issues to reconfigure the scraping to adjust
# to the data that is needed in the constraints

tables = None

def createConstraintTables():
    global tables

def nonConstraintTables():
    global tables
    tables.createFinancialErrorLog()
    tables.createLookedAtStocks()
    tables.createNasdaqIssuedSuspension()
    tables.createNasdaqSplits()
    tables.createNasdaqUpcomingIPOS()
    tables.createNasdaqPricedIPOS()
    tables.createScrapyErrorLog()
    tables.createSymbolInsert()
    tables.createConsolidatedPrices()
    #tables.createNasdaqHolidays()
    #tables.createNasdaqSymbolChanges()
    #tables.createNasdaqAcquisitions()
    #tables.createNasdaqArchiveSymbols()

def alertTables():
    global tables
    tables.createStrikePriceAlerts()

def processTables():
    global tables
    tables.createCommoditiesCompletes()
    tables.createAmericanStockCompletes()
    tables.createFinancialCompletes()

def orderedTables():
    global tables
    #these tables are ordered one after the other
    #no heavy constraints, usually just 1 or 2
    tables.createNasdaqListingReference()
    tables.createNasdaqCompanyListing() # constraint on ListingReference

    tables.createCommodityListings()
    tables.createCommoditiesPrice()

    tables.createXECurrencyListing()
    tables.createXECurrencyPricing() #constraint on Listing

    tables.createMetalPrice()

def companyListingConstraint():
    tables.createIDSymbol()
    tables.createSymbolHistory()
    tables.createGoogleFinancialCompletes()
    tables.createNasdaqFinancialCompletes()
    tables.createYahooFinancialCompletes()
    tables.createBloombergFinancialCompletes()
    tables.createNasdaqCompanyMarketInfo()
    tables.createNasdaqDelisted()
    tables.createNasdaqSummaryQuote()
    #tables.createGoogleSummaryQuote()
    #tables.createYahooSummaryQuote()
    #tables.createGoogleCompanyMarketInfo()
    #tables.createYahooCompanyMarketInfo()
    #tables.createChildrenStocks()
    #tables.createNameChange()
    #tables.createExchangeChange()
    tables.createNasdaqAnnualIncomeStatements()
    tables.createNasdaqAnnualBalanceSheets()
    tables.createNasdaqAnnualCashFlowStatements()
    tables.createNasdaqQuarterlyIncomeStatements()
    tables.createNasdaqQuarterlyBalanceSheets()
    tables.createNasdaqQuarterlyCashFlowStatements()
    tables.createBloombergAnnualIncomeStatements()
    tables.createBloombergAnnualBalanceSheets()
    tables.createBloombergAnnualCashFlowStatements()
    tables.createBloombergQuarterlyIncomeStatements()
    tables.createBloombergQuarterlyBalanceSheets()
    tables.createBloombergQuarterlyCashFlowStatements()
    tables.createYahooAnnualIncomeStatements()
    tables.createYahooAnnualBalanceSheets()
    tables.createYahooAnnualCashFlowStatements()
    tables.createYahooQuarterlyIncomeStatements()
    tables.createYahooQuarterlyBalanceSheets()
    tables.createYahooQuarterlyCashFlowStatements()
    tables.createGoogleQuarterlyIncomeStatements()
    tables.createGoogleQuarterlyBalanceSheets()
    tables.createGoogleQuarterlyCashFlowStatements()
    tables.createGoogleAnnualIncomeStatements()
    tables.createGoogleAnnualBalanceSheets()
    tables.createGoogleAnnualCashFlowStatements()
    
if __name__=="__main__":
    tables = CreateTables()
    # createConstraintTables()
    # alertTables()
    # processTables()
    # nonConstraintTables()
    # orderedTables()
    # companyListingConstraint()
    # tables.close()
    # tables.createNasdaqFinancialCompletes()
    # tables.createNasdaqAnnualBalanceSheets()
    # tables.createNasdaqAnnualIncomeStatements()
    # tables.createNasdaqAnnualCashFlowStatements()
    # tables.createNasdaqQuarterlyBalanceSheets()
    # tables.createNasdaqQuarterlyIncomeStatements()
    # tables.createNasdaqQuarterlyCashFlowStatements()
    # tables.createNasdaqFinancialCompletes()
    # tables.createGoogleFinancialCompletes()
    # tables.createYahooFinancialCompletes()
    # tables.createBloombergFinancialCompletes()
    tables.createSplitHisotry()