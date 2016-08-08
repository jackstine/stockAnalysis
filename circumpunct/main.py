from Analysis.idsymbols.IdSymbols import get_symbol
from circumpunct.API import getStocks

stocks = getStocks()
print len(stocks)
maxID = 0
for i in stocks:
    symbol = get_symbol(i.ID)["symbol"][0]
    maxID = max(maxID,i.ID)
    if (symbol != i.symbol):
        print symbol + " in DB needs to be changed   " + i.symbol + "     ID:  " + str(i.ID)
