from ...scrape.nasdaq import NasdaqCompanyListing
from ...models import Model
import string
from ...models.ModelAlgorithms import getStringModels
from ...repository.nasdaq import NasdaqReferenceRepository, NasdaqMarketInfoRepository, NasdaqCompanyListingRepository
from ...models import InsertModel

class NasdaqCompanyListingController:

    def __init__(self, stream):
        self.stream = stream
        self.scrape = NasdaqCompanyListing()
        self.reference = NasdaqReferenceRepository()
        self.marketInfo = NasdaqMarketInfoRepository()
        self.companyListingRepo = NasdaqCompanyListingRepository()
        self.clearModels()

    def run(self):
        for letter in string.uppercase[:]:
            self.scrape.pull(letter)
            self.filterData(self.scrape.listOfInformation, letter)
            self.updateRepos()
            self.insertRepos()
            self.stream.commit();

    def filterData(self, info, letter):
        newEntries = self.getNewEntries(info, letter)
        print newEntries
        self.createUpdateModels(newEntries)

    def updateRepos(self):
        self.reference.updateLetterIfIn(self.referenceModels , self.stream)
        self.marketInfo.updateIfIn(self.marketInfoModels, self.stream)
        self._updateCompanyNames()

    def _updateCompanyNames(self):
        companyListingFields = ["name"]
        self.companyListingRepo.updateIfIn(self.companyListingModels, self.stream, companyListingFields)

    def insertRepos(self):
        self.reference.insertIfNotIn(self.referenceModels, self.stream)
        self.companyListingRepo.insertIfNotIn(self.companyListingModels, self.stream)
        self.marketInfo.insertIfNotIn(self.marketInfoModels, self.stream)

    def getNewEntries(self, info, letter):
        setOfAssociations = self.createAssociations(info)
        #TODO propably should be the entire list of companies
        #what happens if the letter reference changes for a symbol??  Explosion
        companiesFromDB = self.reference.select(letter, self.stream)
        fields = ["symbol"]
        companyStrings = getStringModels(companiesFromDB, fields)
        return setOfAssociations - companyStrings

    def createUpdateModels(self, entries):
        self.clearModels()
        for e in entries:
            self.addNewEntry(e)
            self.addReferenceModel(e)
            self.addMarketingModel(e)
            self.addCompanyListingModel(e)

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

    def createAssociations(self, info):
        theSet = set()
        for i in info:
            i.setAssociation(i.symbol)
            theSet.add(i)
        return theSet
