from scrapy import Item, Field
class IncomeItem(Item):
	Symbol = Field()
	Date = Field()
	TimeSpan = Field()
	TimeUnit = Field()
	Currency = Field()
	CurrencyUnit = Field()
	Revenue = Field()
	OtherRevenueTotal = Field()
	TotalRevenue = Field()
	CostofRevenueTotal = Field()
	GrossProfit = Field()
	SellingGeneralAdminExpensesTotal = Field()
	ResearchDevelopment = Field()
	DepreciationAmortization = Field()
	InterestExpenseIncomeNetOperating = Field()
	UnusualExpenseIncome = Field()
	OtherOperatingExpensesTotal = Field()
	TotalOperatingExpense = Field()
	OperatingIncome = Field()
	InterestIncomeExpenseNetNonOperating = Field()
	GainLossonSaleofAssets = Field()
	OtherNet = Field()
	IncomeBeforeTax = Field()
	IncomeAfterTax = Field()
	MinorityInterest = Field()
	EquityInAffiliates = Field()
	NetIncomeBeforeExtraItems = Field()
	AccountingChange = Field()
	DiscontinuedOperations = Field()
	ExtraordinaryItem = Field()
	NetIncome = Field()
	PreferredDividends = Field()
	IncomeAvailabletoCommonExclExtraItems = Field()
	IncomeAvailabletoCommonInclExtraItems = Field()
	BasicWeightedAverageShares = Field()
	BasicEPSExcludingExtraordinaryItems = Field()
	BasicEPSIncludingExtraordinaryItems = Field()
	DilutionAdjustment = Field()
	DilutedWeightedAverageShares = Field()
	DilutedEPSExcludingExtraordinaryItems = Field()
	DilutedEPSIncludingExtraordinaryItems = Field()
	DividendsperShareCommonStockPrimaryIssue = Field()
	GrossDividendsCommonStock = Field()
	NetIncomeafterStockBasedCompExpense = Field()
	BasicEPSafterStockBasedCompExpense = Field()
	DilutedEPSafterStockBasedCompExpense = Field()
	DepreciationSupplemental = Field()
	TotalSpecialItems = Field()
	NormalizedIncomeBeforeTaxes = Field()
	EffectofSpecialItemsonIncomeTaxes = Field()
	IncomeTaxesExImpactofSpecialItems = Field()
	NormalizedIncomeAfterTaxes = Field()
	NormalizedIncomeAvailtoCommon = Field()
	BasicNormalizedEPS = Field()
	DilutedNormalizedEPS = Field()
