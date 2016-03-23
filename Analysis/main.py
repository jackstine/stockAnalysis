from Analysis.idsymbols import IdSymbols as IDapi
from Analysis.splits import SplitAPI
from Analysis.pricing import PriceAPI
from Analysis.google import GoogleAPI
import datetime
import pandas
from Analysis.common import Time





print GoogleAPI.get_google_annual_balance_sheet(2)
print GoogleAPI.get_google_annual_cash_flow_statements(2)
print GoogleAPI.get_google_annual_income_statements(2)


# cocaCola = 3677

# prices = PriceAPI.get_split_adjusted_price(2)
# print PriceAPI.get_max_return(prices, 1000)
# print PriceAPI.get_max_loss(prices, 1000)
# print "%s   the number of gains ,   %s  the number of losses   that meet the margin" % PriceAPI.get_number_of_gains_and_losss_margin(prices, 1000, 0.10)
# PriceAPI.print_ratios(prices)