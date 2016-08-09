class SymbolChange:
    def __init__(self):
        self.newSymbol = None
        self.oldSymbol = None
        self.date = None

    def __str__(self):
        return "%s  %s   %s" % (self.newSymbol, self.oldSymbol, self.date)