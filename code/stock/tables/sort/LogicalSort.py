from ..Collection import Collection

class LogicalSort:

    def __init__(self, description):
        self.desc = False
        self.description = description
        self._setSortFunction()

    def _setSortFunction(self):
        primaryKeys = self.description.getPrimaryKeys()
        if (primaryKeys != []):
            pass
        else :
            multiKeys = self.description.getMultiKeys()
            sortFunction = self.getSortFromMultiKey(multiKeys)


    def getSortFromMultiKey(self, multiKeys):
        #because we dont have much to do yet, we are going to begin with only
        #sorting of Dates   GroupBy other ORderBy Date
        if (len(multiKeys) > 2):
            raise Exception("there are more than 2 MultiKeys,  please update the Logical Sorting to Handle this")
        date, i = self.findDate(multiKeys)
        other = multiKeys[i - 1]
        self.groupBy = [other.field(), date.field()]    #OrderBy here takes 2 arguments to Order BY
        self.setDesc() # set DESC cause we want the highest date first

    #this method should probably be in a seperate class, that takes in the rows, fields, and LogicalSort, and table

def buildCollections(rows, fields, table):
    fieldIndex = 0
    sortedValue = rows[0][fieldIndex]
    rowsForCollection = []
    for r in rows:
        if (sortedValue != r[fieldIndex]):
            sortedValue = r[fieldIndex]
            c = Collection(table, rowsForCollection)
            rowsForCollection = []
            rowsForCollection.append(self.typeify(r))
            yield c
        else:
            rowsForCollection.append(self.typeify(r))

def typeify(row):
    for i,r in enumerate(row):
        if (self.description.isInteger(i)):
            row[i] = self.convertInt(r)
        elif (self.description.isDate(i)):
            row[i] = r #TODO dont know the correct convertion
        elif (self.description.isTimeStamp(i)):
            row[i] = r  #TODO dont know the correct convertion
        elif (self.description.isDecimal(i)):
            row[i] = self.convertFloat(r)
        #else it is a String which it already is
    return row

def convertFloat(self, value):
    #NOTE default None value is 0
    if (value != "None"):
        return float(value)
    else:
        return 0

def convertInt(self, value):
    #NOTE default None value is 0
    if (value != "None"):
        return int(value)
    else:
        return 0
        

def findDate(self, keys):
    for i,m in enumerate(keys):
        if (m.isDate()):
            return m, i

def setDesc(self):
    self.desc = True


#TODO but thisd in a algorithms file full of methods
def getFieldIndex(fields, fieldName):
    for i,f in enumerate(fields):
        if (f.getName()== fieldName):
            return i
