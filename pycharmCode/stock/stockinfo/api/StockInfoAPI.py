from pycharmCode.stock.stockinfo.models.IDSymbolModel import IDSymbolModel
from pycharmCode.stock.stockinfo.repos import IDSymbolRepo
from pycharmCode.stock.repository.nasdaq import NasdaqReferenceRepository

class StockInfoAPI:
    def __init__(self, stream):
        self.stream = stream
        self.idRepo = IDSymbolRepo(self.stream)
        self.reference = NasdaqReferenceRepository(self.stream)

    def getAllSymbols(self):
        return [s.symbol for s in self.getAllStockIDInfo()]

    def getAllStockIDInfo(self):
        id = 0
        symbol = 1
        sector = 2
        industry = 3
        name = 4
        reference = 5
        theList = []
        for row in self.idRepo.selectAll().getRows():
            theList.append(IDSymbolModel(row[id], row[symbol], row[sector], row[industry], row[name], row[reference]))
        return theList

    def getAllSymbolToID(self):
        d = dict()
        ids = self.getAllStockIDInfo()
        for id in ids:
            d[id.symbol] = id.id
        return d

    def getSymbolsWithReference(self,letter):
        stocks = self.getAllStockIDInfo()
        return [sym.symbol for sym in filter(lambda x: x.reference == letter, stocks)]

    def delistStock(self, id):
        self.idRepo.delist(id)