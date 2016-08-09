from pycharmCode.stock.scrape.NasdaqSymbolChange import NasdaqSymbolChange
from pycharmCode.stock.streams.mysql.tables.CreateTables import CreateTables
from pycharmCode.stock.streams.mysql.SystemConfiguration.System import getBoolean, insert, _has, getDate
import pycharmCode.stock.streams.mysql.SystemConfiguration.Constants as sC
import Common.utility.Time as t
from pycharmCode.stock.scrape.yahooPrice import getPrices, getAllPrices, getTodaysPrice
from CircumpunctProcesses.WatchList import processWatchList

processWatchList()

# getPrices("AAL",t.now(), t.addYears(t.now(), -2))
# print getTodaysPrice(["AAL","CMRE"])
# n = NasdaqSymbolChange()
# sym = n.run()
# for i in sym:
#     print i