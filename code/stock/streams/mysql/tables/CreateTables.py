from ..DB import DB
from .Tables import Tables

class CreateTables:
    table = "CREATE TABLE "
    day = "(day DATE, PRIMARY KEY (day) )"
    symbolChar = "VARCHAR(15)"
    symbol = "symbol " + symbolChar + ","
    symbolNotNull = "symbol " + symbolChar + " NOT NULL ,"
    companyChar = "VARCHAR(100)"
    foreignKeyID = "FOREIGN KEY (id) REFERENCES IDSymbol (id)";
    foreignNonUpdateSymbol =  "FOREIGN KEY (symbol) REFERENCES NasdaqCompanyListing (symbol)"
    foreignSymbol = foreignNonUpdateSymbol + " ON UPDATE CASCADE"
    foreignReference = "FOREIGN KEY (symbol) REFERENCES NasdaqListingReference (symbol) ON UPDATE CASCADE"
    error = "fileName VARCHAR(100), lineNumber INT, TimeStamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP )"

    def __init__(self):
        self.mysql = DB(DB.Connections.STOCK)
        self.tables = Tables()

    def close(self):
        self.mysql.close()

    def hasNoTable(self, table):
        return self.tables.hasNoTable(table)

    def createIDSymbol(self):
        if (self.hasNoTable("IDSymbol")):
            self.mysql.commitExecute(str(self.table + "IDSymbol (id INT NOT NULL AUTO_INCREMENT," + self.symbolNotNull.split(',')[0] 
                + ", PRIMARY KEY (id))"));

    def createSymbolHistory(self):
        if(self.hasNoTable("SymbolHistory")):
            self.mysql.commitExecute(str(self.table + "SymbolHistory (id INT, Date DATE, " + self.symbolNotNull.split(',')[0] 
                + "," + self.foreignKeyID + ", PRIMARY KEY (id))"));

    def createLookedAtStocks(self):
        if (self.hasNoTable("LookedAtStocks")):
            self.mysql.commitExecute(str(self.table + "LookedAtStocks (" + self.symbol.split(',')[0] + ")"));

    def createStrikePriceAlerts(self):
        if(self.hasNoTable("StrikePriceAlerts")):
            self.mysql.commitExecute(self.table + "StrikePriceAlerts (type ENUM('above','below'), " + self.symbol + "quotePrice DECIMAL(12,2))");

    def createConsolidatedPrices(self):
        if (self.hasNoTable("ConsolidatedPrices")):
            self.mysql.commitExecute(self.table + "ConsolidatedPrices (" + self.symbol + "lastPrice DECIMAL(15,5), "
            + "FirstQuarterGain DECIMAL(12,5),HalfYearGain DECIMAL(12,5), OneYearGain DECIMAL(12,5), "
            + "ThreeYearGain DECIMAL(12,5), FiveYearGain DECIMAL(12,5), "
            + "TenYearGain DECIMAL(12,5), TwentyYearGain DECIMAL(12,5), ThirtyYearGain DECIMAL(12,5))")

    def createCommoditiesCompletes(self):
        if (self.hasNoTable("CommoditiesCompletes")):
            self.mysql.commitExecute(self.table + "CommoditiesCompletes " + self.day);

    def createFinancialCompletes(self):
        if (self.hasNoTable("FinancialCompletes")):
            self.mysql.commitExecute(self.table + "FinancialCompletes " + self.day);

    def createSymbolInsert(self):
        if (self.hasNoTable("SymbolInsert")):
            self.mysql.commitExecute(self.table + "SymbolInsert (" + self.symbol + "Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
                + " INDEX(Timestamp))")

    def createScrapyErrorLog(self):
        if (self.hasNoTable("ScrapyErrorLog")):
            self.mysql.commitExecute(self.table + "ScrapyErrorLog (url VARCHAR(300), error VARCHAR(300),scrape VARCHAR(100), " + self.error)

    def createFinancialErrorLog(self):
        if (self.hasNoTable("FinancialErrorLog")):
            self.mysql.commitExecute(self.table + "FinancialErrorLog (Message VARCHAR(500)," + self.symbol 
                + "TableName VARCHAR(50), Time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

    def createGoogleFinancialCompletes(self):
        if (self.hasNoTable("GoogleFinancialCompletes")):
            self.mysql.commitExecute(self.table + "GoogleFinancialCompletes (" + self.symbol  + "DayExspectingQuarter DATE, Primary Key (symbol),"
                + self.foreignNonUpdateSymbol + ")")

    def createYahooFinancialCompletes(self):
        if (self.hasNoTable("YahooFinancialCompletes")):
            self.mysql.commitExecute(self.table + "YahooFinancialCompletes (" + self.symbol  + "DayExspectingQuarter DATE, Primary Key (symbol),"
                + self.foreignNonUpdateSymbol + ")")

    def createBloombergFinancialCompletes(self):
        if (self.hasNoTable("BloombergFinancialCompletes")):
            self.mysql.commitExecute(self.table + "BloombergFinancialCompletes (" + self.symbol  + "DayExspectingQuarter DATE, Primary Key (symbol),"
                + self.foreignNonUpdateSymbol + ")")

    def createNasdaqFinancialCompletes(self):
        if (self.hasNoTable("NasdaqFinancialCompletes")):
            self.mysql.commitExecute(self.table + "NasdaqFinancialCompletes (" + self.symbol  + "DayExspectingQuarter DATE," 
                + 'Primary Key (symbol),'+ self.foreignNonUpdateSymbol + ")")

    def createCommodityListings(self):
        if (self.hasNoTable("CommodityListings")):
            self.mysql.commitExecute(self.table + "CommodityListings (CIndex VARCHAR(15), name VARCHAR(40), PRIMARY KEY (CIndex))")

    def createCommoditiesPrice(self):
        if (self.hasNoTable("CommoditiesPrice")):
            self.mysql.commitExecute(self.table + "CommoditiesPrice (Cindex VARCHAR(15), date DATE, Units VARCHAR(20), "
                + "Price DECIMAL(15,6), Contract VARCHAR(10), PRIMARY KEY (Cindex, date))")

    def createMetalPrice(self):
        if (self.hasNoTable("MetalPrice")):
            self.mysql.commitExecute(self.table + "MetalPrice (name VARCHAR(40), date DATE, Bid DECIMAL(20,2), "
                + "PRIMARY KEY (name, date))")

    def createXECurrencyListing(self):
        if (self.hasNoTable("XECurrencyListing")):
            self.mysql.commitExecute(self.table + "XECurrencyListing (code VARCHAR(5), name VARCHAR(50), PRIMARY KEY (code))")

    def createXECurrencyPricing(self):
        if ( self.hasNoTable("XECurrencyPricing")):
            self.mysql.commitExecute(self.table + "XECurrencyPricing (code VARCHAR(5), "
                +"UnitsPerUSD DECIMAL(19,12), USDperUnit DECIMAL(19,12), FOREIGN KEY (code) REFERENCES XECurrencyListing"
                +" (code) ON UPDATE CASCADE)")

    def createAmericanStockCompletes(self):
        if (self.hasNoTable("AmericanStockCompletes")):
            self.mysql.commitExecute(self.table + "AmericanStockCompletes " + self.day)

    def createNasdaqListingReference(self):
        if (self.hasNoTable("NasdaqListingReference")):
            self.mysql.commitExecute(self.table + "NasdaqListingReference(" + self.symbol + "reference char(1), Primary Key (symbol),"
                + "INDEX (reference))")

    def createNasdaqCompanyListing(self):
        if ( self.hasNoTable("NasdaqCompanyListing")):
            self.mysql.commitExecute(str(self.table) + "NasdaqCompanyListing (" + str(self.symbol) + "name " 
                + str(self.companyChar) + ", exchange VARCHAR(20), PRIMARY KEY (symbol), "
                + self.foreignReference +" )")

        #prob want to split this query into multiple tables
    def createNasdaqCompanyMarketInfo(self):
        if ( self.hasNoTable("NasdaqCompanyMarketInfo")):
            self.mysql.commitExecute(self.table + "NasdaqCompanyMarketInfo (" + self.symbol + " sector VARCHAR(70),"
                + " industry VARCHAR(70), " + self.foreignSymbol + ", PRIMARY KEY (symbol) )")


    def createNasdaqIssuedSuspension(self):
        if (self.hasNoTable("NasdaqIssuedSuspension")):
            self.mysql.commitExecute(self.table + "NasdaqIssuedSuspension (IssuerName VARCHAR(100)," + self.symbol + "reason VARCHAR(70),"
                + "status VARCHAR(20), EffectiveDate DATE, Form25Date DATE, insertDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "
                + "INDEX (symbol), INDEX (EffectiveDate), "
                + "INDEX (Form25Date), INDEX (insertDate), PRIMARY KEY (symbol, EffectiveDate))")

    def createNasdaqDelisted(self):
        if (self.hasNoTable("NasdaqDelisted")):
            self.mysql.commitExecute(self.table + "NasdaqDelisted (" + self.symbol + "date DATE, ArchivalSymbol VARCHAR(15), PRIMARY KEY (symbol),"
                + " " + self.foreignSymbol + ")")

    def createNasdaqSplits(self):
        #TODO need to make sure that we want Ex-Date to be put into the Primary Key
        if (self.hasNoTable("NasdaqSplits")):
            self.mysql.commitExecute(self.table + "NasdaqSplits (CompanyName VARCHAR(100), " + self.symbol + "Ratio DECIMAL(8,6),"
                + " Payable DATE, ExDate DATE, Announced DATE, PRIMARY KEY (symbol, ExDate))")

    def createNasdaqUpcomingIPOS(self):
        if (self.hasNoTable("NasdaqUpcomingIPOS")):
            self.mysql.commitExecute(self.table + "NasdaqUpcomingIPOS ( CompanyName VARCHAR(100), "+ self.symbol + "Market VARCHAR(30), LowPrice INT,"
                + " HighPrice INT, Shares BIGINT, OfferAmount BIGINT, ExpectedIPODate DATE, "
                + "dateInserted TIMESTAMP DEFAULT CURRENT_TIMESTAMP, INDEX (ExpectedIPODate))")

    def createNasdaqPricedIPOS(self):
        if (self.hasNoTable("NasdaqPricedIPOS")):
            self.mysql.commitExecute(self.table + "NasdaqPricedIPOS (CompanyName VARCHAR(100)," + self.symbol + "Market VARCHAR(30), Price INT,"
                + " Shares BIGINT, OfferAmount BIGINT, DatePriced DATE, INDEX (DatePriced), PRIMARY KEY (symbol))")

    def createNasdaqSummaryQuote(self):
        if (self.hasNoTable("NasdaqSummaryQuote")):
            self.mysql.commitExecute(self.table + "NasdaqSummaryQuote (" + self.symbol + "date DATE, quote DECIMAL(20,5), volume BIGINT,"
                + "low DECIMAL(20,5), high DECIMAL(20,2), outstandingShares BIGINT, PRIMARY KEY (symbol,Date), "
                + self.foreignSymbol + ")")

    def createGoogleSummaryQuote(self):
        if (self.hasNoTable("GoogleSummaryQuote")):
            self.mysql.commitExecute(self.table + "GoogleSummaryQuote (" + self.symbol + "Date DATE, quote DECIMAL(10,5), volume BIGINT, open DECIMAL(10,5),"
                + "low DECIMAL(10,5), high DECIMAL(10,2), shares BIGINT, PRIMARY KEY (symbol,Date), "
                + self.foreignSymbol + ")")

    def createYahooSummaryQuote(self):
        if (self.hasNoTable("YahooSummaryQuote")):
            self.mysql.commitExecute(self.table + "YahooSummaryQuote (" + self.symbol + "Date DATE, quote DECIMAL(10,5), volume BIGINT, open DECIMAL(10,5),"
                + "low DECIMAL(10,5), high DECIMAL(10,2), PRIMARY KEY (symbol,Date), "
                + self.foreignSymbol + ")")


    def createGoogleCompanyMarketInfo(self):
        if ( self.hasNoTable("GoogleCompanyMarketInfo")):
            self.mysql.commitExecute(self.table + "GoogleCompanyMarketInfo (" + self.symbol 
                + " GoogleSector VARCHAR(70), GoogleIndustry VARCHAR(70)," + self.foreignSymbol + ")")

    def createYahooCompanyMarketInfo(self):
        if ( self.hasNoTable("YahooCompanyMarketInfo")):
            self.mysql.commitExecute(self.table + "YahooCompanyMarketInfo (" + self.symbol 
                + "YahooSector VARCHAR(70), YahooIndustry VARCHAR(70), " + self.foreignSymbol + ")")

    def createNasdaqHolidays(self):
        if (self.hasNoTable("NasdaqHolidays")):
            self.mysql.commitExecute(self.table + "NasdaqHolidays ( Date DATE, PRIMARY KEY (Date))")


    def createNasdaqSymbolChanges(self):
        #TODO need to add the constraint on feign key
        if (self.hasNoTable("NasdaqSymbolChanges")):
            self.mysql.commitExecute(table + "NasdaqSymbolChanges ( PreviousSymbol " + self.symbolChar + " NOT NULL, NewSymbol " + self.symbolChar
                + ", Date DATE, INDEX (Date), PRIMARY KEY (NewSymbol))")

    def createNasdaqAcquisitions(self):
        #TODO need to get foreign Key  not sure though
        if (self.hasNoTable("NasdaqAcquisitions")):
            self.mysql.commitExecute(table + "NasdaqAcquisitions ( Buyer VARCHAR(15), Bought VARCHAR(15), Date DATE,"
                + "PricePerShare INT, OutstandingShares BIGINT, ArchivalSymbol VARCHAR(15), INDEX (Date), INDEX (Buyer))")

    def createChildrenStocks(self):
        #TODO  might need to consider the outstanding shares of all issues
        if (self.hasNoTable("ChildrenStocks")):
            self.mysql.commitExecute(table + "ChildrenStocks (PrimaryStock VARCHAR(15), SecondaryStock VARCHAR(15), "
                + "PRIMARY KEY (PrimaryStock), UNIQUE (SecondaryStock), FOREIGN KEY (PrimaryStock) REFERENCES "
                + "NasdaqCompanyListing (symbol) ON UPDATE CASCADE, FOREIGN KEY (SecondaryStock) REFERENCES "
                + "NasdaqCompanyListing (symbol) ON UPDATE CASCADE)")

    def createNameChange(self):
        #TODO FOREIGN key on the archival stuff  and Primary Key on archivalSymbol
        if (self.hasNoTable("NameChange")):
            self.mysql.commitExecute(table + "NameChange ("+ self.symbol +"date DATE, PreviousName VARCHAR(), NewName "
                + self.companyChar + " PRIMARY KEY (symbol), " + self.foreignSymbol + " )")

    def createNasdaqArchiveSymbols(self):
        #TODO
        if (self.hasNoTable("NasdaqArchiveSymbols")):
            self.mysql.commitExecute(table + "NasdaqArchiveSymbols ( PreviousSymbol VARCHAR(15), ArchivalSymbol VARCHAR(15))")

    def createExchangeChange(self):
        if (self.hasNoTable("ExchangeChange")):
            self.mysql.commitExecute(table + "ExchangeChange (" + self.symbol + "date DATE, PreviousExchange VARCHAR(self)"
                + ", NewExchange VARCHAR(self), " + self.foreignSymbol +", PRIMARY KEY (symbol))")

    def createYahooAnnualIncomeStatements(self):
        if (self.hasNoTable("YahooAnnualIncomeStatements")):
            query = ("CREATE TABLE YahooAnnualIncomeStatements "
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "TotalRevenue BIGINT, " 
                + "GrossProfit BIGINT, "
                + "OperatingIncomeorLoss BIGINT, "
                + "NetIncome BIGINT, "
                + "NetIncomeApplicableToCommonShares BIGINT, "
                + "CostofRevenue  BIGINT, "
                + "ResearchDevelopment  BIGINT, "
                + "SellingGeneralandAdministrative  BIGINT, "
                + "NonRecurring  BIGINT, "
                + "Others  BIGINT, "
                + "TotalOtherIncomeExpensesNet BIGINT, "
                + "EarningsBeforeInterestAndTaxes  BIGINT, "
                + "InterestExpense  BIGINT, "
                + "IncomeBeforeTax  BIGINT, "
                + "IncomeTaxExpense  BIGINT, "
                + "MinorityInterest  BIGINT, "
                + "NetIncomeFromContinuingOps  BIGINT, "
                + "DiscontinuedOperations  BIGINT, "
                + "ExtraordinaryItems  BIGINT, "
                + "EffectOfAccountingChanges  BIGINT, "
                + "OtherItems  BIGINT, "
                + "PreferredStockAndOtherAdjustments  BIGINT, "
                + "TotalOperatingExpenses BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createYahooAnnualBalanceSheets(self):
        if (self.hasNoTable("YahooAnnualBalanceSheets")):
            query = ("CREATE TABLE YahooAnnualBalanceSheets"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "CashAndCashEquivalents BIGINT, "
                + "ShortTermInvestments BIGINT, "
                + "NetReceivables BIGINT, "
                + "Inventory BIGINT, "
                + "OtherCurrentAssets BIGINT, "
                + "LongTermInvestments BIGINT, "
                + "PropertyPlantandEquipment BIGINT, "
                + "Goodwill BIGINT, "
                + "IntangibleAssets BIGINT, "
                + "AccumulatedAmortization BIGINT, "
                + "OtherAssets BIGINT, "
                + "DeferredLongTermAssetCharges BIGINT, "
                + "AccountsPayable BIGINT, "
                + "ShortCurrentLongTermDebt BIGINT, "
                + "OtherCurrentLiabilities BIGINT, "
                + "LongTermDebt BIGINT, "
                + "OtherLiabilities BIGINT, "
                + "DeferredLongTermLiabilityCharges BIGINT, "
                + "MinorityInterest BIGINT, "
                + "NegativeGoodwill BIGINT, "
                + "MiscStocksOptionsWarrants BIGINT, "
                + "RedeemablePreferredStock BIGINT, "
                + "PreferredStock BIGINT, "
                + "CommonStock BIGINT, "
                + "RetainedEarnings BIGINT, "
                + "TreasuryStock BIGINT, "
                + "CapitalSurplus BIGINT, "
                + "OtherStockholderEquity BIGINT, "
                + "TotalCurrentAssets BIGINT, "
                + "TotalAssets BIGINT, "
                + "TotalCurrentLiabilities BIGINT, "
                + "TotalLiabilities  BIGINT, "
                + "TotalStockholderEquity BIGINT, "
                + "NetTangibleAssets BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createYahooAnnualCashFlowStatements(self):
        if (self.hasNoTable("YahooAnnualCashFlowStatements")):
            query = ("CREATE TABLE YahooAnnualCashFlowStatements"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "Depreciation BIGINT, "
                + "AdjustmentsToNetIncome BIGINT, "
                + "ChangesInAccountsReceivables  BIGINT, "
                + "ChangesInLiabilities  BIGINT, "
                + "ChangesInInventories  BIGINT, "
                + "ChangesInOtherOperatingActivities  BIGINT, "
                + "CapitalExpenditures  BIGINT, "
                + "Investments BIGINT, "
                + "OtherCashflowsfromInvestingActivities BIGINT, "
                + "DividendsPaid BIGINT, "
                + "SalePurchaseofStock BIGINT, "
                + "NetBorrowings BIGINT, "
                + "OtherCashFlowsfromFinancingActivities BIGINT, "
                + "EffectOfExchangeRateChanges BIGINT, "
                + "NetIncome BIGINT, "
                + "TotalCashFlowFromOperatingActivities BIGINT, "
                + "TotalCashFlowsFromInvestingActivities BIGINT, "
                + "TotalCashFlowsFromFinancingActivities BIGINT, "
                + "ChangeInCashandCashEquivalents BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createYahooQuarterlyIncomeStatements(self):
        if (self.hasNoTable("YahooQuarterlyIncomeStatements")):
            query = ("CREATE TABLE YahooQuarterlyIncomeStatements "
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "TotalRevenue BIGINT, " 
                + "GrossProfit BIGINT, "
                + "OperatingIncomeorLoss BIGINT, "
                + "NetIncome BIGINT, "
                + "NetIncomeApplicableToCommonShares BIGINT, "
                + "CostofRevenue  BIGINT, "
                + "ResearchDevelopment  BIGINT, "
                + "SellingGeneralandAdministrative  BIGINT, "
                + "NonRecurring  BIGINT, "
                + "Others  BIGINT, "
                + "TotalOtherIncomeExpensesNet BIGINT, "
                + "EarningsBeforeInterestAndTaxes  BIGINT, "
                + "InterestExpense  BIGINT, "
                + "IncomeBeforeTax  BIGINT, "
                + "IncomeTaxExpense  BIGINT, "
                + "MinorityInterest  BIGINT, "
                + "NetIncomeFromContinuingOps  BIGINT, "
                + "DiscontinuedOperations  BIGINT, "
                + "ExtraordinaryItems  BIGINT, "
                + "EffectOfAccountingChanges  BIGINT, "
                + "OtherItems  BIGINT, "
                + "PreferredStockAndOtherAdjustments  BIGINT, "
                + "TotalOperatingExpenses BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createYahooQuarterlyBalanceSheets(self):
        if (self.hasNoTable("YahooQuarterlyBalanceSheets")):
            query = ("CREATE TABLE YahooQuarterlyBalanceSheets"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "CashAndCashEquivalents BIGINT, "
                + "ShortTermInvestments BIGINT, "
                + "NetReceivables BIGINT, "
                + "Inventory BIGINT, "
                + "OtherCurrentAssets BIGINT, "
                + "LongTermInvestments BIGINT, "
                + "PropertyPlantandEquipment BIGINT, "
                + "Goodwill BIGINT, "
                + "IntangibleAssets BIGINT, "
                + "AccumulatedAmortization BIGINT, "
                + "OtherAssets BIGINT, "
                + "DeferredLongTermAssetCharges BIGINT, "
                + "AccountsPayable BIGINT, "
                + "ShortCurrentLongTermDebt BIGINT, "
                + "OtherCurrentLiabilities BIGINT, "
                + "LongTermDebt BIGINT, "
                + "OtherLiabilities BIGINT, "
                + "DeferredLongTermLiabilityCharges BIGINT, "
                + "MinorityInterest BIGINT, "
                + "NegativeGoodwill BIGINT, "
                + "MiscStocksOptionsWarrants BIGINT, "
                + "RedeemablePreferredStock BIGINT, "
                + "PreferredStock BIGINT, "
                + "CommonStock BIGINT, "
                + "RetainedEarnings BIGINT, "
                + "TreasuryStock BIGINT, "
                + "CapitalSurplus BIGINT, "
                + "OtherStockholderEquity BIGINT, "
                + "TotalCurrentAssets BIGINT, "
                + "TotalAssets BIGINT, "
                + "TotalCurrentLiabilities BIGINT, "
                + "TotalLiabilities  BIGINT, "
                + "TotalStockholderEquity BIGINT, "
                + "NetTangibleAssets BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createYahooQuarterlyCashFlowStatements(self):
        if (self.hasNoTable("YahooQuarterlyCashFlowStatements")):
            query = ("CREATE TABLE YahooQuarterlyCashFlowStatements"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "Depreciation BIGINT, "
                + "AdjustmentsToNetIncome BIGINT, "
                + "ChangesInAccountsReceivables  BIGINT, "
                + "ChangesInLiabilities  BIGINT, "
                + "ChangesInInventories  BIGINT, "
                + "ChangesInOtherOperatingActivities  BIGINT, "
                + "CapitalExpenditures  BIGINT, "
                + "Investments BIGINT, "
                + "OtherCashflowsfromInvestingActivities BIGINT, "
                + "DividendsPaid BIGINT, "
                + "SalePurchaseofStock BIGINT, "
                + "NetBorrowings BIGINT, "
                + "OtherCashFlowsfromFinancingActivities BIGINT, "
                + "EffectOfExchangeRateChanges BIGINT, "
                + "NetIncome BIGINT, "
                + "TotalCashFlowFromOperatingActivities BIGINT, "
                + "TotalCashFlowsFromInvestingActivities BIGINT, "
                + "TotalCashFlowsFromFinancingActivities BIGINT, "
                + "ChangeInCashandCashEquivalents BIGINT, "
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergAnnualIncomeStatements(self):
        if (self.hasNoTable("BloombergAnnualIncomeStatements")):
            query = ("CREATE TABLE BloombergAnnualIncomeStatements "
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "Revenues DECIMAL(04,2), "
                + "OtherRevenues DECIMAL(14,2), "
                + "CostofGoodsSold DECIMAL(14,2), "
                + "SellingGeneralAdminExpensesTotal DECIMAL(14,2), "
                + "DepreciationAmortizationTotal DECIMAL(14,2), "
                + "OtherOperatingExpenses DECIMAL(14,2), "
                + "InterestExpense DECIMAL(14,2), "
                + "InterestandInvestmentIncome DECIMAL(14,2), "
                + "CurrencyExchangeGainsLoss DECIMAL(14,2), "
                + "OtherNonOperatingIncomeExpenses DECIMAL(14,2), "
                + "MergerRestructuringCharges DECIMAL(14,2), "
                + "GainLossonSaleofInvestments DECIMAL(14,2), "
                + "OtherUnusualItemsTotal DECIMAL(14,2), "
                + "OtherUnusualItems DECIMAL(14,2), "
                + "IncomeTaxExpense DECIMAL(14,2), "
                + "EarningsfromContinuingOperations DECIMAL(14,2), "
                + "TOTALREVENUES DECIMAL(14,2), "
                + "GROSSPROFIT DECIMAL(14,2), "
                + "OTHEROPERATINGEXPENSESTOTAL DECIMAL(14,2), "
                + "OPERATINGINCOME DECIMAL(14,2), "
                + "NETINTERESTEXPENSE DECIMAL(14,2), "
                + "EBTEXCLUDINGUNUSUALITEMS DECIMAL(14,2), "
                + "EBTINCLUDINGUNUSUALITEMS DECIMAL(14,2), "
                + "NETINCOME DECIMAL(14,2), "
                + "NETINCOMETOCOMMONINCLUDINGEXTRAITEMS DECIMAL(14,2), "
                + "NETINCOMETOCOMMONEXCLUDINGEXTRAITEMS DECIMAL(14,2), "
                + "EARNINGSFROMDISCOUNTINUEDOPERATIONS DECIMAL(14,2), "
                + "LegalSettlements DECIMAL(14,2),"
                + "gainlossonsaleofassets DECIMAL(14,2),"
                + "impairmentofgoodwill DECIMAL(14,2),"
                + "incomelossonequityinvestments DECIMAL(14,2),"
                + "inprocessrdexpenses DECIMAL(14,2),"
                + "insurancesettlements DECIMAL(14,2),"
                + "minorityinterestinearnings DECIMAL(14,2),"
                + "rdexpenses DECIMAL(14,2),"
                + "extraordinaryitemaccountingchange DECIMAL(14,2),"
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergAnnualBalanceSheets(self):
        if (self.hasNoTable("BloombergAnnualBalanceSheets")):
            query = ("CREATE TABLE BloombergAnnualBalanceSheets"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "CashandEquivalents DECIMAL(14,2), "
                + "ShortTermInvestments DECIMAL(14,2), "
                + "AccountsReceivable DECIMAL(14,2), "
                + "Inventory DECIMAL(14,2), "
                + "PrepaidExpenses DECIMAL(14,2), "
                + "RestrictedCash DECIMAL(14,2), "
                + "GrossPropertyPlantandEquipment DECIMAL(14,2), "
                + "AccumulatedDepreciation DECIMAL(14,2), "
                + "Goodwill DECIMAL(14,2), "
                + "OtherIntangibles DECIMAL(14,2), "
                + "OtherLongTermAssets DECIMAL(14,2), "
                + "AccountsPayable DECIMAL(14,2), "
                + "AccruedExpenses DECIMAL(14,2), "
                + "CurrentPortionofLongTermDebtCapitalLease DECIMAL(14,2), "
                + "UnearnedRevenueCurrent DECIMAL(14,2), "
                + "LongTermDebt DECIMAL(14,2), "
                + "UnearnedRevenueNonCurrent DECIMAL(14,2), "
                + "PensionOtherPostRetirementBenefits DECIMAL(14,2), "
                + "OtherNonCurrentLiabilities DECIMAL(14,2), "
                + "CommonStock DECIMAL(14,2), "
                + "AdditionalPaidinCapital DECIMAL(14,2), "
                + "RetainedEarnings DECIMAL(14,2), "
                + "ComprehensiveIncomeandOther DECIMAL(14,2), "
                + "TOTALCASHANDSHORTTERMINVESTMENTS  DECIMAL(14,2), "
                + "TOTALRECEIVABLES  DECIMAL(14,2), "
                + "TOTALCURRENTASSETS  DECIMAL(14,2), "
                + "NETPROPERTYPLANTANDEQUIPMENT  DECIMAL(14,2), "
                + "TOTALCURRENTLIABILITIES  DECIMAL(14,2), "
                + "TOTALLIABILITIES  DECIMAL(14,2), "
                + "TOTALCOMMONEQUITY  DECIMAL(14,2), "
                + "TOTALEQUITY  DECIMAL(14,2), "
                + "TOTALASSETS DECIMAL(14,2), "
                + "TOTALLIABILITIESANDEQUITY DECIMAL(14,2), "
                + "capitalleases decimal(14,2),"
                + "currentincometaxespayable decimal(14,2),"
                + "deferredchargeslongterm decimal(14,2),"
                + "deferredtaxassetslongterm decimal(14,2),"
                + "loansheldforsale decimal(14,2),"
                + "loansreceivablelongterm decimal(14,2),"
                + "longterminvestments decimal(14,2),"
                + "minorityinterest decimal(14,2),"
                + "othercurrentassets decimal(14,2),"
                + "othercurrentliabilitiestotal decimal(14,2),"
                + "otherreceivables decimal(14,2),"
                + "preferredstockconvertible decimal(14,2),"
                + "shorttermborrowings decimal(14,2),"
                + "treasurystock decimal(14,2),"


                + "accountsreceivablelongterm DECIMAL(14,2),"
                + "currentportionofcapitalleaseobligations DECIMAL(14,2),"
                + "deferredtaxassetscurrent DECIMAL(14,2),"
                + "deferredtaxliabilitynoncurrent DECIMAL(14,2),"
                + "financedivisiondebtnoncurrent DECIMAL(14,2),"
                + "financedivisionloansandleasescurrent DECIMAL(14,2),"
                + "financedivisionloansandleaseslongterm DECIMAL(14,2),"
                + "financedivisionothercurrentassets DECIMAL(14,2),"
                + "notesreceivable DECIMAL(14,2),"
                + "totalpreferredequity DECIMAL(14,2),"
                + "tradingassetsecurities DECIMAL(14,2),"

                + "financedivisionotherlongtermassets DECIMAL(14,2),"
                + "financedivisionothernoncurrentliabilities DECIMAL(14,2),"
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergAnnualCashFlowStatements(self):
        if (self.hasNoTable("BloombergAnnualCashFlowStatements")):
            query = ("CREATE TABLE BloombergAnnualCashFlowStatements"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "DepreciationAmortization DECIMAL(14,2), "
                + "AmortizationofGoodwillandIntangibleAssets DECIMAL(14,2), "
                + "OtherOperatingActivities DECIMAL(14,2), "
                + "ChangeinAccountsReceivable DECIMAL(14,2), "
                + "ChangeinAccountsPayable DECIMAL(14,2), "
                + "ChangeinUnearnedRevenues DECIMAL(14,2), "
                + "ChangeinOtherWorkingCapital DECIMAL(14,2), "
                + "CapitalExpenditure DECIMAL(14,2), "
                + "SaleofPropertyPlantandEquipment DECIMAL(14,2), "
                + "SalePurchaseofIntangibleAssets DECIMAL(14,2), "
                + "InvestmentsinMarketableEquitySecurities DECIMAL(14,2), "
                + "LongTermDebtIssued DECIMAL(14,2), "
                + "LongTermDebtRepaid DECIMAL(14,2), "
                + "IssuanceofCommonStock DECIMAL(14,2), "
                + "RepurchaseofCommonStock DECIMAL(14,2), "
                + "CommonDividendsPaid DECIMAL(14,2), "
                + "CommonandorPreferredDividendsPaid DECIMAL(14,2), "
                + "OtherFinancingActivities DECIMAL(14,2), "
                + "NETINCOME  DECIMAL(14,2), "
                + "DEPRECIATIONAMORTIZATIONTOTAL  DECIMAL(14,2), "
                + "CASHFROMOPERATIONS  DECIMAL(14,2), "
                + "CASHFROMINVESTING  DECIMAL(14,2), "
                + "TOTALDEBTISSUED  DECIMAL(14,2), "
                + "TOTALDEBTREPAID  DECIMAL(14,2), "
                + "TOTALDIVIDENDPAID  DECIMAL(14,2), "
                + "CASHFROMFINANCING  DECIMAL(14,2), "
                + "NETCHANGEINCASH DECIMAL(14,2), "
                + "amortizationofdeferredcharges DECIMAL(14,2),"
                + "assetwritedownrestructuringcosts DECIMAL(14,2),"
                + "cashacquisitions DECIMAL(14,2),"
                + "changeindeferredtaxes DECIMAL(14,2),"
                + "changeinincometaxes DECIMAL(14,2),"
                + "divestitures DECIMAL(14,2),"
                + "foreignexchangerateadjustments DECIMAL(14,2),"
                + "gainlossfromsaleofasset DECIMAL(14,2),"
                + "gainlossonsaleofinvestment DECIMAL(14,2),"
                + "impairmentofoilgasmineralproperties DECIMAL(14,2),"
                + "incomelossonequityinvestments DECIMAL(14,2),"
                + "minorityinterest DECIMAL(14,2),"
                + "netcashfromdiscontinuedoperations DECIMAL(14,2),"
                + "netincdecinloansoriginatedsold DECIMAL(14,2),"
                + "preferreddividendspaid DECIMAL(14,2),"
                + "provisionforcreditlosses DECIMAL(14,2),"
                + "provisionwriteoffofbaddebts DECIMAL(14,2),"
                + "shorttermdebtissued DECIMAL(14,2),"
                + "shorttermdebtrepaid DECIMAL(14,2),"
                + "specialdividendpaid DECIMAL(14,2),"
                + "taxbenefitfromstockoptions DECIMAL(14,2),"


                + "changeininventories DECIMAL(14,2),"
                + "changeintradingassetsecurities DECIMAL(14,2),"
                + "miscellaneouscashflowadjustments DECIMAL(14,2),"
                + "netincreasedecreaseinloansoriginatedsold DECIMAL(14,2),"
                + "salepurchaseofrealestateproperties DECIMAL(14,2),"

                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergQuarterlyBalanceSheets(self):
        if (self.hasNoTable("BloombergQuarterlyBalanceSheets")):
            query = ("CREATE TABLE BloombergQuarterlyBalanceSheets"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "CashandEquivalents DECIMAL(14,2), "
                + "ShortTermInvestments DECIMAL(14,2), "
                + "AccountsReceivable DECIMAL(14,2), "
                + "Inventory DECIMAL(14,2), "
                + "PrepaidExpenses DECIMAL(14,2), "
                + "RestrictedCash DECIMAL(14,2), "
                + "GrossPropertyPlantandEquipment DECIMAL(14,2), "
                + "AccumulatedDepreciation DECIMAL(14,2), "
                + "Goodwill DECIMAL(14,2), "
                + "OtherIntangibles DECIMAL(14,2), "
                + "OtherLongTermAssets DECIMAL(14,2), "
                + "AccountsPayable DECIMAL(14,2), "
                + "AccruedExpenses DECIMAL(14,2), "
                + "CurrentPortionofLongTermDebtCapitalLease DECIMAL(14,2), "
                + "UnearnedRevenueCurrent DECIMAL(14,2), "
                + "LongTermDebt DECIMAL(14,2), "
                + "UnearnedRevenueNonCurrent DECIMAL(14,2), "
                + "PensionOtherPostRetirementBenefits DECIMAL(14,2), "
                + "OtherNonCurrentLiabilities DECIMAL(14,2), "
                + "CommonStock DECIMAL(14,2), "
                + "AdditionalPaidinCapital DECIMAL(14,2), "
                + "RetainedEarnings DECIMAL(14,2), "
                + "ComprehensiveIncomeandOther DECIMAL(14,2), "
                + "TOTALCASHANDSHORTTERMINVESTMENTS  DECIMAL(14,2), "
                + "TOTALRECEIVABLES  DECIMAL(14,2), "
                + "TOTALCURRENTASSETS  DECIMAL(14,2), "
                + "NETPROPERTYPLANTANDEQUIPMENT  DECIMAL(14,2), "
                + "TOTALCURRENTLIABILITIES  DECIMAL(14,2), "
                + "TOTALLIABILITIES  DECIMAL(14,2), "
                + "TOTALCOMMONEQUITY  DECIMAL(14,2), "
                + "TOTALEQUITY  DECIMAL(14,2), "
                + "TOTALASSETS DECIMAL(14,2), "
                + "TOTALLIABILITIESANDEQUITY DECIMAL(14,2), "
                + "capitalleases decimal(14,2),"
                + "currentincometaxespayable decimal(14,2),"
                + "deferredchargeslongterm decimal(14,2),"
                + "deferredtaxassetslongterm decimal(14,2),"
                + "loansheldforsale decimal(14,2),"
                + "loansreceivablelongterm decimal(14,2),"
                + "longterminvestments decimal(14,2),"
                + "minorityinterest decimal(14,2),"
                + "othercurrentassets decimal(14,2),"
                + "othercurrentliabilitiestotal decimal(14,2),"
                + "otherreceivables decimal(14,2),"
                + "preferredstockconvertible decimal(14,2),"
                + "shorttermborrowings decimal(14,2),"
                + "treasurystock decimal(14,2),"


                + "accountsreceivablelongterm DECIMAL(14,2),"
                + "currentportionofcapitalleaseobligations DECIMAL(14,2),"
                + "deferredtaxassetscurrent DECIMAL(14,2),"
                + "deferredtaxliabilitynoncurrent DECIMAL(14,2),"
                + "financedivisiondebtnoncurrent DECIMAL(14,2),"
                + "financedivisionloansandleasescurrent DECIMAL(14,2),"
                + "financedivisionloansandleaseslongterm DECIMAL(14,2),"
                + "financedivisionothercurrentassets DECIMAL(14,2),"
                + "notesreceivable DECIMAL(14,2),"
                + "totalpreferredequity DECIMAL(14,2),"
                + "tradingassetsecurities DECIMAL(14,2),"
                + "financedivisionotherlongtermassets DECIMAL(14,2),"

                + "financedivisionothernoncurrentliabilities DECIMAL(14,2),"
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergQuarterlyCashFlowStatements(self):
        if (self.hasNoTable("BloombergQuarterlyCashFlowStatements")):
            query = ("CREATE TABLE BloombergQuarterlyCashFlowStatements"
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "DepreciationAmortization DECIMAL(14,2), "
                + "AmortizationofGoodwillandIntangibleAssets DECIMAL(14,2), "
                + "OtherOperatingActivities DECIMAL(14,2), "
                + "ChangeinAccountsReceivable DECIMAL(14,2), "
                + "ChangeinAccountsPayable DECIMAL(14,2), "
                + "ChangeinUnearnedRevenues DECIMAL(14,2), "
                + "ChangeinOtherWorkingCapital DECIMAL(14,2), "
                + "CapitalExpenditure DECIMAL(14,2), "
                + "SaleofPropertyPlantandEquipment DECIMAL(14,2), "
                + "SalePurchaseofIntangibleAssets DECIMAL(14,2), "
                + "InvestmentsinMarketableEquitySecurities DECIMAL(14,2), "
                + "LongTermDebtIssued DECIMAL(14,2), "
                + "LongTermDebtRepaid DECIMAL(14,2), "
                + "IssuanceofCommonStock DECIMAL(14,2), "
                + "RepurchaseofCommonStock DECIMAL(14,2), "
                + "CommonDividendsPaid DECIMAL(14,2), "
                + "CommonandorPreferredDividendsPaid DECIMAL(14,2), "
                + "OtherFinancingActivities DECIMAL(14,2), "
                + "NETINCOME  DECIMAL(14,2), "
                + "DEPRECIATIONAMORTIZATIONTOTAL  DECIMAL(14,2), "
                + "CASHFROMOPERATIONS  DECIMAL(14,2), "
                + "CASHFROMINVESTING  DECIMAL(14,2), "
                + "TOTALDEBTISSUED  DECIMAL(14,2), "
                + "TOTALDEBTREPAID  DECIMAL(14,2), "
                + "TOTALDIVIDENDPAID  DECIMAL(14,2), "
                + "CASHFROMFINANCING  DECIMAL(14,2), "
                + "NETCHANGEINCASH DECIMAL(14,2), "
                + "amortizationofdeferredcharges DECIMAL(14,2),"
                + "assetwritedownrestructuringcosts DECIMAL(14,2),"
                + "cashacquisitions DECIMAL(14,2),"
                + "changeindeferredtaxes DECIMAL(14,2),"
                + "changeinincometaxes DECIMAL(14,2),"
                + "divestitures DECIMAL(14,2),"
                + "foreignexchangerateadjustments DECIMAL(14,2),"
                + "gainlossfromsaleofasset DECIMAL(14,2),"
                + "gainlossonsaleofinvestment DECIMAL(14,2),"
                + "impairmentofoilgasmineralproperties DECIMAL(14,2),"
                + "incomelossonequityinvestments DECIMAL(14,2),"
                + "minorityinterest DECIMAL(14,2),"
                + "netcashfromdiscontinuedoperations DECIMAL(14,2),"
                + "netincdecinloansoriginatedsold DECIMAL(14,2),"
                + "preferreddividendspaid DECIMAL(14,2),"
                + "provisionforcreditlosses DECIMAL(14,2),"
                + "provisionwriteoffofbaddebts DECIMAL(14,2),"
                + "shorttermdebtissued DECIMAL(14,2),"
                + "shorttermdebtrepaid DECIMAL(14,2),"
                + "specialdividendpaid DECIMAL(14,2),"
                + "taxbenefitfromstockoptions DECIMAL(14,2),"

                + "changeininventories DECIMAL(14,2),"
                + "changeintradingassetsecurities DECIMAL(14,2),"
                + "miscellaneouscashflowadjustments DECIMAL(14,2),"
                + "netincreasedecreaseinloansoriginatedsold DECIMAL(14,2),"
                + "salepurchaseofrealestateproperties DECIMAL(14,2),"
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createBloombergQuarterlyIncomeStatements(self):
        if (self.hasNoTable("BloombergQuarterlyIncomeStatements")):
            query = ("CREATE TABLE BloombergQuarterlyIncomeStatements "
                + "(" + self.symbol
                + "date DATE, "
                + "currency VARCHAR(100),"
                + "Revenues DECIMAL(14,2), "
                + "OtherRevenues DECIMAL(14,2), "
                + "CostofGoodsSold DECIMAL(14,2), "
                + "SellingGeneralAdminExpensesTotal DECIMAL(14,2), "
                + "DepreciationAmortizationTotal DECIMAL(14,2), "
                + "OtherOperatingExpenses DECIMAL(14,2), "
                + "InterestExpense DECIMAL(14,2), "
                + "InterestandInvestmentIncome DECIMAL(14,2), "
                + "CurrencyExchangeGainsLoss DECIMAL(14,2), "
                + "OtherNonOperatingIncomeExpenses DECIMAL(14,2), "
                + "MergerRestructuringCharges DECIMAL(14,2), "
                + "GainLossonSaleofInvestments DECIMAL(14,2), "
                + "OtherUnusualItemsTotal DECIMAL(14,2), "
                + "OtherUnusualItems DECIMAL(14,2), "
                + "IncomeTaxExpense DECIMAL(14,2), "
                + "EarningsfromContinuingOperations DECIMAL(14,2), "
                + "TOTALREVENUES DECIMAL(14,2), "
                + "GROSSPROFIT DECIMAL(14,2), "
                + "OTHEROPERATINGEXPENSESTOTAL DECIMAL(14,2), "
                + "OPERATINGINCOME DECIMAL(14,2), "
                + "NETINTERESTEXPENSE DECIMAL(14,2), "
                + "EBTEXCLUDINGUNUSUALITEMS DECIMAL(14,2), "
                + "EBTINCLUDINGUNUSUALITEMS DECIMAL(14,2), "
                + "NETINCOME DECIMAL(14,2), "
                + "NETINCOMETOCOMMONINCLUDINGEXTRAITEMS DECIMAL(14,2), "
                + "NETINCOMETOCOMMONEXCLUDINGEXTRAITEMS DECIMAL(14,2), "
                + "EARNINGSFROMDISCOUNTINUEDOPERATIONS DECIMAL(14,2), "
                + "LegalSettlements DECIMAL(14,2), "
                + "gainlossonsaleofassets DECIMAL(14,2),"
                + "impairmentofgoodwill DECIMAL(14,2),"
                + "incomelossonequityinvestments DECIMAL(14,2),"
                + "inprocessrdexpenses DECIMAL(14,2),"
                + "insurancesettlements DECIMAL(14,2),"
                + "minorityinterestinearnings DECIMAL(14,2),"
                + "rdexpenses DECIMAL(14,2),"
                + "extraordinaryitemaccountingchange DECIMAL(14,2),"
                + "INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)


    def createNasdaqAnnualIncomeStatements(self):
        if ( self.hasNoTable("NasdaqAnnualIncomeStatements")):
            query = ("CREATE TABLE NasdaqAnnualIncomeStatements "
                + "(" + self.symbol
                + "date DATE"
                + ",currency VARCHAR(100)"
                + ",totalRevenue BIGINT SIGNED"
                + ",costOfRevenue BIGINT SIGNED"
                + ",grossProfit BIGINT SIGNED"
                + ",operatingExpenses BIGINT SIGNED"
                + ",researchAndDevelopment BIGINT SIGNED"
                + ",salesGeneralandAdmin BIGINT SIGNED"
                + ",nonRecurringItems BIGINT SIGNED"
                + ",otherOperatingItems BIGINT SIGNED"
                + ",operatingIncome BIGINT SIGNED"
                + ",addlIncomeExpenseItems BIGINT SIGNED"
                + ",earningsBeforeInterestAndTax BIGINT SIGNED"
                + ",interestExpense BIGINT SIGNED"
                + ",earningsBeforeTax BIGINT SIGNED"
                + ",incomeTax BIGINT SIGNED"
                + ",minorityInterest BIGINT SIGNED"
                + ",equityEarningsLossUnconsolidatedSubsidiary BIGINT SIGNED"
                + ",netIncomeContOperations BIGINT SIGNED"
                + ",netIncome BIGINT SIGNED"
                + ",netIncomeApplicableToCommonShareHolders BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createNasdaqAnnualCashFlowStatements(self):
        if (self.hasNoTable("NasdaqAnnualCashFlowStatements")):
            query = ("CREATE TABLE NasdaqAnnualCashFlowStatements "
                + "(" + self.symbol
                + "date DATE"
                + ",currency VARCHAR(100)"
                + ",NetIncome BIGINT SIGNED"
                + ",CashFlowsOperatingrtivities BIGINT SIGNED"
                + ",Depreciation BIGINT SIGNED"
                + ",NetIncomeAdjustments BIGINT SIGNED"
                + ",ChangesinOperatingActivities BIGINT SIGNED"
                + ",AccountsReceivable BIGINT SIGNED"
                + ",ChangesinInventories BIGINT SIGNED"
                + ",OtherOperatingActivities BIGINT SIGNED"
                + ",Liabilities BIGINT SIGNED"
                + ",NetCashFlowOperating BIGINT SIGNED"
                + ",CashFlowsInvestingActivities BIGINT SIGNED"
                + ",CapitalExpenditures BIGINT SIGNED"
                + ",Investments BIGINT SIGNED"
                + ",OtherInvestingActivities BIGINT SIGNED"
                + ",NetCashFlowsInvesting BIGINT SIGNED"
                + ",CashFlowsFinancingActivities BIGINT SIGNED"
                + ",SaleandPurchaseofStock BIGINT SIGNED"
                + ",NetBorrowings BIGINT SIGNED"
                + ",OtherFinancingActivities BIGINT SIGNED"
                + ",NetCashFlowsFinancing BIGINT SIGNED"
                + ",EffectofExchangeRate BIGINT SIGNED"
                + ",NetCashFlow BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createNasdaqAnnualBalanceSheets(self):
        if (self.hasNoTable("NasdaqAnnualBalanceSheets")):
            query = ("CREATE TABLE NasdaqAnnualBalanceSheets "
                + "(" + self.symbol
                + "date Date"
                + ",currency VARCHAR(100)"
                + ",CurrentAssets BIGINT SIGNED"
                + ",CashandCashEquivalents BIGINT SIGNED"
                + ",ShortTermInvestments BIGINT SIGNED"
                + ",NetReceivables BIGINT SIGNED"
                + ",Inventory BIGINT SIGNED"
                + ",OtherCurrentAssets BIGINT SIGNED"
                + ",TotalCurrentAssets BIGINT SIGNED"
                + ",LongTermAssets BIGINT SIGNED"
                + ",LongTermInvestments BIGINT SIGNED"
                + ",FixedAssets BIGINT SIGNED"
                + ",Goodwill BIGINT SIGNED"
                + ",IntangibleAssets BIGINT SIGNED"
                + ",OtherAssets BIGINT SIGNED"
                + ",DeferredAssetCharges BIGINT SIGNED"
                + ",TotalAssets BIGINT SIGNED"
                + ",CurrentLiabilities BIGINT SIGNED"
                + ",AccountsPayable BIGINT SIGNED"
                + ",ShortTermDebtCurrentPortionofLongTermDebt BIGINT SIGNED"
                + ",OtherCurrentLiabilities BIGINT SIGNED"
                + ",TotalCurrentLiabilities BIGINT SIGNED"
                + ",LongTermDebt BIGINT SIGNED"
                + ",OtherLiabilities BIGINT SIGNED"
                + ",DeferredLiabilityCharges BIGINT SIGNED"
                + ",MiscStocks BIGINT SIGNED"
                + ",MinorityInterest BIGINT SIGNED"
                + ",TotalLiabilities BIGINT SIGNED"
                + ",StockHoldersEquity BIGINT SIGNED"
                + ",CommonStocks BIGINT SIGNED"
                + ",CapitalSurplus BIGINT SIGNED"
                + ",RetainedEarnings BIGINT SIGNED"
                + ",TreasuryStock BIGINT SIGNED"
                + ",OtherEquity BIGINT SIGNED"
                + ",TotalEquity BIGINT SIGNED"
                + ",TotalLiabilitiesEquity BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createNasdaqQuarterlyIncomeStatements(self):
        if ( self.hasNoTable("NasdaqQuarterlyIncomeStatements")):
            query = ("CREATE TABLE NasdaqQuarterlyIncomeStatements "
                + "(" + self.symbol
                + "date DATE"
                + ",currency VARCHAR(100)"
                + ",totalRevenue BIGINT SIGNED"
                + ",costOfRevenue BIGINT SIGNED"
                + ",grossProfit BIGINT SIGNED"
                + ",operatingExpenses BIGINT SIGNED"
                + ",researchAndDevelopment BIGINT SIGNED"
                + ",salesGeneralandAdmin BIGINT SIGNED"
                + ",nonRecurringItems BIGINT SIGNED"
                + ",otherOperatingItems BIGINT SIGNED"
                + ",operatingIncome BIGINT SIGNED"
                + ",addlIncomeExpenseItems BIGINT SIGNED"
                + ",earningsBeforeInterestAndTax BIGINT SIGNED"
                + ",interestExpense BIGINT SIGNED"
                + ",earningsBeforeTax BIGINT SIGNED"
                + ",incomeTax BIGINT SIGNED"
                + ",minorityInterest BIGINT SIGNED"
                + ",equityEarningsLossUnconsolidatedSubsidiary BIGINT SIGNED"
                + ",netIncomeContOperations BIGINT SIGNED"
                + ",netIncome BIGINT SIGNED"
                + ",netIncomeApplicableToCommonShareHolders BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createNasdaqQuarterlyCashFlowStatements(self):
        if (self.hasNoTable("NasdaqQuarterlyCashFlowStatements")):
            query = ("CREATE TABLE NasdaqQuarterlyCashFlowStatements "
                + "(" + self.symbol
                + "date DATE"
                + ",currency VARCHAR(100)"
                + ",NetIncome BIGINT SIGNED"
                + ",CashFlowsOperatingrtivities BIGINT SIGNED"
                + ",Depreciation BIGINT SIGNED"
                + ",NetIncomeAdjustments BIGINT SIGNED"
                + ",ChangesinOperatingActivities BIGINT SIGNED"
                + ",AccountsReceivable BIGINT SIGNED"
                + ",ChangesinInventories BIGINT SIGNED"
                + ",OtherOperatingActivities BIGINT SIGNED"
                + ",Liabilities BIGINT SIGNED"
                + ",NetCashFlowOperating BIGINT SIGNED"
                + ",CashFlowsInvestingActivities BIGINT SIGNED"
                + ",CapitalExpenditures BIGINT SIGNED"
                + ",Investments BIGINT SIGNED"
                + ",OtherInvestingActivities BIGINT SIGNED"
                + ",NetCashFlowsInvesting BIGINT SIGNED"
                + ",CashFlowsFinancingActivities BIGINT SIGNED"
                + ",SaleandPurchaseofStock BIGINT SIGNED"
                + ",NetBorrowings BIGINT SIGNED"
                + ",OtherFinancingActivities BIGINT SIGNED"
                + ",NetCashFlowsFinancing BIGINT SIGNED"
                + ",EffectofExchangeRate BIGINT SIGNED"
                + ",NetCashFlow BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createNasdaqQuarterlyBalanceSheets(self):
        if (self.hasNoTable("NasdaqQuarterlyBalanceSheets")):
            query = ("CREATE TABLE NasdaqQuarterlyBalanceSheets "
                + "(" + self.symbol
                + "date Date"
                + ",currency VARCHAR(100)"
                + ",CurrentAssets BIGINT SIGNED"
                + ",CashandCashEquivalents BIGINT SIGNED"
                + ",ShortTermInvestments BIGINT SIGNED"
                + ",NetReceivables BIGINT SIGNED"
                + ",Inventory BIGINT SIGNED"
                + ",OtherCurrentAssets BIGINT SIGNED"
                + ",TotalCurrentAssets BIGINT SIGNED"
                + ",LongTermAssets BIGINT SIGNED"
                + ",LongTermInvestments BIGINT SIGNED"
                + ",FixedAssets BIGINT SIGNED"
                + ",Goodwill BIGINT SIGNED"
                + ",IntangibleAssets BIGINT SIGNED"
                + ",OtherAssets BIGINT SIGNED"
                + ",DeferredAssetCharges BIGINT SIGNED"
                + ",TotalAssets BIGINT SIGNED"
                + ",CurrentLiabilities BIGINT SIGNED"
                + ",AccountsPayable BIGINT SIGNED"
                + ",ShortTermDebtCurrentPortionofLongTermDebt BIGINT SIGNED"
                + ",OtherCurrentLiabilities BIGINT SIGNED"
                + ",TotalCurrentLiabilities BIGINT SIGNED"
                + ",LongTermDebt BIGINT SIGNED"
                + ",OtherLiabilities BIGINT SIGNED"
                + ",DeferredLiabilityCharges BIGINT SIGNED"
                + ",MiscStocks BIGINT SIGNED"
                + ",MinorityInterest BIGINT SIGNED"
                + ",TotalLiabilities BIGINT SIGNED"
                + ",StockHoldersEquity BIGINT SIGNED"
                + ",CommonStocks BIGINT SIGNED"
                + ",CapitalSurplus BIGINT SIGNED"
                + ",RetainedEarnings BIGINT SIGNED"
                + ",TreasuryStock BIGINT SIGNED"
                + ",OtherEquity BIGINT SIGNED"
                + ",TotalEquity BIGINT SIGNED"
                + ",TotalLiabilitiesEquity BIGINT SIGNED"
                + ",INDEX(symbol)"
                + ",INDEX(date))")
            print query
            self.mysql.commitExecute(query)

    def createGoogleQuarterlyIncomeStatements(self):
        if ( self.hasNoTable("GoogleQuarterlyIncomeStatements")):
            query = ("CREATE TABLE GoogleQuarterlyIncomeStatements ("
                + self.symbol
                + "date DATE"
                + ", timeSpan INT"
                + ",timeUnit VARCHAR(10)"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",revenue DECIMAL(20,2)"
                + ",otherRevenueTotal DECIMAL(20,2)"
                + ",totalRevenue DECIMAL(20,2)"
                + ",costOfRevenueTotal DECIMAL(20,2)"
                + ",grossProfit DECIMAL(20,2)"
                + ",sellingGeneralAdminExpensesTotal DECIMAL(20,2)"
                + ",researchDevelopment DECIMAL(20,2)"
                + ",depreciationAmortization DECIMAL(20,2)"
                + ",interestExpenseIncomeNetOperating DECIMAL(20,2)"
                + ",unusualExpenseIncome DECIMAL(20,2)"
                + ",otherOperatingExpensesTotal DECIMAL(20,2)"
                + ",totalOperatingExpense DECIMAL(20,2)"
                + ",operatingIncome DECIMAL(20,2)"
                + ",InterestIncomeExpenseNetNonOperating DECIMAL(20,2)"
                + ",gainLossOnSaleOfAssets DECIMAL(20,2)"
                + ",otherNet DECIMAL(20,2)"
                + ",incomeBeforeTax DECIMAL(20,2)"
                + ",incomeAfterTax DECIMAL(20,2)"
                + ",minorityInterest DECIMAL(20,2)"
                + ",equityInAffiliates DECIMAL(20,2)"
                + ",netIncomeBeforeExtraItems DECIMAL(20,2)"
                + ",accountingChange DECIMAL(20,2)"
                + ",discontinuedOperations DECIMAL(20,2)"
                + ",extraordinaryItem DECIMAL(20,2)"
                + ",netIncome DECIMAL(20,2)"
                + ",preferredDividends DECIMAL(20,2)"
                + ",incomeAvailabletoCommonExclExtraItems DECIMAL(20,2)"
                + ",incomeAvailabletoCommonInclExtraItems DECIMAL(20,2)"
                + ",basicWeightedAverageShares DECIMAL(20,2)"
                + ",basicEPSExcludingExtraordinaryItems DECIMAL(20,2)"
                + ",basicEPSIncludingExtraordinaryItems DECIMAL(20,2)"
                + ",dilutionAdjustment DECIMAL(20,2)"
                + ",dilutedWeightedAverageShares DECIMAL(20,2)"
                + ",dilutedEPSExcludingExtraordinaryItems DECIMAL(20,2)"
                + ",dilutedEPSIncludingExtraordinaryItems DECIMAL(20,2)"
                + ",dividendsperShareCommonStockPrimaryIssue DECIMAL(20,2)"
                + ",grossDividendsCommonStock DECIMAL(20,2)"
                + ",netIncomeafterStockBasedCompExpense DECIMAL(20,2)"
                + ",basicEPSafterStockBasedCompExpense DECIMAL(20,2)"
                + ",dilutedEPSafterStockBasedCompExpense DECIMAL(20,2)"
                + ",depreciationSupplemental DECIMAL(20,2)"
                + ",totalSpecialItems DECIMAL(20,2)"
                + ",normalizedIncomeBeforeTaxes DECIMAL(20,2)"
                + ",effectofSpecialItemsonIncomeTaxes DECIMAL(20,2)"
                + ",incomeTaxesExImpactofSpecialItems DECIMAL(20,2)"
                + ",normalizedIncomeAfterTaxes DECIMAL(20,2)"
                + ",normalizedIncomeAvailtoCommon DECIMAL(20,2)"
                + ",basicNormalizedEPS DECIMAL(20,2)"
                + ",dilutedNormalizedEPS DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)

    def createGoogleQuarterlyBalanceSheets(self):
        if ( self.hasNoTable("GoogleQuarterlyBalanceSheets")):
            query = ("CREATE TABLE GoogleQuarterlyBalanceSheets("
                + self.symbol
                + "date DATE"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",cashEquivalents DECIMAL(20,2)"
                + ",shortTermInvestments DECIMAL(20,2)"
                + ",cashandShortTermInvestments DECIMAL(20,2)"
                + ",accountsReceivableTradeNet DECIMAL(20,2)"
                + ",receivablesOther DECIMAL(20,2)"
                + ",totalReceivablesNet DECIMAL(20,2)"
                + ",totalInventory DECIMAL(20,2)"
                + ",prepaidExpenses DECIMAL(20,2)"
                + ",otherCurrentAssetsTotal DECIMAL(20,2)"
                + ",totalCurrentAssets DECIMAL(20,2)"
                + ",propertyPlantEquipmentTotalGross DECIMAL(20,2)"
                + ",accumulatedDepreciationTotal DECIMAL(20,2)"
                + ",goodwillNet DECIMAL(20,2)"
                + ",intangiblesNet DECIMAL(20,2)"
                + ",longTermInvestments DECIMAL(20,2)"
                + ",otherLongTermAssetsTotal DECIMAL(20,2)"
                + ",totalAssets DECIMAL(20,2)"
                + ",accountsPayable DECIMAL(20,2)"
                + ",accruedExpenses DECIMAL(20,2)"
                + ",notesPayableShortTermDebt DECIMAL(20,2)"
                + ",currentPortofLTDebtCapitalLeases DECIMAL(20,2)"
                + ",otherCurrentliabilitiesTotal DECIMAL(20,2)"
                + ",totalCurrentLiabilities DECIMAL(20,2)"
                + ",longTermDebt DECIMAL(20,2)"
                + ",capitalLeaseObligations DECIMAL(20,2)"
                + ",totalLongTermDebt DECIMAL(20,2)"
                + ",totalDebt DECIMAL(20,2)"
                + ",deferredIncomeTax DECIMAL(20,2)"
                + ",minorityInterest DECIMAL(20,2)"
                + ",otherLiabilitiesTotal DECIMAL(20,2)"
                + ",totalLiabilities DECIMAL(20,2)"
                + ",redeemablePreferredStockTotal DECIMAL(20,2)"
                + ",preferredStockNonRedeemableNet DECIMAL(20,2)"
                + ",commonStockTotal DECIMAL(20,2)"
                + ",additionalPaidInCapital DECIMAL(20,2)"
                + ",retainedEarningsAccumulatedDeficit DECIMAL(20,2)"
                + ",treasuryStockCommon DECIMAL(20,2)"
                + ",otherEquityTotal DECIMAL(20,2)"
                + ",totalEquity DECIMAL(20,2)"
                + ",totalLiabilitiesShareholdersEquity DECIMAL(20,2)"
                + ",sharesOutsCommonStockPrimaryIssue DECIMAL(20,2)"
                + ",totalCommonSharesOutstanding DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)

    def createGoogleQuarterlyCashFlowStatements(self):
        if ( self.hasNoTable("GoogleQuarterlyCashFlowStatements")):
            query = ("CREATE TABLE GoogleQuarterlyCashFlowStatements("
                + self.symbol
                + "date DATE"
                + ",timeSpan INT"
                + ",timeUnit VARCHAR(10)"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",netIncomeStartingLine DECIMAL(20,2)"
                + ",depreciationDepletion DECIMAL(20,2)"
                + ",amortization DECIMAL(20,2)"
                + ",deferredTaxes DECIMAL(20,2)"
                + ",nonCashItems DECIMAL(20,2)"
                + ",changesinWorkingCapital DECIMAL(20,2)"
                + ",cashfromOperatingActivities DECIMAL(20,2)"
                + ",capitalExpenditures DECIMAL(20,2)"
                + ",otherInvestingCashFlowItemsTotal DECIMAL(20,2)"
                + ",cashfromInvestingActivities DECIMAL(20,2)"
                + ",financingCashFlowItems DECIMAL(20,2)"
                + ",totalCashDividendsPaid DECIMAL(20,2)"
                + ",issuanceRetirementofStockNet DECIMAL(20,2)"
                + ",issuanceRetirementofDebtNet DECIMAL(20,2)"
                + ",cashfromFinancingActivities DECIMAL(20,2)"
                + ",foreignExchangeEffects DECIMAL(20,2)"
                + ",netChangeinCash DECIMAL(20,2)"
                + ",cashInterestPaidSupplemental DECIMAL(20,2)"
                + ",cashTaxesPaidSupplemental DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)

    def createGoogleAnnualIncomeStatements(self):
        if ( self.hasNoTable("GoogleAnnualIncomeStatements")):
            query = ("CREATE TABLE GoogleAnnualIncomeStatements ("
                + self.symbol
                + "date DATE"
                + ",timeSpan INT"
                + ",timeUnit VARCHAR(10)"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",revenue DECIMAL(20,2)"
                + ",otherRevenueTotal DECIMAL(20,2)"
                + ",totalRevenue DECIMAL(20,2)"
                + ",costOfRevenueTotal DECIMAL(20,2)"
                + ",grossProfit DECIMAL(20,2)"
                + ",sellingGeneralAdminExpensesTotal DECIMAL(20,2)"
                + ",ResearchDevelopment DECIMAL(20,2)"
                + ",depreciationAmortization DECIMAL(20,2)"
                + ",InterestExpenseIncomeNetOperating DECIMAL(20,2)"
                + ",unusualExpenseIncome DECIMAL(20,2)"
                + ",otherOperatingExpensesTotal DECIMAL(20,2)"
                + ",totalOperatingExpense DECIMAL(20,2)"
                + ",operatingIncome DECIMAL(20,2)"
                + ",interestIncomeExpenseNetNonOperating DECIMAL(20,2)"
                + ",gainLossOnSaleOfAssets DECIMAL(20,2)"
                + ",otherNet DECIMAL(20,2)"
                + ",incomeBeforeTax DECIMAL(20,2)"
                + ",incomeAfterTax DECIMAL(20,2)"
                + ",minorityInterest DECIMAL(20,2)"
                + ",equityInAffiliates DECIMAL(20,2)"
                + ",netIncomeBeforeExtraItems DECIMAL(20,2)"
                + ",accountingChange DECIMAL(20,2)"
                + ",discontinuedOperations DECIMAL(20,2)"
                + ",extraordinaryItem DECIMAL(20,2)"
                + ",netIncome DECIMAL(20,2)"
                + ",preferredDividends DECIMAL(20,2)"
                + ",incomeAvailabletoCommonExclExtraItems DECIMAL(20,2)"
                + ",incomeAvailabletoCommonInclExtraItems DECIMAL(20,2)"
                + ",basicWeightedAverageShares DECIMAL(20,2)"
                + ",basicEPSExcludingExtraordinaryItems DECIMAL(20,2)"
                + ",basicEPSIncludingExtraordinaryItems DECIMAL(20,2)"
                + ",dilutionAdjustment DECIMAL(20,2)"
                + ",dilutedWeightedAverageShares DECIMAL(20,2)"
                + ",dilutedEPSExcludingExtraordinaryItems DECIMAL(20,2)"
                + ",dilutedEPSIncludingExtraordinaryItems DECIMAL(20,2)"
                + ",dividendsperShareCommonStockPrimaryIssue DECIMAL(20,2)"
                + ",grossDividendsCommonStock DECIMAL(20,2)"
                + ",netIncomeafterStockBasedCompExpense DECIMAL(20,2)"
                + ",basicEPSafterStockBasedCompExpense DECIMAL(20,2)"
                + ",dilutedEPSafterStockBasedCompExpense DECIMAL(20,2)"
                + ",depreciationSupplemental DECIMAL(20,2)"
                + ",totalSpecialItems DECIMAL(20,2)"
                + ",normalizedIncomeBeforeTaxes DECIMAL(20,2)"
                + ",effectofSpecialItemsonIncomeTaxes DECIMAL(20,2)"
                + ",incomeTaxesExImpactofSpecialItems DECIMAL(20,2)"
                + ",normalizedIncomeAfterTaxes DECIMAL(20,2)"
                + ",normalizedIncomeAvailtoCommon DECIMAL(20,2)"
                + ",basicNormalizedEPS DECIMAL(20,2)"
                + ",dilutedNormalizedEPS DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)

    def createGoogleAnnualBalanceSheets(self):
        if ( self.hasNoTable("GoogleAnnualBalanceSheets")):
            query = ("CREATE TABLE GoogleAnnualBalanceSheets("
                + self.symbol
                + "date DATE"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",cashEquivalents DECIMAL(20,2)"
                + ",shortTermInvestments DECIMAL(20,2)"
                + ",cashandShortTermInvestments DECIMAL(20,2)"
                + ",accountsReceivableTradeNet DECIMAL(20,2)"
                + ",receivablesOther DECIMAL(20,2)"
                + ",totalReceivablesNet DECIMAL(20,2)"
                + ",totalInventory DECIMAL(20,2)"
                + ",prepaidExpenses DECIMAL(20,2)"
                + ",otherCurrentAssetsTotal DECIMAL(20,2)"
                + ",totalCurrentAssets DECIMAL(20,2)"
                + ",propertyPlantEquipmentTotalGross DECIMAL(20,2)"
                + ",accumulatedDepreciationTotal DECIMAL(20,2)"
                + ",goodwillNet DECIMAL(20,2)"
                + ",intangiblesNet DECIMAL(20,2)"
                + ",longTermInvestments DECIMAL(20,2)"
                + ",otherLongTermAssetsTotal DECIMAL(20,2)"
                + ",totalAssets DECIMAL(20,2)"
                + ",accountsPayable DECIMAL(20,2)"
                + ",accruedExpenses DECIMAL(20,2)"
                + ",notesPayableShortTermDebt DECIMAL(20,2)"
                + ",currentPortofLTDebtCapitalLeases DECIMAL(20,2)"
                + ",otherCurrentliabilitiesTotal DECIMAL(20,2)"
                + ",totalCurrentLiabilities DECIMAL(20,2)"
                + ",longTermDebt DECIMAL(20,2)"
                + ",capitalLeaseObligations DECIMAL(20,2)"
                + ",totalLongTermDebt DECIMAL(20,2)"
                + ",totalDebt DECIMAL(20,2)"
                + ",deferredIncomeTax DECIMAL(20,2)"
                + ",minorityInterest DECIMAL(20,2)"
                + ",otherLiabilitiesTotal DECIMAL(20,2)"
                + ",totalLiabilities DECIMAL(20,2)"
                + ",redeemablePreferredStockTotal DECIMAL(20,2)"
                + ",preferredStockNonRedeemableNet DECIMAL(20,2)"
                + ",commonStockTotal DECIMAL(20,2)"
                + ",additionalPaidInCapital DECIMAL(20,2)"
                + ",retainedEarningsAccumulatedDeficit DECIMAL(20,2)"
                + ",treasuryStockCommon DECIMAL(20,2)"
                + ",otherEquityTotal DECIMAL(20,2)"
                + ",totalEquity DECIMAL(20,2)"
                + ",totalLiabilitiesShareholdersEquity DECIMAL(20,2)"
                + ",sharesOutsCommonStockPrimaryIssue DECIMAL(20,2)"
                + ",totalCommonSharesOutstanding DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)

    def createGoogleAnnualCashFlowStatements(self):
        if ( self.hasNoTable("GoogleAnnualCashFlowStatements")):
            query = ("CREATE TABLE GoogleAnnualCashFlowStatements("
                + self.symbol
                + "date DATE"
                + ",timeSpan INT"
                + ",timeUnit VARCHAR(10)"
                + ",currency VARCHAR(5)"
                + ",currencyUnit VARCHAR(15)"
                + ",netIncomeStartingLine DECIMAL(20,2)"
                + ",depreciationDepletion DECIMAL(20,2)"
                + ",amortization DECIMAL(20,2)"
                + ",deferredTaxes DECIMAL(20,2)"
                + ",nonCashItems DECIMAL(20,2)"
                + ",changesinWorkingCapital DECIMAL(20,2)"
                + ",cashfromOperatingActivities DECIMAL(20,2)"
                + ",capitalExpenditures DECIMAL(20,2)"
                + ",otherInvestingCashFlowItemsTotal DECIMAL(20,2)"
                + ",cashfromInvestingActivities DECIMAL(20,2)"
                + ",financingCashFlowItems DECIMAL(20,2)"
                + ",totalCashDividendsPaid DECIMAL(20,2)"
                + ",issuanceRetirementofStockNet DECIMAL(20,2)"
                + ",issuanceRetirementofDebtNet DECIMAL(20,2)"
                + ",cashfromFinancingActivities DECIMAL(20,2)"
                + ",foreignExchangeEffects DECIMAL(20,2)"
                + ",netChangeinCash DECIMAL(20,2)"
                + ",cashInterestPaidSupplemental DECIMAL(20,2)"
                + ",cashTaxesPaidSupplemental DECIMAL(20,2)"
                + ",INDEX(symbol))")
            self.mysql.commitExecute(query)
