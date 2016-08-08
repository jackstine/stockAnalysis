from Analysis.financial import FinancialModel as f
from Analysis.sql.Con import con

def stocks_not_accounted_for_in_financials():
    #returns the stocks that are not listed in the income statements of the google database
    # TODO maybe add a reference to the date that it is between....
    stocks = con.read_query("SELECT sym.id, symbol FROM IDSymbol as sym LEFT JOIN GoogleAnnualIncomeStatements as goog ON goog.id = sym.id WHERE goog.id IS NULL")
    return stocks

def get_all_google_ids():
    return con.read_query("SELECT DISTINCT(sym.id), symbol FROM IDSymbol as sym LEFT JOIN GoogleAnnualIncomeStatements as goog ON goog.id = sym.id WHERE goog.id IS NOT NULL")

def get_all_non_accurate_google_ids():
    # the data shows that 12 months, 52 weeks, 53 weeks are the accepted forms of information that we will allow, the others are not
    return con.read_query("select DISTINCT(id) from GoogleAnnualIncomeStatements where timeSpan != 12 AND timeSpan != 52 AND timeSpan != 53")

def get_all_accurate_google_ids():
    return con.read_query("select DISTINCT(id) from GoogleAnnualIncomeStatements where timeSpan = 12 OR timeSpan = 52 OR timeSpan = 53")

def google_financial_website(symbol):
    return "https://www.google.com/finance?q=" + symbol +"&ei=tDQMV_nSAYvGe-TsofgE"

def get_google_annual_income_statements(id):
    return con.read_id("GoogleAnnualIncomeStatements", id)

def get_google_annual_balance_sheet(id):
    return con.read_id("GoogleAnnualBalanceSheets", id)

def get_google_annual_cash_flow_statements(id):
    return con.read_id("GoogleAnnualCashFlowStatements", id)