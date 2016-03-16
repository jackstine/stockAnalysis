from . import FinancialState

class IncomeState(FinancialState):
    endingUrl="/financials?query=income-statement"

    def getItem(self):
        """returns the valid item of the state:  This case it is a
        IncomeItem
        """
        item=IncomeItem()
        return item

    def insert(self, controller, i):
        """Passes Item i to the controllerquery to insert into the database
        for the corresponding table, A for Annual Q for Quarter
        this is for the Income Statements
        """
        if(self.time==None or self.time=="A"):
            controller.insertNasdaqAnnualIncomeStatement(i)
        elif(self.time=="Q"):
            controller.insertNasdaqQuarterlyIncomeStatement(i)
