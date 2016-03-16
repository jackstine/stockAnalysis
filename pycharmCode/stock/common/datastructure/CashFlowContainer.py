class CashFlowContainer:

	def __init__(self, info):
		self.symbol = info[0]
		self.currency = info[1]
		self.currencyUnit = info[2]
		self.date = info[3]
		self.timeSpan = info[4]
		self.timeUnit = info[5]
		self.netIncomeStartingLine = info[6]
		self.depreciationDepletion = info[7]
		self.amortization = info[8]
		self.deferredTaxes = info[9]
		self.nonCashItems = info[10]
		self.changesinWorkingCapital = info[11]
		self.cashfromOperatingActivities = info[12]
		self.capitalExpenditures = info[13]
		self.otherInvestingCashFlowItemsTotal = info[14]
		self.cashfromInvestingActivities = info[15]
		self.financingCashFlowItems = info[16]
		self.totalCashDividendsPaid = info[17]
		self.issuanceRetirementofStockNet = info[18]
		self.issuanceRetirementofDebtNet = info[19]
		self.cashfromFinancingActivities = info[20]
		self.foreignExchangeEffects = info[21]
		self.netChangeinCash = info[22]
		self.cashInterestPaidSupplemental = info[23]
		self.cashTaxesPaidSupplemental = info[24]

