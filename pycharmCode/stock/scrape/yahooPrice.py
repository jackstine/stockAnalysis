import datetime, urllib, csv, string

def getPrices(symbol, beginDate = None, endDate = None, all = False):
    sourceCSV = ""
    if all == True:
        sourceCSV = _connectToGetAll(symbol)
    else:
        sourceCSV = _connectingToCSV(symbol, beginDate, endDate)
    try:
        for index,row in enumerate(sourceCSV):
            if index==0:
                continue
            date=row[0]
            price=row[1]
            high=row[2]
            low=row[3]
            close=row[4]
            volume=row[5]
            adjClose=row[6]
            if index == 1:
                print "%s  DOING THIS IS THE FIRST DATE" % (date)
            if (index % 250 == 0 or index == 1):
                print "%s     %s     %s     %s     %s     %s     %s" % (date,price,high,low,close,volume,adjClose)
    except:
        print "Unable to do symbol " + symbol

def _connectingToURL(url):
    while True:
        try:
            source=urllib.urlopen(url)
            return source
        except IOError as e:
            error="Error: %s" % (e.args[0])
            print error

def _connectingToCSV(symbol,startDate, endDate):
    #a is the start month -1
    #b is the start date
    #c is the begin year
    #d is the end month - 1
    #e is the end day
    #f is the end year
    #g is day?>???
    a = endDate.month - 1
    b = endDate.day
    c = endDate.year
    d = startDate.month - 1
    e = startDate.day
    f = startDate.year
    url=('http://ichart.finance.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&ignore=.csv' % (symbol,a,b,c,d,e,f))
    print url
    source=_connectingToURL(url)
    sourceCSV=csv.reader(source)
    return sourceCSV

def _connectToGetAll(symbol):
    url=('http://ichart.finance.yahoo.com/table.csv?s='+symbol+'&c=2016&ignore=.csv')
    source=_connectingToURL(url)
    sourceCSV=csv.reader(source)
    return sourceCSV

def getAllPrices(symbol):
    getPrices(symbol,all = True)

def getTodaysPrice(symbols):
    """
    :param symbols: as a list
    :return: for each symbol, returns the corresponding bid of the stock
    """
    url=('http://finance.yahoo.com/d/quotes.csv?s=%s&f=nab' % string.join(symbols, "+"))
    source=_connectingToURL(url)
    sourceCSV=csv.reader(source)
    bids = list()
    for index,row in enumerate(sourceCSV):
        bids.append(row[2])
    return bids