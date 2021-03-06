class CompanyContainer:
    """If these are compared with any operator,the highest alphaNumeric 
    value is greater than the lowest alphaNumeric value of first the name
    and second the symbol
    """
    symbol=""
    name=""

    def __init__(self,symbol,name,data):
        self.symbol=symbol
        self.name=name
        self.data=data

    def __eq__(self,data):
        if(self.name==data.name and self.symbol==data.symbol):
            return True
        else:
            return False

    def __le__(self,other):
        if(self==other):
            return True
        elif(self<other):
            return True
        else:
            return False

    def __ne__(self,other):
        return not self==other

    def __gt__(self,data):
        print data
        print data.name
        if(self.name>data.name):
            return True
        elif (self.name<data.name):
            return False
        else:	#they are equal
            return self.symbol>data.symbol

    def __cmp__(self,other):
        if(self<other):
            return -1
        elif(self==other):
            return 0
        elif(self>other):
            return 1

    def __getitem__(self,key):
        if(key==0):
            return self.symbol
        if(key==1):
            return self.name
        if(key==2):
            return self.data

    def __ge__(self,other):
        if(self==other):
            return True
        elif(self>other):
            return True
        else:
            return False

    def __lt__(self,data):
        if(self.name < data.name):
            return True
        elif(self.name > data.name):
            return False
        else:	#they are equal
            return self.symbol < data.symbol
