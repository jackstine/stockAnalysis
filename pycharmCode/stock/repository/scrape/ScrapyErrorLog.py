from Common.utility import Filter
from pycharmCode.stock.repository import ErrorRepo
from pycharmCode.stock.streams.models import InsertModel


class ScrapyErrorLog(ErrorRepo):
    table = "ScrapyErrorLog"

    def __init__(self):
        ErrorRepo.__init__(self)
        self.f = Filter()

    def log(self, response, error, scrape):
        m = InsertModel(self.table)
        m.insert("url", response.url)
        m.insert("error", self.f.filterForSQL(str(error)))
        m.insert("scrape", scrape)
        self.insert(m)
