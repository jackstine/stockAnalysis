import Analysis.spreadsheets.Spreadsheets as sp
import Analysis.google.GoogleAPI as API
import Analysis.google.GoogleSpreadsheetAPI as spAPI

def google_symbol_spreadsheet(func):
    path = "~/StockAnalysis/google_symbols_financials.csv"
    stocks = API.stocks_not_accounted_for_in_financials()
    websites = []
    for sym in stocks["symbol"]:
        websites.append(spAPI.hyperlink_google_financial_website(sym))
    stocks["website"] = websites
    stocks.to_csv(path_or_buf = path)