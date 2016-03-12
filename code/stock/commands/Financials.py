from ..controllers import ScrapyLetterController

class Financials():
    def __init__(self):
        pass

    def run(self):
        self.runNasdaq()
        self.runYahoo()
        self.runBloomberg()
        self.runGoogle()

    def runNasdaq(self):
        ScrapyLetterController(ScrapyLetterController.NASDAQ_FINANCIALS).run()

    def runYahoo(self):
        ScrapyLetterController(ScrapyLetterController.YAHOO_FINANCIALS).run()

    def runBloomberg(self):
        ScrapyLetterController(ScrapyLetterController.BLOOMBERG_FINANCIALS).run()

    def runGoogle(self):
        ScrapyLetterController(ScrapyLetterController.GOOGLE_FINANCIALS).run()
        
