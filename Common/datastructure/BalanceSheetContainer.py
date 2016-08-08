class BalanceSheetContainer:

	def __init__(self, info):
		self.symbol = info[0]
		self.currency = info[1]
		self.currencyUnit = info[2]
		self.date = info[3]
		self.cashEquivalents = info[4]
		self.shortTermInvestments = info[5]
		self.cashandShortTermInvestments = info[6]
		self.accountsReceivableTradeNet = info[7]
		self.receivablesOther = info[8]
		self.totalReceivablesNet = info[9]
		self.totalInventory = info[10]
		self.prepaidExpenses = info[11]
		self.otherCurrentAssetsTotal = info[12]
		self.totalCurrentAssets = info[13]
		self.propertyPlantEquipmentTotalGross = info[14]
		self.accumulatedDepreciationTotal = info[15]
		self.goodwillNet = info[16]
		self.intangiblesNet = info[17]
		self.longTermInvestments = info[18]
		self.otherLongTermAssetsTotal = info[19]
		self.totalAssets = info[20]
		self.accountsPayable = info[21]
		self.accruedExpenses = info[22]
		self.notesPayableShortTermDebt = info[23]
		self.currentPortofLTDebtCapitalLeases = info[24]
		self.otherCurrentliabilitiesTotal = info[25]
		self.totalCurrentLiabilities = info[26]
		self.longTermDebt = info[27]
		self.capitalLeaseObligations = info[28]
		self.totalLongTermDebt = info[29]
		self.totalDebt = info[30]
		self.deferredIncomeTax = info[31]
		self.minorityInterest = info[32]
		self.otherLiabilitiesTotal = info[33]
		self.totalLiabilities = info[34]
		self.redeemablePreferredStockTotal = info[35]
		self.preferredStockNonRedeemableNet = info[36]
		self.commonStockTotal = info[37]
		self.additionalPaidInCapital = info[38]
		self.retainedEarningsAccumulatedDeficit = info[39]
		self.treasuryStockCommon = info[40]
		self.otherEquityTotal = info[41]
		self.totalEquity = info[42]
		self.totalLiabilitiesShareholdersEquity = info[43]
		self.sharesOutsCommonStockPrimaryIssue = info[44]
		self.totalCommonSharesOutstanding = info[45]
