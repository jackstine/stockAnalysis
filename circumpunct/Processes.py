import circumpunct.API as api
import string
from pycharmCode.stock.utility.Email import sendText, sendEmail
from time import sleep
import Analysis.idsymbols.IdSymbols as ids
from pycharmCode.stock.scrape import ScrapyAPI
from pycharmCode.stock.models import NasdaqSummaryModel as summaryM

def runWatchList():
    while True:
        messages = processWatchList()
        if (len(messages) > 0):
            s = string.join(messages,"\n")
            sendEmail(s)
            sendText(s)
            break
        sleep(10)


def getSummaryOfWatchList():
    watches = api.getWatchList()
    for w in watches:
        symbol = ids.get_symbol(w.stockId)['symbol'][0]
        summary = summaryM.Summary(ScrapyAPI.getNasdaqSummary(symbol))
        summary.setId(w.stockId)
        w.setSummary(summary)
    return watches

def processWatchList():
    watches = getSummaryOfWatchList()
    messages = list()
    links = list()
    for w in watches:
        if (w.canBuy() or w.isHigh() or w.isLow()):
            links.append(api.getStockOpinionWebPage(w.stockId))
        if (w.canBuy()):
            messages.append("Can buy " + w.summary.symbol + " now at " + w.summary.price)
        if (w.isLow()):
            messages.append(w.summary.symbol + " is now low at " + w.summary.price)
        if (w.isHigh()):
            messages.append(w.summary.symbol + " is now high at " + w.summary.price)
    messages.extend(links)
    return messages