import circumpunct.API as api
import string
from pycharmCode.stock.utility.Email import sendText, sendEmail
from time import sleep
import Analysis.idsymbols.IdSymbols as ids
from pycharmCode.stock.scrape import yahooPrice
from pycharmCode.stock.models.PriceModel import PriceModel as pm
from circumpunct.model import StockData as sd

def runWatchList():
    while True:
        messages = processWatchList()
        if (len(messages) > 0):
            s = string.join(messages,"\n")
            sendEmail(s)
            sendText(s)
            break
        sleep(10)


def getPricesOfWatchList():
    watches = api.getWatchList()
    symbols = list()
    for w in watches:
        symbol = ids.get_symbol(w.stockId)['symbol'][0] # replace this api, with the one on the site,  the site will return this info
        symbols.append(symbol)
    print symbols
    prices = yahooPrice.getTodaysPrice(symbols)
    print prices
    for i, p in enumerate(prices):
        watches[i].setPriceModel(pm(symbols[i], p))
    return watches

def processWatchList():
    watches = getPricesOfWatchList()
    messages = list()
    links = list()
    for w in watches:
        if (w.canBuy() or w.isHigh() or w.isLow()):
            links.append(api.getStockOpinionWebPage(w.stockId))
        if (w.canBuy()):
            messages.append("Can buy " + w.symbol + " now at " + w.price)
        if (w.isLow()):
            messages.append(w.symbol + " is now low at " + w.price)
        if (w.isHigh()):
            messages.append(w.symbol + " is now high at " + w.price)
    messages.extend(links)
    for w in watches:
        api.updateStockData(sd(w.stockId, w.price))
    return messages