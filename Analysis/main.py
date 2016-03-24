from Analysis.idsymbols import IdSymbols as IDapi
from Analysis.splits import SplitAPI
from Analysis.pricing import PriceAPI
from Analysis.google import GoogleAPI
from Analysis.financial import FinancialAPI
import datetime
import pandas
from Analysis.common import Time





df = GoogleAPI.get_google_annual_financials(2)
FinancialAPI.transform_financials(df)
print df

# cocaCola = 3677

# prices = PriceAPI.get_split_adjusted_price(2)
# print PriceAPI.get_max_return(prices, 1000)
# print PriceAPI.get_max_loss(prices, 1000)
# print "%s   the number of gains ,   %s  the number of losses   that meet the margin" % PriceAPI.get_number_of_gains_and_losss_margin(prices, 1000, 0.10)
# PriceAPI.print_ratios(prices)