class IncomeStatementContainer:
	"""To init, place a MYSQL select Google IncomeStatement result into the parameter
	This allows us to access the fields in the mysql result with names
	"""

	def __init__(self, info):
		self.symbol = info[0]
		self.currency = info[1]
		self.currencyUnit = info[2]
		self.date = info[3]
		self.timeSpan = info[4]
		self.timeUnit = info[5]
		self.revenue = info[6]
		self.otherRevenu = info[7]
		self.totalRevenue = info[8]
		self.costofRevenu = info[9]
		self.grossProfit = info[10]
		self.sellingGenAdminExpense = info[11]
		self.researchAndDevelopment = info[12]
		self.depreciationAmortization = info[13]
		self.interestExpens = info[14]
		self.unusualExpens = info[15]
		self.otherOperatingExpens = info[16]
		self.totalOperatingExpense = info[17]
		self.operatingIncome = info[18]
		self.interestIncome = info[19]
		self.gainLossOnAssets = info[20]
		self.otherNet = info[21]
		self.incomeBeforeTax = info[22]
		self.incomeAfterTax = info[23]
		self.minorityInterest = info[24]
		self.equityInAffiliates = info[25]
		self.netIncomeBeforeExtraItems = info[26]
		self.accountingChange = info[27]
		self.discontinuedOperations = info[28]
		self.extraordinaryItem = info[29]
		self.netIncome = info[30]
		self.preferredDividends = info[31]
		self.incomeAvailabletoCommonExclExtraItems = info[32]
		self.incomeAvailabletoCommonInclExtraItems = info[33]
		self.basicWeightedAverageShares = info[34]
		self.basicEPSExcludingExtraordinaryItems = info[35]
		self.basicEPSIncludingExtraordinaryItems = info[36]
		self.dilutionAdjustment = info[37]
		self.dilutedWeightedAverageShares = info[38]
		self.dilutedEPSExcludingExtraordinaryItems = info[39]
		self.dilutedEPSIncludingExtraordinaryItems = info[40]
		self.dividendsperShareCommonStockPrimaryIssue = info[41]
		self.grossDividendsCommonStock = info[42]
		self.netIncomeafterStockBasedCompExpense = info[43]
		self.basicEPSafterStockBasedCompExpense = info[44]
		self.dilutedEPSafterStockBasedCompExpense = info[45]
		self.depreciationSupplemental = info[46]
		self.totalSpecialItems = info[47]
		self.normalizedIncomeBeforeTaxes = info[48]
		self.effectofSpecialItemsonIncomeTaxes = info[49]
		self.incomeTaxesExImpactofSpecialItems = info[50]
		self.normalizedIncomeAfterTaxes = info[51]
		self.normalizedIncomeAvailtoCommon = info[52]
		self.basicNormalizedEPS = info[53]
		self.dilutedNormalizedEPS = info[54]
