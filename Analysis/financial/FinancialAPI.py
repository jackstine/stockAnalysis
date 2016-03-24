import FinancialModel as f



#transforms the financial model into the columns of the dataframe that have been calculated yet, because of
#dependencies that are needed.  One example is using fields in the Income Statement
#and one in the Balance Sheet to create a new field.  Such as Return on Assets
def transform_financials(fin):
    fin[f.RETURN_ON_ASSETS] = fin[f.NET_INCOME_IN_STATE] / fin[f.TOTAL_ASSETS]
    fin[f.DIVIDEND_PAYOUT_RATIO] = fin[f.DIVIDENDS] / fin[f.NET_INCOME_IN_STATE]
    fin[f.GROSS_MARGIN] = (fin[f.REVENUE] - fin[f.COST_OF_REVENUE]) / fin[f.REVENUE]
    fin[f.OPERATING_MARGIN] = fin[f.OPERATING_INCOME] / fin[f.REVENUE]
    fin[f.PROFIT_MARGIN] = fin[f.NET_INCOME_IN_STATE] / fin[f.REVENUE]
    fin[f.RETURN_ON_EQUITY] = fin[f.NET_INCOME_IN_STATE] / fin[f.TOTAL_EQUITY]
    fin[f.GOODWILL_EQUITY] = fin[f.GOODWILL] / fin[f.TOTAL_EQUITY]
    fin[f.ASSET_TURNOVER] = fin[f.REVENUE] / fin[f.TOTAL_ASSETS]
    fin[f.INVENTORY_TURNOVER] = fin[f.REVENUE] / fin[f.INVENTORY]
    # TODO decide if I want to user DEBT or TOTAL_LIABILITY
    fin[f.DEBT_RATIO] = fin[f.TOTAL_LIABILITY] / fin[f.TOTAL_ASSETS]
    fin[f.DEBT_OPERATING_CASH_CASH_RATIO] = fin[f.DEBT] / fin[f.CASH_OPERATING]
    fin[f.DEBT_OPERATING_INCOME_RATIO] = fin[f.DEBT] / fin[f.OPERATING_INCOME]
    fin[f.DEBT_INCOME_RATIO] = fin[f.DEBT] / fin[f.NET_INCOME_IN_STATE]
    fin[f.DEBT_EQUITY_RATIO] = fin[f.TOTAL_LIABILITY] / fin[f.TOTAL_EQUITY]
    fin[f.ACID_TEST_RATIO] = (fin[f.CASH_BALANCE] + fin[f.ACCOUNTS_RECEIVABLE]
                            + fin[f.SHORT_TERM_INVESTMENTS]) / fin[f.CURRENT_LIABILITIES]
    fin[f.INTEREST_COVERAGE] = fin[f.OPERATING_INCOME] / fin[f.INTEREST_EXPENSE]
    fin[f.FIXED_OPERATING_CASH] = fin[f.CASH_OPERATING] - fin[f.WORKING_CAPITAL]
    fin[f.DEBT_FIXED_OPERATING_CASH] = fin[f.DEBT] / fin[f.FIXED_OPERATING_CASH] # NOTE must be before FIXED_OPERATING_CASH
    fin[f.CURRENT_RATIO] = fin[f.CURRENT_ASSETS] / fin[f.CURRENT_LIABILITIES]
    fin[f.QUICK_RATIO] = (fin[f.CURRENT_ASSETS] - fin[f.INVENTORY] )/ fin[f.CURRENT_LIABILITIES]
    fin[f.CASH_RATIO] = ( fin[f.CASH_BALANCE] + fin[f.SHORT_TERM_INVESTMENTS] ) / fin[f.CURRENT_LIABILITIES]
    fin[f.RECEIVABLES_TURNOVER] = fin[f.REVENUE] / fin[f.ACCOUNTS_RECEIVABLE]   # NOTE should be credit Revenue
    fin[f.OPERATING_CASH_FLOW_RATIO] = fin[f.CASH_OPERATING] / fin[f.DEBT]



    # Weighted Average Cost of Capital
    # Return on Invested Capital ROIC
    # Average Collection Period
    #