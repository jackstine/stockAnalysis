from . import FinancialState

class BalanceState(FinancialState):
    endingUrl="/financials?query=balance-sheet"

    def getItem(self):
        """returns the valid item of the state:  This case it is a
        BalanceItem
        """
        item=BalanceItem()
        return item

    def insert(self, controller, i):
        """Passes Item i to the mysql query to insert into the database
        for the corresponding table, A for Annual Q for Quarter
        this is for the Balance Sheet
        """
        if(self.time==None or self.time=="A"):
            controller.insertNasdaqAnnualBalanceSheet(i)
        elif(self.time=="Q"):
            controller.insertNasdaqQuarterlyBalanceSheet(i)
