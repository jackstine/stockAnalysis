import os, string,time, inspect

class ScrapyLetterController:
    #DEFAULT_PATH = os.path.expanduser("~") + "/Dropbox/Programs/Stock/code/stock/scrape/scrapycrawls"
    THIS_FILE_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
    DEFAULT_PATH = string.join(THIS_FILE_DIR.split("/")[:-1] + ["scrape","scrapycrawls"],"/")
    NASDAQ_SUMMARY = {"directory":"/nasdaq/summary","scrape":"/summary/spiders/"
        ,"scrapy":"QuoteSpider"}
    SPLIT_HISTORY = {"directory":"/splits","scrape":"/splits/spiders/"
        ,"scrapy":"SplitSpider"}
    NASDAQ_FINANCIALS = {"directory":"/nasdaq/financials","scrape":"/financials/spiders/"
        ,"scrapy":"FinancialSpider"}
    GOOGLE_FINANCIALS = {"directory":"/google/financials","scrape":"/financials/spiders/"
        ,"scrapy":"GoogleFinancialSpider"}
    YAHOO_FINANCIALS = {"directory":"/yahoo/financials/financial","scrape":"/financial/spiders/"
        ,"scrapy":"yahooFinancial"}
    BLOOMBERG_FINANCIALS = {"directory":"/bloomberg/financials","scrape":"/financials/spiders/", 
        "scrapy":"BloombergFinancials"}

    def __init__(self, extension):
        self.extension= extension
        self.extendTime()

    def extendTime(self):
        if (self.extension == self.NASDAQ_FINANCIALS or self.extension == self.YAHOO_FINANCIALS):
            self.extendTheTime = True
        else:
            self.extendTheTime = False

    def run(self):
        self.getDirectory()
        self.scrapeReferences()
        os.chdir(self.oldDirectory)

    def getDirectory(self):
        self.oldDirectory = os.getcwd()
        os.chdir(self.DEFAULT_PATH + self.extension["directory"])
        self.directory = os.getcwd()

    def scrapeReferences(self):
        references = string.uppercase
        for index,ref in enumerate(references):
            self.setScrapeFile(ref)
            self.scrape()
            self.runTime(index)

    def runTime(self, index):
        if (self.extendTheTime):
            if (index % 5 == 0):
                time.sleep(500)

    def setScrapeFile(self, ref):
        os.chdir(self.directory + self.extension["scrape"] )
        f = open("letter.txt",'w')    #the letter file allows us to do 1 file at a time
        f.write(ref)
        f.close()
        os.chdir(self.directory)

    def scrape(self):
        print self.extension["scrapy"]
        os.system("scrapy crawl " + self.extension["scrapy"])
