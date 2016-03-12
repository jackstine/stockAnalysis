from stock.commands import Financials, AmericanStockDaily, DailyInformation
from stock.streams.mysql import DB

db = DB(DB.Connections.STOCK)
#DailyInformation().run()
AmericanStockDaily(db).run()
#Financials().run()
db.close()
