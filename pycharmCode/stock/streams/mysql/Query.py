class Query:
    def __init__(self, db):
        self.db = db
        self.builds = []
        self.tables = []

    def add(self, table):
        D = self.db.describe(table)
        self.builds.append([])
        self.tables.append(table)
        index = len(self.tables) - 1
        for r in D:
            self.builds[index].append(r[0])

    def remove(self, table, field):
        self.builds[self.tables.index(table)].remove(field)

    def build(self):
        string = ""
        for i,t in enumerate(self.tables):
            for f in self.builds[i]:
                string += t + "." + f + ","
        return string[:-1]

    def getFields(self):
        fields = []
        for i,t in enumerate(self.tables):
            for f in self.builds[i]:
                fields.append(f)
        return fields
