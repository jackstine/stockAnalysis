import os

import scrapy
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

from Common.utility import Filter
from pycharmCode.stock.controllers.financials import FinancialController
from pycharmCode.stock.repository.scrape import ScrapyErrorLog


class StockScrapy(scrapy.Spider):

    def __init__(self, controlTable, directory, *args, **kwargs):
        super(StockScrapy, self).__init__(*args, **kwargs)
        self.dirstuff = os.path.dirname(os.path.realpath(directory))
        self.f = Filter()
        self.controller = FinancialController(controlTable)
        self._getStartingURLS()
        self.errorLog = ScrapyErrorLog()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def _getStartingURLS(self):
        self.letter = self._getLetter()
        models = self.controller.getAvailableCompanySymbols(self.letter)
        for index,s in enumerate(models):
            if (not self._addURLS(index, s)):
                break

    def _getLetter(self):
        f = open(self.dirstuff + "/letter.txt" , 'r')
        letter = f.read()[0]
        f.close()
        return letter

    def parse(self, response):
        try:
            self.parsing(response)
        except Exception as e:
            self.errorLog.log(response, e, self.name)

    def spider_closed(self, spider):
        self.controller.insertCompleteModel()
        self.controller.updateCompleteModel()
        # self.controller.commit()
        self.controller.close()
        self.errorLog.close()
