#-*- coding: utf-8 -*-
import sys,os
import datetime
sys.path.insert(1, os.path.expanduser("~") + "/PycharmProjects/untitled/")
from stock.utility import Filter, Time
from stock.controllers.financials import FinancialController
from stock.models import InsertModel
from stock.repository.scrape import ScrapyErrorLog
from stock.scrape import StockScrapy

import scrapy
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher


class BloombergfinancialsSpider(StockScrapy):
    name = "BloombergFinancials"

    def __init__(self,category=None,*args,**kwargs):
        super(BloombergfinancialsSpider,self).__init__(controlTable= FinancialController.BLOOMBERG, directory=__file__, *args,**kwargs)

    def _addURLS(self, index, s):
        s = s.upper()
        s = s.replace(".", "/")
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=cashFlow&period=A&currency=native"]
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=balanceSheet&period=A&currency=native"]
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=incomeStatement&period=A&currency=native"]
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=cashFlow&period=Q&currency=native"]
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=balanceSheet&period=Q&currency=native"]
        self.start_urls += ["http://www.bloomberg.com/research/stocks/financials/financials.asp?ticker="+ s +"&dataset=incomeStatement&period=Q&currency=native"]
        return True

    def getTable(self, response):
        url = response._url
        if ("cashFlow&period=A" in url):
            return "BloombergAnnualCashFlowStatements"
        elif ("cashFlow&period=Q" in url):
            return "BloombergQuarterlyCashFlowStatements"
        elif ("balanceSheet&period=Q" in url):
            return "BloombergQuarterlyBalanceSheets"
        elif ("balanceSheet&period=A" in url):
            return "BloombergAnnualBalanceSheets"
        elif ("incomeStatement&period=A" in url):
            return "BloombergAnnualIncomeStatements"
        elif ("incomeStatement&period=Q" in url):
            return "BloombergQuarterlyIncomeStatements"
            
    def parsing(self, response):
        table = self.getTable(response)
        symbol = response.xpath("//span[@itemprop = 'tickerSymbol']/text()").extract()[0]
        currency = response.xpath('//table[@class="financialStatement"]/tr/td[@class="headerLite"]/text()').extract()
        colHeaders = response.xpath('//table[@class="financialStatement"]/tr/td[@class="headerDark bold "]/text()').extract()
        colHeadersBold = response.xpath('//table[@class="financialStatement"]/tr/td[@class="headerDark bold  gray"]/text()').extract()
        rowHeaders = response.xpath('//table[@class="financialStatement"]/tr/td[@class="statementLabel cell"]/text()').extract()
        rowData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell"]/text()').extract()
        rowGrayData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell gray"]/text()').extract()
        boldRowHeaders = response.xpath('//table[@class="financialStatement"]/tr/td[@class="statementLabel cell bold indent"]/text()').extract()
        boldRowData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell bold indent"]/text()').extract()
        boldGrayRowData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell bold indent gray"]/text()').extract()
        extraBoldHeaders = response.xpath('//table[@class="financialStatement"]/tr/td[@class="statementLabel cell bold b4"]/text()').extract()
        extraBoldData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell bold b4"]/text()').extract()
        extraGrayBoldData = response.xpath('//table[@class="financialStatement"]/tr/td[@class="cell bold b4 gray"]/text()').extract()
        models = []
        print currency[1]

        numOfHeaders = (len(colHeaders) + len(colHeadersBold) ) / 2
        for col in range(0,numOfHeaders):
            dateOf = self.getDate(col, colHeaders, colHeadersBold)
            if (dateOf == -1):
                continue
            rowIndex = 0
            dataIndex = col / 2
            grayIndex = col / 2
            boldDataIndex = col/ 2
            boldGrayDataIndex = col/ 2
            extraBoldIndex = col/ 2
            extraGrayBoldIndex = col/ 2
#            print len(colHeaders)
#            print len(rowData)
#            print len(rowHeaders)
            m = InsertModel(table)
            m.insert("symbol", symbol)
            m.insert("date", dateOf)
            m.insert("currency", currency[1])
#            print response._url
#            print dateOf
            if ((col + 1)% 2 == 1):
                while(rowIndex < len(rowHeaders)):
                    r = self.f.filterHeader(rowHeaders[rowIndex])
                    rowIndex += 1
                    m.insert(r, self.f.convertDashesToZero(self.f.filterNonListedData(rowData[dataIndex])))
#                    print r + "     " + self.f.convertDashesToZero(self.f.filterNonListedData(rowData[dataIndex]))
                    dataIndex += len(colHeaders) / 2
                for head in boldRowHeaders:
                    h = self.f.filterHeader(head)
                    m.insert(h, self.f.convertDashesToZero(self.f.filterNonListedData(boldRowData[boldDataIndex])))
#                    print h + "      "  + self.f.convertDashesToZero(self.f.filterNonListedData(boldRowData[boldDataIndex]))
                    boldDataIndex += len(colHeaders) / 2
                for head in extraBoldHeaders:
                    h = self.f.filterHeader(head)
                    m.insert(h, self.f.convertDashesToZero(self.f.filterNonListedData(extraBoldData[extraBoldIndex])))
#                    print h + "    " + self.f.convertDashesToZero(self.f.filterNonListedData(extraBoldData[extraBoldIndex]))
                    extraBoldIndex += len(colHeaders) / 2
            else:
                while(rowIndex < len(rowHeaders)):
                    r = self.f.filterHeader(rowHeaders[rowIndex])
                    rowIndex += 1
                    m.insert(r, self.f.convertDashesToZero(self.f.filterNonListedData(rowGrayData[grayIndex])))
#                    print r + "     " + self.f.convertDashesToZero(self.f.filterNonListedData(rowGrayData[grayIndex]))
                    grayIndex += len(colHeaders) / 2
                for head in boldRowHeaders:
                    h = self.f.filterHeader(head)
                    m.insert(h, self.f.convertDashesToZero(self.f.filterNonListedData(boldGrayRowData[boldGrayDataIndex])))
#                    print h + "      "  + self.f.convertDashesToZero(self.f.filterNonListedData(boldGrayRowData[boldGrayDataIndex]))
                    boldGrayDataIndex += len(colHeaders) / 2
                for head in extraBoldHeaders:
                    h = self.f.filterHeader(head)
                    m.insert(h, self.f.convertDashesToZero(self.f.filterNonListedData(extraGrayBoldData[extraGrayBoldIndex])))
#                    print h + "    " + self.f.convertDashesToZero(self.f.filterNonListedData(extraGrayBoldData[extraGrayBoldIndex]))
                    extraGrayBoldIndex += len(colHeaders) / 2
            models.append(m)
        self.controller.insert(symbol,models)

    def getDate(self, num, colHeaders, colHeadersBold):
        left = (num / 2 ) * 2  # round num down and multiply by 2
        right = left + 1
        date = None
        if (num % 2 == 0):
            date = colHeaders[left] + " " + colHeaders[right]
        if (num % 2 == 1):
            date = colHeadersBold[left] + " " + colHeadersBold[right]
        if (date == '-- --'):
            return -1
        return str(datetime.datetime.strptime(date, '%b %d %Y').date())
