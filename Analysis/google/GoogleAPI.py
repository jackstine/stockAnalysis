from Analysis.financial import FinancialModel as f
from Analysis.sql.Con import con
import pandas as pd

#this will return the data frame of the id used here
def get_google_annual_financials(id):
    income = get_google_financial_annual_income_statement(id)
    balance = get_google_financial_annual_balance_sheets(id)
    cash = get_google_financial_annual_cash_flow_statements(id)
    merged = pd.merge(income, balance,how = "outer", on = f.DATE)
    finalMerged = pd.merge(cash, merged, how = 'outer', on = f.DATE)
    return finalMerged


def get_google_annual_income_statements(id):
    return con.read_id("GoogleAnnualIncomeStatements", id)

def get_google_annual_balance_sheet(id):
    return con.read_id("GoogleAnnualBalanceSheets", id)

def get_google_annual_cash_flow_statements(id):
    return con.read_id("GoogleAnnualCashFlowStatements", id)

def get_google_financial_annual_income_statement(id):
    return map_google_financial_income_annual(get_google_annual_income_statements(id))

def get_google_financial_annual_balance_sheets(id):
    return map_google_financial_balance_annual(get_google_annual_balance_sheet(id))

def get_google_financial_annual_cash_flow_statements(id):
    return map_google_financial_cash_flow_annual(get_google_annual_cash_flow_statements(id))


def map_google_financial_balance_annual(goog):
    df = pd.DataFrame()
    df[f.ID] = goog["id"]
    df[f.DATE] = goog["date"]
    df[f.CASH_BALANCE] = goog["cashEquivalents"]
    df[f.SHORT_TERM_INVESTMENTS] = goog["shortTermInvestments"]
    df[f.ACCOUNTS_RECEIVABLE] = goog["totalReceivablesNet"]
    df[f.INVENTORY] = goog["totalInventory"]
    df[f.CURRENT_ASSETS] = goog["totalCurrentAssets"]
    df[f.PROPERTY_PLANT_EQUIPMENT] = goog["propertyPlantEquipmentTotalGross"]
    df[f.ACCUMULATED_DEPRECIATION] = goog["accumulatedDepreciationTotal"]
    df[f.GOODWILL] =  goog["goodwillNet"]
    df[f.INTANGIBLES] = goog["intangiblesNet"]
    df[f.LONG_TERM_INVESTMENTS] = goog["longTermInvestments"] + goog["otherLongTermAssetsTotal"]
    df[f.TOTAL_ASSETS] = goog["totalAssets"]
    df[f.ACCOUNTS_PAYABLE] = goog["accountsPayable"]
    df[f.NOTES_PAYABLE] = goog["notesPayableShortTermDebt"]
    df[f.CURRENT_PORTION_OF_DEBT]  = goog["currentPortofLTDebtCapitalLeases"]
    df[f.CURRENT_LIABILITIES] = goog["totalCurrentLiabilities"]
    df[f.LONG_TERM_DEBT] = goog["totalLongTermDebt"]
    df[f.DEBT] = goog["totalDebt"]
    df[f.OTHER_LIABILITY] = goog["deferredIncomeTax"] + goog["minorityInterest"]  + goog["otherLiabilitiesTotal"]
    df[f.TOTAL_LIABILITY] = goog["totalLiabilities"]
    df[f.PAID_IN_CAPITAL] = goog["additionalPaidInCapital"]
    df[f.PREFERRED_STOCK] = goog["redeemablePreferredStockTotal"] + goog["preferredStockNonRedeemableNet"]
    df[f.RETAINED_EARNINGS] = goog["retainedEarningsAccumulatedDeficit"]
    df[f.TREASURY_STOCK] = goog["treasuryStockCommon"]
    df[f.TOTAL_EQUITY] = goog["totalEquity"]
    return df


def map_google_financial_income_annual(goog):
    df = pd.DataFrame()
    df[f.ID] = goog["id"]
    df[f.DATE] = goog["date"]
    df[f.REVENUE] = goog["totalRevenue"]
    df[f.COST_OF_REVENUE] = goog["costOfRevenueTotal"]
    df[f.GROSS_PROFIT] = goog["grossProfit"]
    df[f.SELLING_ADMIN_EXPENSE] = goog["sellingGeneralAdminExpensesTotal"]
    df[f.R_AND_D] = goog["ResearchDevelopment"]
    df[f.DEPRECIATION_INCOME] = goog["depreciationAmortization"]
    df[f.INTEREST_EXPENSE] = goog["InterestExpenseIncomeNetOperating"]
    df[f.UNUSUAL_EXPENSE] = goog["unusualExpenseIncome"] + goog["otherOperatingExpensesTotal"]
    df[f.OPERATING_EXPENSE] = goog["totalOperatingExpense"]
    df[f.OPERATING_INCOME] = goog["operatingIncome"]
    #TODO  what is interestIncomeExpenseNetNonOperating?????
    df[f.GAIN_ON_ASSETS] = goog["gainLossOnSaleOfAssets"]
    df[f.INCOME_BEFORE_TAX] = goog["incomeBeforeTax"]
    df[f.INCOME_AFTER_TAX] = goog["incomeAfterTax"]
    df[f.MINORITY_INTEREST] = goog["minorityInterest"]
    df[f.AFFILIATES] = goog["equityInAffiliates"]
    df[f.OTHER_ITEMS] = goog["discontinuedOperations"] + goog["accountingChange"] + goog["extraordinaryItem"]
    df[f.NET_INCOME_IN_STATE] = goog["netIncome"]
    df[f.PREFERRED_DIVIDENDS] = goog["preferredDividends"]
    return df



def map_google_financial_cash_flow_annual(goog):
    df = pd.DataFrame()
    df[f.ID] = goog["id"]
    df[f.DATE] = goog["date"]
    df[f.NET_INCOME_CASH_FLOW] = goog["netIncomeStartingLine"]
    df[f.DEPRECIATION_CASH_FLOW] = goog["depreciationDepletion"]
    df[f.AMORTIZATION] = goog["amortization"]
    df[f.DEFERRED_TAXES] = goog["deferredTaxes"]
    df[f.NON_CASH_ITEMS] = goog["nonCashItems"]
    df[f.WORKING_CAPITAL] = goog["changesinWorkingCapital"]
    df[f.CASH_OPERATING] = goog["cashfromOperatingActivities"]
    df[f.CAPITAL_EXPENDITURES] = goog["capitalExpenditures"]
    df[f.OTHER_INVESTMENTS] = goog["otherInvestingCashFlowItemsTotal"]
    df[f.CASH_INVESTING] = goog["cashfromInvestingActivities"]
    df[f.FINANCING_ITEMS] = goog["financingCashFlowItems"]
    df[f.DIVIDENDS] = goog["totalCashDividendsPaid"]
    df[f.CASH_STOCK] = goog["issuanceRetirementofStockNet"]
    df[f.CASH_DEBT] = goog["issuanceRetirementofDebtNet"]
    df[f.CASH_FINANCING] = goog["cashfromFinancingActivities"]
    df[f.NET_CHANGE_IN_CASH] = goog["netChangeinCash"]

    #TODO not sure if these are going to be made
    df[f.CASH_INTEREST_PAID] = goog["cashInterestPaidSupplemental"]
    df[f.CASH_TAXES_PAID] = goog["cashTaxesPaidSupplemental"]
    return df