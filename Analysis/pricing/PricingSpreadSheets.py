from Analysis.pricing import PriceModel as pm
from Analysis.idsymbols import IdSymbols as IDapi
from Analysis.google import GoogleSpreadsheetAPI as GoogleSpAPI
from Analysis.pricing import PriceAPI
import pandas

def create_full_Dict():
    ID = "id"
    SYMBOL = "symbol"
    WEB = "Web"

    cocaCola = 3677
    stocks = []
    ids = IDapi.get_id_symbols()
    for i in range(0,10):
        id = ids.iloc[i,0]
        symbol = ids.iloc[i,1]
        d = PriceAPI.get_full_dict(id)
        d[ID] = id
        d[SYMBOL] = symbol
        d[WEB] = GoogleSpAPI.hyperlink_google_financial_website(symbol)
        stocks.append(d)
    df = pandas.DataFrame(stocks)
    #sort the list of columns
    priorityList = ["week","month", "quarter","year"]
    priorityColumns = []
    for col in list(df.columns.values):
        for i,type in enumerate(priorityList):
            if (type in col):
                priorityColumns.append(col)
    finalList = priorityColumns
    finalList.sort()
    displayColumns = [ID, WEB, pm.ANNULALIZED_MAX_RETURN, pm.ANNULALIZED_MAX_LOSS, pm.MAX_RETURN, pm.MAX_LOSS]
    displayColumns.extend(finalList)
    df.to_csv(path_or_buf="~/pricingStocks.csv", columns=displayColumns)