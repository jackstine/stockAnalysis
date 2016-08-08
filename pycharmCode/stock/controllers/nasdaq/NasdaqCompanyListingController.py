import string

from Common.datastructure import KeyValue
from pycharmCode.stock.scrape.nasdaq import NasdaqCompanyListing
from pycharmCode.stock.stockinfo.api import StockInfoAPI
from pycharmCode.stock.stockinfo.repos import IDSymbolRepo
from pycharmCode.stock.streams.models import InsertModel
from pycharmCode.stock.streams.models.ModelAlgorithms import getStringModels


class NasdaqCompanyListingController:

    def __init__(self, stream):
        self.stream = stream
        self.stockInfoAPI = StockInfoAPI(self.stream)
        self.idRepo = IDSymbolRepo(self.stream)
        self.scrape = NasdaqCompanyListing()
        self.companiesFromDB = self.stockInfoAPI.getAllStockIDInfo()
        self.companyNames = self.get_name_kv(self.companiesFromDB)
        self.companySymbols = self.get_symbol_kv(self.companiesFromDB)
        self.resetModels()

    def run(self):
        for letter in string.uppercase[:]:
            self.scrape.pull(letter)
            self.filterData(self.scrape.listOfInformation, letter)
            self.updateRepos()
            self.insertRepos()
            self.printInfo()
            self.resetModels()
        self.stream.commit()

    def printInfo(self):
        for p in self.newModelsToSend:
            print p

    def resetModels(self):
        self.newModelsToSend = []
        self.nameUpdateModels = []
        self.symbolUpdateModels = []

    def filterData(self, info, letter):

        setOfSymbolKV, setOfNameKV = self.getKVPairs(info)


        newNames = setOfNameKV - self.companyNames
        newNamesSymbols = self.get_symbol_kv([name.value for name in newNames])
        existingSymbolsNewNames = newNamesSymbols & self.companySymbols     #all the same symbols, but new names
        existingSymbolsNewNames = [sym.value for sym in existingSymbolsNewNames]
        newSymbolsNewNames = newNamesSymbols - self.companySymbols          #companies who have not existed yet



        newSymbols = setOfSymbolKV - self.companySymbols
        newSymbolsNames = self.get_name_kv([symbol.value for symbol in newSymbols])
        existingNamesNewSymbols = newSymbolsNames & self.companyNames       #companies whos symbols have changed
        existingNamesNewSymbols = [name.value for name in existingNamesNewSymbols]
        newNamesNewSymbols = newSymbolsNames - self.companySymbols          #companies who have not existed yet

        newNameList = self.get_symbol_kv([name.value for name in newNamesNewSymbols])
        newSymbolList = self.get_symbol_kv([symbol.value for symbol in newSymbolsNewNames])

        #add All three of these together to get the new list of companies that need to be added
        companiesToAdd = newSymbolList & newNameList
        companiesSymbolsToAdd = newSymbolList - newNameList
        companiesNamesToAdd = newNameList - newSymbolList

        companiesToAdd = [com.value for com in companiesToAdd]
        companiesToAdd.extend([com.value for com in companiesSymbolsToAdd])
        companiesToAdd.extend([com.value for com in companiesNamesToAdd])
        #now companiesToAdd contains the companies that need to be added to the DB  IDSymbols

        self.newModelsToSend = self.create_new_models(companiesToAdd, letter)  #convert to the model and then push into the database
        self.nameUpdateModels = self.create_new_models(existingSymbolsNewNames, letter) #update these????
        self.symbolUpdateModels = self.create_new_models(existingNamesNewSymbols, letter) #update these???


    def create_new_models(self, coms, letter):
        newModels = []
        for com in coms:
            model = InsertModel("IDSymbol")
            model.insert("symbol",com.symbol)
            model.insert("name", com.name)
            model.insert("sector", com.sector)
            model.insert("industry", com.industry)
            model.insert("reference", letter)
            newModels.append(model)
        return newModels

    def updateRepos(self):
        self.idRepo._update(self.nameUpdateModels,["name", "sector", "industry", "reference"],"symbol")
        self.idRepo._update(self.symbolUpdateModels, ["symbol", "sector", "industry", "reference"], "name")

    def insertRepos(self):
        self.idRepo.inserting(self.newModelsToSend)

    def getKVPairs(self, info):
        setOfSymbolKV = self.get_symbol_kv(info)
        setOfNameKV = self.get_name_kv(info)
        return setOfSymbolKV, setOfNameKV

    def get_symbol_kv(self, info):
        return self.createKVs(info, lambda x: x.symbol)

    def get_name_kv(self, info):
        return self.createKVs(info, lambda x: x.name)

    def get_company_name_strings(self,companies):
        fields = ["name"]
        companyStrings = getStringModels(companies, fields)
        return companyStrings

    def get_company_symbol_strings(self, companies):
        fields = ["symbols"]
        companyStrings = getStringModels(companies, fields)
        return companyStrings

    def get_new_symbols(self, info, companyStrings):
        symbols = info - companyStrings
        return symbols

    def createUpdateModels(self, entries):
        self.clearModels()
        for e in entries:
            self.addNewEntry(e)
            self.addReferenceModel(e)
            self.addMarketingModel(e)
            self.addCompanyListingModel(e)

    #not sure what we are doing here,  inserting the symbol into SymbolInsert table
    def addNewEntry(self, e):
        model = InsertModel("SymbolInsert")
        model.insert("symbol", e.symbol)
        self.stream.insert(model).queue()

    def addReferenceModel(self, e):
        model = InsertModel("NasdaqListingReference")
        model.insert("symbol", e.symbol)
        model.insert("reference", e.letter)
        self.referenceModels.append(model)

    def addMarketingModel(self, e):
        model = InsertModel("NasdaqCompanyMarketInfo")
        model.insert("symbol", e.symbol)
        model.insert("sector", e.sector)
        model.insert("industry", e.sector)
        self.marketInfoModels.append(model)
        
    def addCompanyListingModel(self, e):
        model = InsertModel("NasdaqCompanyListing")
        model.insert("name", e.name)
        model.insert("symbol", e.symbol)
        self.companyListingModels.append(model)

    def clearModels(self):
        self.referenceModels = []
        self.companyListingModels = []
        self.marketInfoModels = []

    def createKVs(self, info,  func):
        theSet = set()
        for i in info:
            KV = KeyValue.KeyValue(i, func(i))
            theSet.add(KV)
        return theSet
