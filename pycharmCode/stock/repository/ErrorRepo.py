from pycharmCode.stock.repository import Repo
from pycharmCode.stock.streams.mysql import DB
import os, sys

class ErrorRepo:
    def __init__(self):
        self.db = DB(DB.Connections.STOCK)

    def insert(self, m):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        m.insert("lineNumber", str(exc_tb.tb_lineno))
        m.insert("fileName", fname)
        self.db.insert(m).queue() 

    def close(self):
        self.db.commit()
        self.db.close()
