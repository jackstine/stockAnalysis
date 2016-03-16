import urllib
import csv
import time
import MySQLdb
import datetime
import threading

from stock.stockinfo.api import StockInfoAPI
from stock.streams.mysql import DB

#CREATE TABLE yahooCSV (symbol VARCHAR(10) ,date DATE,closePrice DECIMAL(13,4),todaysHigh DECIMAL(13,4)
#	,todaysLow DECIMAL(13,4),volume BIGINT UNSIGNED,adjClose DECIMAL(13,4), INDEX(symbol), INDEX(date))

today=datetime.date.today()


def updatingDatabase(sourceCSV,stockID):
    symbol = stockID.symbol
    id = stockID.id
    try:
    	connection=MySQLdb.connect(host='localhost',passwd='stockaholic',user='stock',db='stock')
    	cur=connection.cursor()
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
            if (index % 250 == 0):
                print "%s     %s     %s     %s     %s     %s     %s" % (date,price,high,low,close,volume,adjClose)
            cur.execute(('INSERT INTO NasdaqSummaryQuote (id,date,quote,high,low'
            	+',volume) VALUES (%s,%s,%s,%s,%s,%s)')
           	    ,(id,date,price,high,low,volume))
        connection.commit()
        connection.close()
    except MySQLdb.Error as e:
        print 'ERROR %s:%s' % (e[0],e[1])
    except:
        print symbol
        fileOpen=open('yahooSymNA.txt','a')
        fileOpen.write(symbol)
        fileOpen.write('\n')
        fileOpen.close()

def connectingToURL(url):
    while True:
        try:
            source=urllib.urlopen(url)
            return source
        except IOError as e:
            error="Error: %s" % (e.args[0])
            print error

def connectingToCSV(symbol):
    if today.day<=9:
        day='0'+str(today.day)
    else:
        day=today.day
    word=''
    url=('http://ichart.finance.yahoo.com/table.csv?s='+symbol+'&d='+str(today.month-1)+'&e='+str(day)+'&f='+str(today.year)+'&g=d&a=6&b=0&c=2013&ignore=.csv')
    source=connectingToURL(url)
    sourceCSV=csv.reader(source)
    return sourceCSV


def isGoodSymbol(sym):
    if ('^' in sym):
        return False
    else:
        return True

def connectAndFetch(symbol):
    source=connectingToCSV(str(symbol.symbol))
    updatingDatabase(source,symbol)

def main():
#	day=input('what day do you want :')
#	if day>9:
#		day='0'+str(day)
#	month=input('What month do you want (as a number):')
#	month=month-1
#	year=input('What year do you want :')
    try:
        db = DB(DB.Connections.STOCK)
        api = StockInfoAPI(db)
        stocks = api.getAllStockIDInfo()
        for index,symbol in enumerate(stocks):
            print 'doing symbol %s , %s of %s' % (symbol.id,symbol.symbol,len(stocks))
            if isGoodSymbol(symbol.symbol):
                connectAndFetch(symbol)
    except MySQLdb.Error as e:
        print e[0]
        print e[1]
        print 'there is a database error'


if __name__=='__main__':
    main()
