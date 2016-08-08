from Analysis.idsymbols import IdSymbols as IDapi
from Analysis.splits import SplitAPI
from Analysis.pricing import PriceAPI
from Analysis.pricing import PriceModel as pm
from Analysis.google import GoogleAPI
from Analysis.google import GoogleSpreadsheetAPI as GoogleSpAPI
from Analysis.financial import GoogleModel as GM
from Analysis.google import GoogleCSV as gCSV
from Analysis.financial import FinancialAPI as fAPI
from Analysis.financial import FinancialModel as f
from Analysis.sql.Con import con
import datetime
import pandas
from Common.utility import Time
from pycharmCode.stock.scrape import ScrapyAPI

# get the summary Quote of a symbol
# summary = ScrapyAPI.getNasdaqSummary("AAL")
# print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
# print summary['Marketcap']
# print summary['LastSale']
# print summary['PERatio']






# ALL_STOCKS = []
# for number in range(1,10):
#     df = GoogleAPI.get_google_annual_financials(number)
#     FinancialAPI.transform_financials(df)
#     percentageDF = FinancialAPI.percentages(df)
#     print percentageDF




# id = 1220
# prices = PriceAPI.get_split_adjusted_price(id)
# d = PriceAPI.dict_of_ratios(prices)
# print d






# ID = "id"
# SYMBOL = "symbol"
# WEB = "Web"
# SPLITS = "Has_Splits"
#
# cocaCola = 3677
# stocks = []
# ids = IDapi.get_id_symbols()
# for i in range(0,ids.shape[0] - 1):
#     id = ids.iloc[i,0]
#     symbol = ids.iloc[i,1]
#     d = PriceAPI.get_full_dict(id)
#     d[ID] = id
#     d[SYMBOL] = symbol
#     d[SPLITS] = SplitAPI.has_splits(id)
#     d[WEB] = GoogleSpAPI.hyperlink_google_financial_website(symbol)
#     stocks.append(d)
# df = pandas.DataFrame(stocks)
# #sort the list of columns
# priorityList = ["week","month", "quarter","year"]
# priorityColumns = []
# for col in list(df.columns.values):
#     for i,type in enumerate(priorityList):
#         if (type in col):
#             priorityColumns.append(col)
# finalList = priorityColumns
# finalList.sort()
# displayColumns = [ID, WEB, SPLITS, pm.ANNULALIZED_MAX_RETURN, pm.ANNULALIZED_MAX_LOSS, pm.MAX_RETURN, pm.MAX_LOSS]
# displayColumns.extend(finalList)
# df.to_csv(path_or_buf="~/pricingStocks.csv", columns=displayColumns)







    #
    # for key,value in d.iteritems():
    #     print "%s : %s" % (key, value)

#
# stocks = []
# ids = IDapi.get_id_symbols()
# for i in range(1,2):
#     id = ids.iloc[i,0]
#     symbol = ids.iloc[i,1]
#     d = dict()
#     prices = PriceAPI.get_split_adjusted_price(id)
#     p = PriceAPI._get_prices_begin_date(prices,PriceAPI._get_number_of_rows(prices))
#     for e in p.prices:
#         print e
#     for key, value in pm.TERMS.iteritems():
#         longMaxReturn, daysLong = PriceAPI.get_max_long_return(prices, value[pm.TERM])
#         d["long_max_" + key] = longMaxReturn
#         d["annualized_long_" + key] = PriceAPI.get_annulized_return_days(longMaxReturn, daysLong)
#     d["id"] = id
#     d["symbol"] = symbol
#     d["Web"] = GoogleSpAPI.hyperlink_google_financial_website(symbol)
#     stocks.append(d)
# df = pandas.DataFrame(stocks)
# df.to_csv(path_or_buf="~/Options.csv")




# print PriceAPI.get_max_return(prices, 1000)
# print PriceAPI.get_max_loss(prices, 1000)
# print "%s   the number of gains ,   %s  the number of losses   that meet the margin" % PriceAPI.get_number_of_gains_and_losss_margin(prices, 1000, 0.10)