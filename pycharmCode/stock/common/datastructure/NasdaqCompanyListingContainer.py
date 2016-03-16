class NasdaqCompanyListingContainer:

    def __init__(self, info):
        self.symbol = info["Symbol"]
        self.name = info["Name"]
        self.sector = info["Sector"]
        self.industry = info["industry"]
        self.letter = info["Letter"]

    def __str__(self):
        string = (self.symbol + ", " + self.name + ", " + self.sector
            + ", " + self.industry + ", " + self.letter)
        return string
