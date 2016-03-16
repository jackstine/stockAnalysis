import urllib2


class KitcoMetals:
    
    def __init__(self):
        self.site = "http://www.kitco.com/market/"
        self.information = []

    def getMetalPrices(self):
        self.clear()
        request = urllib2.urlopen(self.site)
        html = request.read()
        goldStart = html.find("GOLD")
        self.information.append(self.getInfo(goldStart, html))
        silverStart = html.find("SILVER", goldStart)
        self.information.append(self.getInfo(silverStart, html))
        platinumStart = html.find("PLATINUM", silverStart)
        self.information.append(self.getInfo(platinumStart, html))
        palladiumStart = html.find("PALLADIUM", platinumStart)
        self.information.append(self.getInfo(palladiumStart, html))
        rhodiumStart = html.find("RHODIUM", palladiumStart)
        self.information.append(self.getInfo(rhodiumStart, html))
        print self.information


    def getInfo(self, start, html):
        nameEnd = html.find("<", start)
        name = html[start:nameEnd]
        beginDate = html.find("<td>", nameEnd)
        endDate = html.find("<", beginDate + 1)
        date = html[beginDate + 4 : endDate]
        beginTime = html.find("<td>", endDate)
        beginBid = html.find("<td>", beginTime +1)
        endBid = html.find("<", beginBid + 1)
        bid = html[beginBid + 4: endBid]
        info = dict()
        info["name"] = name
        info["date"] = date
        info["bid"] = bid
        return info

    def clear(self):
        self.priceingModels = []
        self.listingModels = []
