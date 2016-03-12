from stock.streams.mysql import DB,Query
from stock.tables import Table
from stock.compiler import FinancialCompiler
from stock.models.financial import FinancialModelFactory

db = DB(DB.Connections.STOCK)
q = Query(db)
q.add("GoogleAnnualIncomeStatements")
q.add("GoogleAnnualBalanceSheets")
q.remove("GoogleAnnualBalanceSheets", "symbol")
q.remove("GoogleAnnualBalanceSheets", "date")
q.add("GoogleAnnualCashFlowStatements")
q.remove("GoogleAnnualCashFlowStatements", "symbol")
q.remove("GoogleAnnualCashFlowStatements", "date")
query = "SELECT " + q.build() + " FROM GoogleAnnualCashFlowStatements, GoogleAnnualBalanceSheets, GoogleAnnualIncomeStatements "
query += "WHERE GoogleAnnualCashFlowStatements.symbol = GoogleAnnualBalanceSheets.symbol "
query += "AND GoogleAnnualIncomeStatements.symbol = GoogleAnnualBalanceSheets.symbol "
query += "AND GoogleAnnualIncomeStatements.symbol = GoogleAnnualCashFlowStatements.symbol "
query += "AND GoogleAnnualCashFlowStatements.date = GoogleAnnualBalanceSheets.date "
query += "AND GoogleAnnualIncomeStatements.date = GoogleAnnualBalanceSheets.date "
query += "AND GoogleAnnualIncomeStatements.date = GoogleAnnualCashFlowStatements.date LIMIT 10"

fields = q.getFields()
cur = db.executeQuery(query)

dictFields = dict()
for i,f in enumerate(fields):
    dictFields[f.lower()] = i

t = Table("Combined Google", cur.fetchall(), dictFields, "symbol", "date", FinancialModelFactory.makeGoogleAnnual)


#t.setRef("symbol","Symbol")
#t.setRef("date","Date")
#
#
#t.setRef("cashEquivalents","cashEquivalents")
#t.setRef("shortTermInvestments","shortTermInvestments")
#t.setRef("totalReceivablesNet","totalReceivable")
#t.setRef("totalInventory","inventory")
#t.setRef("totalCurrentAssets","totalCurrentAssets")
#t.setRef("propertyPlantEquipmentTotalGross","propertyPlant")
#t.setRef("accumulatedDepreciationTotal","depreciation")
#t.setRef("longTermInvestments","longTermInvestments")
#t.setRef("totalAssets","totalAssets")
#t.setRef("accountsPayable","accountsPayable")
#t.setRef("totalCurrentLiabilities","totalCurrentLiabilities")
#t.setRef("totalLongTermDebt","longTermDebt")
#t.setRef("totalDebt","totalDebt")
#t.setRef("minorityInterest","minorityInterest")
#t.setRef("totalLiabilities","totalLiabilities")
#t.setRef("preferredStockNonRedeemableNet","preferredStock")
#t.setRef("additionalPaidInCapital","paidInCapital")
#t.setRef("commonStockTotal","commonStock")
#t.setRef("treasuryStockCommon","treasuryStock")
#t.setRef("otherEquityTotal","otherEquity")
#t.setRef("totalEquity","totalEquity")
#
#
#t.setRef("depreciationDepletion","depreciation")
#t.setRef("amortization","amortization")
#t.setRef("deferredTaxes","defferedTaxes")
#t.setRef("cashfromOperatingActivities","cashFromOperatingActivities")
#t.setRef("capitalExpenditures","capitalExpenditures")
#t.setRef("cashfromInvestingActivities","cashFromInvestingActivities")
#t.setRef("cashfromFinancingActivities","financingCashFlowItems")
#t.setRef("totalCashDividendsPaid","cashDividends")
#t.setRef("issuanceRetirementofStockNet","stockAffect")
#t.setRef("issuanceRetirementofDebtNet","debtAffect")
#t.setRef("cashfromFinancingActivities","cashFromFinancingActivities")
#t.setRef("cashInterestPaidSupplemental","interestPaid")
#t.setRef("cashTaxesPaidSupplemental","taxesPaid")
#
#
#t.setRef("revenue","revenue")
#t.setRef("totalRevenue","totalRevenue")
#t.setRef("costOfRevenueTotal","costOfRevenue")
#t.setRef("grossProfit","grossProfit")
#t.setRef("sellingGeneralAdminExpensesTotal","sellingGeneralAdmin")
#t.setRef("ResearchDevelopment","rAndD")
#t.setRef("depreciationAmortization","depreciationandAmmortization")
#t.setRef("InterestExpenseIncomeNetOperating","interestExpense")
#t.setRef("totalOperatingExpense","totalOperatingExpenses")
#t.setRef("operatingIncome","operatingIncome")
#t.setRef("gainLossOnSaleOfAssets","saleofAssets")
#t.setRef("incomeBeforeTax","incomeBeforeTax")
#t.setRef("minorityInterest","minorityInterest")  #2 Minority Interest
#t.setRef("netIncome","netIncome")
#t.setRef("preferredDividends","preferredDividends")


#t.compileCollections(FinancialCompiler())




















































#    google = open("GoogleBase.csv", 'w')
#    count = 0
#    while(True):
#        if (count == 0):
#            rows = fields
#        else:
#            rows = cur.fetchone()
#        if (rows == None):
#            break
#        for r in rows:
#            google.write(str(r) + ",")
#        google.write("\n")
#        count += 1
#
#    google.close()
