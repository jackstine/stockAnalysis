from ...repopository.nasdaq import NasdaqSummaryRepo

class PriceAPI:
    def __init__(self, stream):
        self.stream = stream

    def getPrice(self, symbol):
        NasdaqSummaryRepo().selectAllIn(symbol)
