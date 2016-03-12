import sys,os
sys.path.insert(1,os.path.expanduser("~") + "/Dropbox/Programs/Stock/code/")
from stock.streams.mysql import DB, Ops
from stock.streams.mysql.connections import Connections
from stock.models import Model

import unittest
from datetime import datetime

class TestDB(unittest.TestCase):
    jacobValues = ( 'jacob', 500L, datetime(2015, 6, 20, 14, 23, 23))
    mattValues = ( 'matt', 300L, datetime(2015, 6, 20, 14, 23, 35))
    momValues = ( 'mom', 200L, datetime(2015, 6, 20, 14, 23, 43))
    dadValues = ("dad", 700L, datetime(2015,07,07,07,07,07))
    dataValues = [jacobValues, mattValues, momValues]
    jacob = {'phone': str(500), 'name':'jacob', 'time': str(datetime(2015, 6, 20, 14, 23, 23))}
    mom = {'phone': str(200), 'name':'mom', 'time': str(datetime(2015, 6, 20, 14, 23, 43))}
    matt = {'phone': str(300), 'name':'matt', 'time': str(datetime(2015, 6, 20, 14, 23, 35))} 
    dad = {"phone":"700", "name":"dad", "time":str(datetime(2015,07,07,07,07,07))}
    testdata = [jacob, matt, mom]
    types = ['varchar(10)', 'int(11)', 'timestamp']
    fields = ['name', 'phone', 'time']
    names = [(jacobValues[0],), (mattValues[0],), (momValues[0],)]
    jacobAddress = ('jacob', 'atlanta')
    mattAddress = ('matt', 'orleans')
    momAddress = ('mom', 'pensacola')
    addressValues = [jacobAddress, mattAddress, momAddress]
    addressTable = [{'name': 'jacob', 'address': 'atlanta'}, {'name': 'matt', 'address': 'orleans'}, {'name': 'mom', 'address': 'pensacola'}]
    leftJoinAddress = [{'name': 'jacob', 'address': 'atlanta'}]
    leftJoinData = [{'phone': str(500), 'name':'jacob', 'time': str(datetime(2015, 6, 20, 14, 23, 23))}]

    def setUp(self):
        self.mysql = DB(Connections.STOCK_TEST)
        self.datatable = Model("datatable")
        self.addressModel = Model("address")

    def tearDown(self):
        self.mysql.close()

    def test_getFields(self):
        fields = self.mysql.getFields(self.datatable.table)
        self.assertEqual(fields, self.fields)

    def test_getTypes(self):
        types = self.mysql.getTypes(self.datatable.table)
        self.assertEqual(types, self.types)

    def test_select_all(self):
        self.mysql.select(self.datatable).execute()
        self.assertEqual(self.datatable.getRows(), self.dataValues)

    def test_select_item(self):
        self.datatable.addField('name')
        self.mysql.select(self.datatable).execute()
        self.assertEqual(self.datatable.getRows(), self.names)

    def test_select_where(self):
        self.mysql.select(self.datatable).where("name", Ops.EQUALS, "jacob").execute()
        self.assertEqual(self.datatable.getRows(), [self.jacobValues])

    def test_zinsert(self):
        self.datatable.addFieldValues(["name", "phone", "time"] 
                                    , ["dad",  "700",   str(datetime(2015,07,07,07,07,07))])
        self.mysql.insert(self.datatable).queue()
        self.mysql.commit()
        table = Model("datatable")
        self.mysql.select(table).where("name", Ops.EQUALS, "dad").execute()
        self.assertEqual(table.getRows(), [self.dadValues])

    def test_zzdelete(self):
        self.mysql.delete(self.datatable).where("name", Ops.EQUALS, "dad").queue()
        self.mysql.commit()
        self.mysql.select(self.datatable).execute()
        self.assertEqual(self.datatable.getRows(), self.dataValues)

    def test_leftjoin(self):
        self.mysql.leftJoin(self.datatable, self.addressModel, "name").execute()
        self.assertEqual(self.datatable.getRows(), self.dataValues)
        self.assertEqual(self.addressModel.getRows(), self.addressValues)

    def test_leftJoinWhere(self):
        self.mysql.leftJoin(self.datatable, self.addressModel, "name").where("phone", Ops.EQUALS, 500).execute() 
        self.assertEqual(self.datatable.getRows(), [self.jacobValues])
        self.assertEqual(self.addressModel.getRows(), [self.jacobAddress])

if __name__ == '__main__':
    unittest.main()
