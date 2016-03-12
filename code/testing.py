from stock.stockinfo.api import StockInfoAPI
from stock.streams.mysql import DB

db = DB(DB.Connections.STOCK)
print StockInfoAPI(db).getSymbols(None)
db.close()
