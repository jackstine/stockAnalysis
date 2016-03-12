from ..controllers.nasdaq import NasdaqDelistedController, NasdaqSplitsController
from ..controllers.nasdaq import NasdaqCompanyListingController, NasdaqUpcomingIPOSController
from ..controllers.nasdaq import NasdaqPricedIPOSController
from ..controllers import ScrapyLetterController
    

class AmericanStockDaily:

    def __init__(self, stream):
        self.stream = stream

    def run(self):
        self.runDelisted()
        self.runSplits()
        self.runUpcomingIPOS()
        self.runPricedIPOS()
        self.runCompanyListing()
        self.runSummaryQuotes()

    def runDelisted(self):
        NasdaqDelistedController(self.stream).run()

    def runSplits(self):
        NasdaqSplitsController(self.stream).run()

    def runUpcomingIPOS(self):
        NasdaqUpcomingIPOSController(self.stream).run()

    def runPricedIPOS(self):
        NasdaqPricedIPOSController(self.stream).run()

    def runCompanyListing(self):
        NasdaqCompanyListingController(self.stream).run()

    def runSummaryQuotes(self):
        ScrapyLetterController(ScrapyLetterController.NASDAQ_SUMMARY).run()
