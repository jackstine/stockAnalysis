from stock.stockinfo.api import StockInfoAPI
from stock.stockinfo.repos import IDSymbolRepo
from stock.streams.mysql import DB
import string

db = DB(DB.Connections.STOCK)
stockAPI = StockInfoAPI(db)
symbols = stockAPI.getAllSymbols()
#for ds in symbols:
repo = IDSymbolRepo(db)
repo.insert('A')
db.commit()
