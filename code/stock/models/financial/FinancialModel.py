from .. import RowModel

class FinancialModel(RowModel):
    def __init__(self, symbol, date, cashEquivalents, shortTermInvestments, 
        totalReceivable, inventory, totalCurrentAssets, propertyPlant
        , longTermInvestments, totalAssets, accountsPayable, totalCurrentLiabilities, 
        longTermDebt, totalDebt, minorityInterest, totalLiabilities, preferredStock
        , paidInCapital, commonStock, treasuryStock, otherEquity, 
        totalEquity, depreciation, amortization, defferedTaxes, cashFromOperatingActivities
        , capitalExpenditures, cashFromInvestingActivities, financingCashFlowItems, cashDividends, 
        issuanceOfStock, issuanceOfDebt, cashFromFinancingActivities, interestPaid, taxesPaid
        , revenue, totalRevenue, costOfRevenue, grossProfit, 
        sellingGeneralAdmin, rAndD, depreciationandAmmortization, interestExpense, totalOperatingExpenses
        , operatingIncome, saleofAssets, incomeBeforeTax, netIncome, preferredDividends, data):

        RowModel.__init__(self,data)
        self.symbol = symbol
        self.date = date
        self.cashEquivalents = cashEquivalents
        self.shortTermInvestments = shortTermInvestments
        self.totalReceivable = totalReceivable
        self.inventory = inventory
        self.totalCurrentAssets = totalCurrentAssets
        self.propertyPlant = propertyPlant
        self.depreciation = depreciation
        self.longTermInvestments = longTermInvestments
        self.totalAssets = totalAssets
        self.accountsPayable = accountsPayable
        self.totalCurrentLiabilities = totalCurrentLiabilities
        self.longTermDebt = longTermDebt
        self.totalDebt = totalDebt
        self.minorityInterest = minorityInterest
        self.totalLiabilities = totalLiabilities
        self.preferredStock = preferredStock
        self.paidInCapital = paidInCapital
        self.commonStock = commonStock
        self.treasuryStock = treasuryStock
        self.otherEquity = otherEquity
        self.totalEquity = totalEquity
        self.amortization = amortization
        self.defferedTaxes = defferedTaxes
        self.cashFromOperatingActivities = cashFromOperatingActivities
        self.capitalExpenditures = capitalExpenditures
        self.cashFromInvestingActivities = cashFromInvestingActivities
        self.financingCashFlowItems = financingCashFlowItems
        self.cashDividends = cashDividends
        self.issuanceOfStock = issuanceOfStock
        self.issuanceOfDebt = issuanceOfDebt
        self.cashFromFinancingActivities = cashFromFinancingActivities
        self.interestPaid = interestPaid
        self.taxesPaid = taxesPaid
        self.revenue = revenue
        self.totalRevenue = totalRevenue
        self.costOfRevenue = costOfRevenue
        self.grossProfit = grossProfit
        self.sellingGeneralAdmin = sellingGeneralAdmin
        self.rAndD = rAndD
        self.depreciationandAmmortization = depreciationandAmmortization
        self.interestExpense = interestExpense
        self.totalOperatingExpenses = totalOperatingExpenses
        self.operatingIncome = operatingIncome
        self.saleofAssets = saleofAssets
        self.incomeBeforeTax = incomeBeforeTax
        self.netIncome = netIncome
        self.preferredDividends = preferredDividends
