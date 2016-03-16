import csv, urllib2, requests,string,os,operator
from stock.common.datastructure import NasdaqCompanyListingContainer

# has Symbol Name  LastSale  MarketCap  ADR TSO   IPOYear  Sector  Industry   SummaryQuote
class NasdaqCompanyListing:
    def __init__(self):
        self.companyListingsDir = "companylistings/"
        self.path = os.path.dirname(os.path.realpath(__file__))+"/"+ self.companyListingsDir
        self.companyFileName = "companyListing-"
        self.listOfInformation=[]

    def _clearInformation(self,clear=True):
        if clear:
            self.listOfInformation=[]

    #the fetch methods fetch information from the website
    def fetchAll(self):
        alphabet=string.uppercase[:]
        for letter in alphabet:
            self.fetch(letter)

    def fetch(self,letter):
        companyListingsURL="http://www.nasdaq.com/screening/companies-by-name.aspx?letter="+letter+"&render=download"
        self._getCompanyListingCSVFile(companyListingsURL,letter)


    #these getCompanyListings fetch or and init the information in the object

    def get(self,letter):
        self._readCSVFile(self._getCompanyFileNameForLetter(letter),letter)

    def getAll(self):
        self.readCompanyListingFiles()

    #the pull methods both fetch and get the requested information
    def pull(self,letter):
        self._clearInformation()
        self.fetch(letter)
        self.get(letter)

    def pullAll(self):
        self.fetchAll()
        self.getAll()

    def getInfo(self):
        #the info is sorted before being passed
        sortedCom=sorted(self.listOfInformation)
        return sortedCom

    #get all access all the files in the companyListing directory only
    def readCompanyListingFiles(self):
        fileList=[f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path,f))]
        #TODO maybe only the files that have companyListings in the name 
        fileList.sort()
        for index,f in enumerate(fileList):
            self._readCSVFile(self.path+f,string.uppercase[index], clear=False)

    #creates the companyListing csv file from the url
    def _getCompanyListingCSVFile(self,URL,letter):
        #TODO  make sure that this does not time out.....
        request=requests.get(URL)
        fileName=self._getCompanyFileNameForLetter(letter)
        self._createCVSFileFromRequest(fileName,request)

    #reads from the selected fileName and then fills the listOfInformation
    def _readCSVFile(self,fileName,letter,clear=True):
        csvFile=open(fileName,'rb')
        reader=csv.reader(csvFile)
        #the first row will give me the headers of the row
        #we will create a dictionary of the list
        headers=self._getHeaders(reader)
        #add the Letter dictionary to the list
        self._clearInformation(clear)
        for index,row in enumerate(reader):
            if (index==0):
                continue
            information={}
            for i,col in enumerate(row):
                information[headers[i]]=col
            information["Letter"] = letter
            com = NasdaqCompanyListingContainer(information)
            self.listOfInformation.append(com)
        csvFile.close()

    #this function fetches the information from the CVS file and puts it into the companyListing directory
    def _createCVSFileFromRequest(self,fileName,request):
        with open(fileName,'wb') as f:
            for chunk in request.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        f.close()

    def _getHeaders(self,reader):
        #just returns the first row of a CSV file  usually the headers
        for row in reader:
            if row[7]=="industry":
                row[7]="Industry"
            if row[5]=="IPOyear":
                row[5]="IPO"
            return row
                

    def _getCompanyFileNameForLetter(self,letter):
        return self.path + self.companyFileName + letter + ".csv"
