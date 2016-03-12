class NasdaqCompanyListingContainer:

    def __init__(self, info):
        self.symbol = info["Symbol"]
        self.name = info["Name"]
        self.sector = info["Sector"]
        self.industry = info["industry"]
        self.letter = info["Letter"]
        self.association = ""

    def setAssociation(self, association):
        self.association = association

    def __hash__(self):
        return self.association.__hash__()

    def __cmp__(self, other):
        if (self.association < other):
            return -1
        elif (self.association > other):
            return 1
        else:
            return 0

    def __eq__(self, other):
        return self.association.__eq__(other)

    def __str__(self):
        string = (self.symbol + ", " + self.name + ", " + self.sector
            + ", " + self.industry + ", " + self.letter)
        return string
