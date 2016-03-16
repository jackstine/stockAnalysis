import string

class Filter:

    def mushList(self, l):
        newList = []
        for item in l:
            newList.append(self.mushString(item))
        return newList

    def mushString(self, string):
        newString = ""
        for c in string:
            if (c == " "):
                continue
            newString += c
        return newString


    def filterListedData(self,data):
        """Use this to fix the data to a more readable, and database friendly format
        """
        #get the right data
        returnData=""
        if(len(data)>0):
                returnData=data[0]
        else:
                returnData=data

        #if the data is a texData then just return it, else filter
        if (self.isTextInfo(returnData)):
                return returnData
        #filter the data
        charactersToFilter="$ %,"
        newHeader=''.join(c for c in returnData if c not in charactersToFilter)
        return newHeader

    def getZero(self,data):
        if (len(data)==1):
            if(data[0]=='-'):
                return "0"
        return data

    def convertDashesToZero(self, data):
        if ("--" in data):
            return "0"
        else:
            return data

    def fixNumber(self, data):
        if (type(data) is str or data[0] == "-"):
            return "0"
        else:
            newData = self.convertToNeg(data)
            if (type(newData) is unicode):
                return newData
            else:
                return str(newData)

    def isTextInfo(self,data):
        """If there is a Uppercase character in the data
        then it must be a Tex based data
        """
        for c in string.uppercase:
            if (c in data):
                return True
        return False

    def filterHeader(self,header):
        """This is used to filter the header for the Fields in the Scrapy Items
        """
        if (len(header)==1):    #for some discrepancies it will come as a list,  need to shorten it to a string
            header=header[0]
        charactersToFilter="\n&()'`1234567890 /.:,-"
        newHeader=''.join(c for c in header if c not in charactersToFilter)
        return newHeader

    def filterNewLine(self,header):
        """This filters the new lines from the string
        """
        if (len(header)==1):    #for some discrepancies it will come as a list,  need to shorten it to a string
            header=header[0]
        charactersToFilter="\n\t"
        newHeader=''.join(c for c in header if c not in charactersToFilter)
        return newHeader

    def filterNonListedData(self,data):
        #filter the data
        charactersToFilter="$ %,\n/"
        newHeader=''.join(c for c in data if c not in charactersToFilter)
        return newHeader

    def fixListedData(self,data):
        """Use this to fix the data to a more readable, and database friendly format
        """
        #get the right data
        returnData=""
        if(len(data)>0):
            returnData=data[0]
        else:
            returnData=data

        #if the data is a texData then just return it, else filter
        if (self.isTextInfo(returnData)):
            return returnData
        #filter the data
        charactersToFilter="$ %,"
        newHeader=''.join(c for c in returnData if c not in charactersToFilter)
        return newHeader

    def headerFilter(self,header):
        """This is used to filter the header for the Fields in the Scrapy Items
        """
        if (len(header)==1):    #for some discrepancies it will come as a list,  need to shorten it to a string
            header=header[0]
        charactersToFilter="()'`1234567890 /.:,-"
        newHeader=''.join(c for c in header if c not in charactersToFilter)
        return newHeader

    def convertToNeg(self,num):
        """converts Parenthetical to negative
        """
        if (num[0]=="("):
            newNum=num[1:(len(num)-1)]
            return int(newNum)*-1
        else:
            return num

    def convertDate(self, date):
        if (len(date.split()) == 0):
            return None
        endOfMonth = date.find("/")
        endOfDays = date.find("/", endOfMonth + 1)
        dateString = date[endOfDays+1:] + "-"
        if (len(date[:endOfMonth]) == 1):
            dateString += "0" 
        dateString += date[:endOfMonth]  + "-" 
        if (len(date[endOfMonth+1: endOfDays]) == 1):
            dateString += "0"
        dateString += date[endOfMonth+1: endOfDays]
        return dateString

    def fixNonListedData(self,data):
        #filter the data
        charactersToFilter="$ %,"
        newHeader=''.join(c for c in data if c not in charactersToFilter)
        for char in newHeader:
            print char
        return newHeader

    def filterForSQL(self,data):
        charactersToFilter="'\""
        newHeader=''.join(c for c in data if c not in charactersToFilter)
        return newHeader

    def isNumber(self, number):
        returnNumber = self.filterNonListedData(number)
        try :
            returnNumber = float(returnNumber)
            return True
        except Exception:
            return False

    
