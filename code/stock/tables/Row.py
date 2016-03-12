class Row:
    def __init__(self, row, table):
        self.row = row
        self.table = table
        self.model = None

    def setModel(self, model):
        self.model = model

    def get(self, index):
        return self.row[index]
