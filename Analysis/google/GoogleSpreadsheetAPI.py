import Analysis.spreadsheets.Spreadsheets as sp
import Analysis.google.GoogleAPI as API
import pandas as pd
import Analysis.financial.FinancialAPI as fAPI
import Analysis.financial.GoogleModel as GM
import Analysis.financial.FinancialModel as f

def hyperlink_google_financial_website(symbol):
    return sp.hyperlink(API.google_financial_website(symbol), symbol)

def create_financial_spreadsheet():
    listOfPercentages = []
    ids = API.get_all_accurate_google_ids()
    for index in range(0,ids.shape[0]):
        id = ids.iloc[index,0]
        print id
        stocks = GM.get_google_annual_financials(id)
        p = fAPI.percentages(stocks,1,[f.NET_INCOME_IN_STATE,  f.REVENUE, f.OPERATING_INCOME, f.CASH_OPERATING])
        symbol = fAPI.add_symbol(stocks, p)
        p["website"] = hyperlink_google_financial_website(symbol)
        listOfPercentages.append(p)
    df = pd.DataFrame(listOfPercentages)
    df.to_csv(path_or_buf="~/stocksageww.csv")