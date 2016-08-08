from pycharmCode.stock.streams.mysql import DB

def dropNasdaq():
    global db
    db.commitExecute("Drop TABLE NasdaqQuarterlyIncomeStatements")
    db.commitExecute("Drop TABLE NasdaqQuarterlyBalanceSheets")
    db.commitExecute("Drop TABLE NasdaqQuarterlyCashFlowStatements")
    db.commitExecute("Drop TABLE NasdaqAnnualIncomeStatements")
    db.commitExecute("Drop TABLE NasdaqAnnualBalanceSheets")
    db.commitExecute("Drop TABLE NasdaqAnnualCashFlowStatements")
    db.commitExecute("drop table NasdaqFinancialCompletes")

def dropBloomberg():
    global db
    db.commitExecute("Drop TABLE BloombergQuarterlyIncomeStatements")
    db.commitExecute("Drop TABLE BloombergQuarterlyBalanceSheets")
    db.commitExecute("Drop TABLE BloombergQuarterlyCashFlowStatements")
    db.commitExecute("Drop TABLE BloombergAnnualIncomeStatements")
    db.commitExecute("Drop TABLE BloombergAnnualBalanceSheets")
    db.commitExecute("Drop TABLE BloombergAnnualCashFlowStatements")
    db.commitExecute("drop table BloombergFinancialCompletes")

def dropYahoo():
    global db
    db.commitExecute("Drop TABLE YahooQuarterlyIncomeStatements")
    db.commitExecute("Drop TABLE YahooQuarterlyBalanceSheets")
    db.commitExecute("Drop TABLE YahooQuarterlyCashFlowStatements")
    db.commitExecute("Drop TABLE YahooAnnualIncomeStatements")
    db.commitExecute("Drop TABLE YahooAnnualBalanceSheets")
    db.commitExecute("Drop TABLE YahooAnnualCashFlowStatements")
    db.commitExecute("drop table YahooFinancialCompletes")

def dropGoogle():
    global db
    db.commitExecute("Drop TABLE GoogleAnnualIncomeStatements")
    db.commitExecute("Drop TABLE GoogleAnnualBalanceSheets")
    db.commitExecute("Drop TABLE GoogleAnnualCashFlowStatements")
    db.commitExecute("Drop TABLE GoogleQuarterlyIncomeStatements")
    db.commitExecute("Drop TABLE GoogleQuarterlyBalanceSheets")
    db.commitExecute("Drop TABLE GoogleQuarterlyCashFlowStatements")
    db.commitExecute("drop table GoogleFinancialCompletes")

def dropOthers():
    global db
    db.commitExecute("Drop table ScrapyErrorLog")
    db.commitExecute("Drop table FinancialErrorLog")

if (__name__== "__main__"):
    db = DB(DB.Connections.STOCK)
    #dropNasdaq()
    dropBloomberg()
    dropYahoo()
    dropGoogle()
    #dropOthers()
    db.close()
