from .Where import Where

class Delete:
    query = ''
    def __init__(self, mysql):
        self.mysql = mysql

    def delete(self, model):
        self.model = model
        if (model.table != None):
            self.query = "DELETE FROM " + model.table
        else:
            raise Exception("Delete needs a table to delete from")

    def where(self, field, operation, comparator):
        where = Where(self.mysql, self.model);
        where.where(field, operation, comparator, self.query);
        return where

#TODO add this later, when safer
#    def execute(self):
#        self.mysql.execute(self.query)
