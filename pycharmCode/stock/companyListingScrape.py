from controllers import ScrapyLetterController
from stock.controllers.nasdaq import NasdaqCompanyListingController
from stock.scrape.nasdaq import NasdaqCompanyListing
from stock.streams.mysql import DB
from stock.stockinfo.api.StockInfoAPI import StockInfoAPI
from stock.controllers import ScrapyLetterController

db = DB(DB.Connections.STOCK)
scrape = NasdaqCompanyListingController(db)
scrape.run()
db.close()
