from ...repository.nasdaq import NasdaqReferenceRepository

class StockInfoAPI:
    def __init__(self, stream):
        self.stream = stream
        self.reference = NasdaqReferenceRepository()

    def getSymbols(self, letter):
        return [row[self.reference.STOCK_COLUMN] for row in self.reference.select(letter, self.stream).getRows()]

    def getAllSymbols(self):
        return [row[self.reference.STOCK_COLUMN] for row in self.reference.selectAll(self.stream).getRows()]
