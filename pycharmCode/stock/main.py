from controllers import ScrapyLetterController
from stock.controllers.nasdaq import NasdaqCompanyListingController
from stock.scrape.SplitsScrape import SplitsScrape
from stock.streams.mysql import DB
from stock.stockinfo.api.StockInfoAPI import StockInfoAPI
import string

db = DB(DB.Connections.STOCK)
# scrape = SplitsScrape()
# api = StockInfoAPI(db)
# scrape.run(api.getAllStockIDInfo()[1:4])

scrape = ScrapyLetterController(ScrapyLetterController)
scrape.run()
db.close()