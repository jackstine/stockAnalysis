class FinancialState:
    quarterly="&data=quarterly"
    endingUrl=""
    time=None

    def __init__(self,quarter=None):
        if quarter=="Q":
            self.urlStamp=self.endingUrl+self.quarterly
        else:
            self.urlStamp=self.endingUrl
        self.time=quarter

    def getURL(self):
        """Returns the urlStamp of the class
        """
        return self.urlStamp

    def getItem(self):
        """Use to create the particular item
        """
        pass

    def insert(self, controller, i):
        """Used to control the controller handling, takes item MYSQL which is
        the mysql handler, and i the item to be passed to the database
        """
        pass
