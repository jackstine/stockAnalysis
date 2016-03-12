import sys, os
sys.path.insert(1,os.path.expanduser("~") + "/Dropbox/Programs/Stock/code/")
from stock.tables import DataPool
from stock.streams.mysql import DB

dp = DataPool(DB(DB.Connections.STOCK))


