from . import FinancialState

class CashState(FinancialState):
        endingUrl="/financials?query=cash-flow"

        def getItem(self):
                """returns the valid item of the state:  This case it is a
                CashItem
                """
                item=CashItem()
		return item

        def insert(self, controller, i):
                """Passes Item i to the mysql query to insert into the database
                for the corresponding table, A for Annual Q for Quarter
                this is for the Cash Flow Statements
                """
                if(self.time==None or self.time=="A"):
                        controller.insertNasdaqAnnualCashFlow(i)
                elif(self.time=="Q"):
                        controller.insertNasdaqQuarterlyCashFlow(i)


