class MysqlStatement:
    def __init__(self, mysql, model):
        self.query = ""
        self.mysql = mysql
        self.model = model

    def getModel(self):
        return self.mysql.model

    def execute(self):
        print self.query
        return self.mysql.execute(self.query, self.model)

    def queue(self):
        print self.query
        return self.mysql.queue(self.query)

    def __str__(self):
        return "(" + self.query + ")"
