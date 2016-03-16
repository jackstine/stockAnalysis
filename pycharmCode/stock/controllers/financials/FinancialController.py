from stock.streams.mysql import DB, Ops
from stock.streams.mysql.connections import Connections
from stock.streams.models import Model, InsertModel
from stock.streams.models import createDictFromModel
from stock.repository.financials import CompletesRepo, FinancialErrorLog
from stock.common.utility import Time

class FinancialController:
    GOOGLE = CompletesRepo.GOOGLE
    NASDAQ = CompletesRepo.NASDAQ
    BLOOMBERG = CompletesRepo.BLOOMBERG
    YAHOO = CompletesRepo.YAHOO
    QUARTER = Time.t(days = 90)
    ANNUAL = Time.t(days = 360)
    THIRTY_DAYS = Time.t(days = 30)

    def __init__(self, completeTable):
        self.mysql = DB(Connections.STOCK)
        self.completesRepo = CompletesRepo(completeTable, self.mysql)
        self.completeTable = completeTable
        self.error = FinancialErrorLog()
        self.dateDict = dict()
        self.updateDates = dict()

    def getAvailableCompanySymbols(self,letter):
        self.currentModel = self.completesRepo.getCurrentFinancials(letter)
        self._setCurrentModel()
        return self._getCurrentSymbols()

    def _setCurrentModel(self):
        self.currentDictModel = createDictFromModel(self.currentModel, ["symbol", self.completeTable + ".tableName"])

    def _getCurrentSymbols(self):
        symbolField = self.currentModel.getField("symbol")
        symbols = set()
        for r in self.currentModel.getRows():
            symbols.add(r[symbolField])
        return [s for s in symbols]

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()

    def getTableDictItems(self, itemList):
        itemListDict = dict()
        for item in itemList:
            if (itemListDict.has_key(item.table)):
                itemListDict[item.table].append(item)
            else:
                itemListDict[item.table] = []
        return itemListDict

    def insert(self, currentSymbol, itemList):
        try:
            itemListDict = self.getTableDictItems(itemList)
            for table,itemTableList in itemListDict.iteritems():
                currentModelComplete = self._getModelFromSymbolTable(currentSymbol, table)
                self.insertValidModels(currentModelComplete, itemTableList)
        except Exception as e:
            print "********************************FINANCIAL CONTROLLER **************************************"
            print str(e)
            errorMessage = str(e)
            self.error.insert(self.mysql, errorMessage, currentSymbol, itemList[0].table)

    def _getModelFromSymbolTable(self, sym, table):
        try:
            return self.currentDictModel[sym + table]
        except Exception as e:
            return self.currentDictModel[sym + "None"]

    def insertValidModels(self, currentModel, itemList):
        dayField = self.completeTable.lower() + ".dayexspectingquarter"
        validList = []
        if (currentModel.getValue(dayField) == "None"):
            self.insertModels(itemList, self.dateDict, currentModel)
        else:
            for item in itemList:
                if (self.validDateRange(item.getValue("Date"), currentModel.getValue(dayField))):
                    validList.append(item)
            self.insertModels(validList, self.updateDates, currentModel)




        #
        # dayField = self.completeTable.lower() + ".dayexspectingquarter"
        # for i in itemList:
        #     currentModel = self._getModelFromSymbolTable(symbol, i.table)
        #     if (currentModel.getValue(dayField) == "None"):
        #         self.insertModels([i], self.dateDict, currentModel)
        #     elif (self.validDateRange(i.getValue("Date"), currentModel.getValue(dayField))):
        #         self.insertModels([i], self.updateDates, currentModel)

    def validDateRange(self, itemDate, modelRange):
        iDate = Time.convertSQLStringDate(itemDate)
        modelRange = Time.convertSQLStringDate(modelRange)
        return ( (str(itemDate) >= str(modelRange - self.THIRTY_DAYS)) and (str(itemDate) <= str(modelRange + self.THIRTY_DAYS)) )

    def insertModels(self, itemList, maxDates, currentModel):
        id = currentModel.getValue("id")
        for item in itemList:
            item.insert("id",id)
            item.remove("symbol")
            self.mysql.insert(item).queue()
        self._setMaxDate(itemList, maxDates)

    def insertCompleteModel(self):
        for key, value in self.dateDict.iteritems():
            nextDate = value.date + self.QUARTER
            model = InsertModel(self.completeTable)
            model.insert("id", key)
            print str(value)
            model.insert("tableName", value.table)
            model.insert("dayexspectingquarter", str(nextDate))
            self.mysql.insert(model).queue()

    def updateCompleteModel(self):
        for key, value in self.updateDates.iteritems():
            nextDate = value.date + self.QUARTER
            model = InsertModel(self.completeTable)
            model.insert("dayexspectingquarter", str(nextDate))
            model.insert("tablename", str(value.table))
            self.mysql.update(model).where("id", self.mysql.Ops.EQUALS, key).queue()

    def deleteCompleteModel(self, itemList, id):
        model = Model(self.completeTable)
        self.mysql.delete(model).where("id", self.mysql.Ops.EQUALS, )

    def _setMaxDate(self, itemList, maxDateList):
        dateIsInList = itemList[0].getValue("id") in maxDateList
        maxDate = self._getCurrentMaxDate(itemList, maxDateList)
        for i in itemList:
            if (i.getValue("Date") > maxDate):
                maxDate = i.getValue("Date")
        if ( (dateIsInList and maxDate != maxDateList[itemList[0].getValue("id")].date) or (not dateIsInList)):
            conversion = Time.convertSQLStringDate(maxDate)
            dt = DateTable(conversion, itemList[0].table)
            maxDateList[itemList[0].getValue("id")] = dt

    def _getCurrentMaxDate(self, itemList, maxDateList):
        dateIsInList = itemList[0].getValue("id") in maxDateList
        if (dateIsInList):
            maxDate = str(maxDateList[itemList[0].getValue("id")].date)
        else:
            maxDate = itemList[0].getValue("Date")
        return maxDate

class DateTable:
    def __init__(self, date, table):
        self.date = date
        self.table = table

    def __str__(self):
        return str(self.date) + "    " + str(self.table)