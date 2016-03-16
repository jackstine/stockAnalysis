class IDSymbolModel:
    def __init__(self, id, symbol, sector, industry, name, reference):
        self.id = id
        self.symbol = symbol
        self.name = name
        self.sector = sector
        self.industry = industry
        self.reference = reference


    def __str__(self):
        return (str(self.id) + ", " + str(self.symbol) + ", " + str(self.name)
            + ", " + self.sector + ", " + self.industry)