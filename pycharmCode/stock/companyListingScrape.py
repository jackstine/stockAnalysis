from pycharmCode.stock.controllers.nasdaq import NasdaqCompanyListingController
from pycharmCode.stock.streams.mysql import DB

db = DB(DB.Connections.STOCK)
scrape = NasdaqCompanyListingController(db)
scrape.run()
db.close()
