from ...streams.mysql import DB, Ops
from ...streams.mysql.connections import Connections
from ...models import Model, InsertModel
from ...models import createDictFromModel
from ...repository.financials import CompletesRepo, FinancialErrorLog
from ...utility import Time

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
        self.completesRepo = CompletesRepo(completeTable)
        self.completeTable = completeTable
        self.error = FinancialErrorLog()
        self.dateDict = dict()
        self.updateDates = dict()

    def getAvailableCompanySymbols(self,letter):
        self.currentModel = self.completesRepo.getCurrentFinancials(self.mysql, letter)
        self._setCurrentModel()
        return self._getCurrentSymbols()

    def _setCurrentModel(self):
        self.currentDictModel = createDictFromModel(self.currentModel, ["symbol"])

    def _getCurrentSymbols(self):
        symbolField = self.currentModel.getField("symbol")
        symbols = []
        for r in self.currentModel.getRows():
            symbols.append(r[symbolField])
        return symbols

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()

    def insert(self, currentSymbol, itemList):
        try:
            currentModel = self._getModelFromSymbol(currentSymbol)
            self.insertValidModels(currentModel, itemList)
        except Exception as e:
            errorMessage = str(e)
            self.error.insert(self.mysql, errorMessage, currentSymbol, itemList[0].table)

    def _getModelFromSymbol(self, sym):
        return self.currentDictModel[sym]

    def insertValidModels(self, currentModel, itemList):
        dayField = self.completeTable.lower() + ".dayexspectingquarter"
        validList = []
        if (currentModel.getValue(dayField) == "None"):
            self.insertModels(itemList, self.dateDict)
        else:
            for item in itemList:
                if (self.validDateRange(item.getValue("Date"), currentModel.getValue(dayField))):
                    validList.append(item)
            self.insertModels(validList, self.updateDates)

    def validDateRange(self, itemDate, modelRange):
        iDate = Time.convertSQLStringDate(itemDate)
        modelRange = Time.convertSQLStringDate(modelRange)
        return ( (str(itemDate) >= str(modelRange - self.THIRTY_DAYS)) and (str(itemDate) <= str(modelRange + self.THIRTY_DAYS)) )

    def insertModels(self, itemList, maxDates):
        for item in itemList:
            self.mysql.insert(item).queue()
        self._setMaxDate(itemList, maxDates)

    def insertCompleteModel(self):
        for key, value in self.dateDict.iteritems():
            nextDate = value + self.QUARTER
            model = InsertModel(self.completeTable)
            model.insert("symbol", key)
            model.insert("dayexspectingquarter", str(nextDate))
            self.mysql.insert(model).queue()

    def updateCompleteModel(self):
        for key, value in self.updateDates.iteritems():
            nextDate = value + self.QUARTER
            model = InsertModel(self.completeTable)
            model.insert("dayexspectingquarter", str(nextDate))
            self.mysql.update(model).where("symbol", self.mysql.Ops.EQUALS, key).queue()

    def deleteCompleteModel(self, itemList):
        model = Model(self.completeTable)
        self.mysql.delete(model).where("symbol", self.mysql.Ops.EQUALS, itemList[0].getValue("symbol"))

    def _setMaxDate(self, itemList, maxDateList):
        dateIsInList = itemList[0].getValue("symbol") in maxDateList
        maxDate = self._getCurrentMaxDate(itemList, maxDateList)
        for i in itemList:
            if (i.getValue("Date") > maxDate):
                maxDate = i.getValue("Date")
        if ( (dateIsInList and maxDate != maxDateList[itemList[0].getValue("symbol")]) or (not dateIsInList)):
            conversion = Time.convertSQLStringDate(maxDate)
            maxDateList[itemList[0].getValue("symbol")] = conversion

    def _getCurrentMaxDate(self, itemList, maxDateList):
        dateIsInList = itemList[0].getValue("symbol") in maxDateList
        if (dateIsInList):
            maxDate = str(maxDateList[itemList[0].getValue("symbol")])
        else:
            maxDate = itemList[0].getValue("Date")
        return maxDate
