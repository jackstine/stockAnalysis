from stock.controllers import ScrapyLetterController

scrape = ScrapyLetterController(ScrapyLetterController.NASDAQ_FINANCIALS)
scrape.run()
