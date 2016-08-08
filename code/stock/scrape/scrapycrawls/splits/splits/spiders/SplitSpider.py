import scrapy, os, string

from Common.utility import Filter
from stock.stockinfo.api import StockInfoAPI
from stock.streams.models import InsertModel
from stock.streams.mysql import DB


class SplitSpider(scrapy.Spider):
    name = "SplitSpider"

    def __init__(self, *args, **kwargs):
        super(SplitSpider,self).__init__(*args,**kwargs)
        self.directory=os.path.dirname(os.path.realpath(__file__))
        self.db = DB(DB.Connections.STOCK)
        self.api = StockInfoAPI(self.db)
        letter = self._getLetter()
        self.stockInfos = self.api.getAllStockIDInfo()
        self.symbolToId = self.api.getAllSymbolToID()
        self._getStartingURLS(letter)

    def parse(self,response):
        splits = response.xpath("//center/div[@style='border: 1px solid #444444; background: #FFFFFF; width:1000px;']"
            + "/table[2]/tr/td[@width='208']/table[@style='font-family: Arial; font-size: 12px']/tr/td/text()").extract()
        symbol = string.split(response._url,"=")[1]
        id = self.symbolToId[symbol]
        inModel = self.getModel(splits,id)
        for m in inModel:
            self.db.insert(m).queue()
        self.db.commit()

    def getModel(self, splits, id):
        inModels = []
        dateI = 0
        splitInfoI = 1
        step = 2
        lengthOfSplits = len(splits)
        #DateI is the reference of the index that we are using
        while(dateI < lengthOfSplits):
            inModel = InsertModel("SplitHistory")
            dateSplitted = splits[dateI].split("/")
            date = string.join([dateSplitted[2], dateSplitted[0], dateSplitted[1]], "/")
            splitInfo = splits[splitInfoI]
            ratio = self.getSplitRatio(splitInfo)
            print date + "      "  +  str(ratio)
            #now we have the splitInfo  and the ratio
            inModel.insert("Date", str(date))
            inModel.insert("id", id)
            inModel.insert("Ratio", str(ratio))
            dateI += step
            splitInfoI += step
            inModels.append(inModel)
        return inModels

    def getSplitRatio(self, info):
        stringSplits = info.split(" ")
        numerator = stringSplits[0]
        denominator = stringSplits[2]
        return (float(numerator) / float(denominator))


    def _getLetter(self):
        """
        Used to get the letter for the database
        """
        f=open(self.directory+"/letter.txt","r")
        letter=f.read()[0]	#we only need the first character
        f.close()
        return letter


    def _getStartingURLS(self, letter):
        symbols = [s.symbol for s in self.stockInfos if (s.reference == letter)]
        for s in symbols:
            self.start_urls+=["https://www.stocksplithistory.com/?symbol="+s]