class ModelIter:
    def __init__(self, model):
        self.model = model
        self.count = 0

    def reset(self):
        self.count = 0

    def getNext(self, field, value):
        field = self.model.getDictFields()[field]
        rows = self.model.getRows()
        # we need to handle values that have skipped, or have None
        #or whatever
        while(True):
            if(self.count == len(rows)):
                break
            r = rows[self.count]
            if (r[field] == value):
                self.count += 1
                return r
            elif (r[field] > value):
                return None
            self.count += 1

        return None
        

    def getFieldIndex(self, field):
        return self.model.getDictFields()[field]
