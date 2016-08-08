from Common.U import getFromDict

class Summary:
    def __init__(self, d):
        self.exchange = d["Exchange"]
        self.marketCap = d['Marketcap']
        self.pe = getFromDict(d,"PERatio")
        self.price = d['LastSale']
        self.volume = d['Volume']
        self.symbol = d['Symbol']

    def setId(self, id):
        self.id = id