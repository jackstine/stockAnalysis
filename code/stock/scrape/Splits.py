import urllib2
import time, datetime
from scrapy.selector import Selector
from ..models import InsertModel

class Splits:
    def __init__(self):
        pass

    def run(self):
        html = urllib2.urlopen("http://getsplithistory.com/AA").read()
        response = Selector(text = html, type = "html")
        datesAndOther = response.xpath("//table/tbody/tr/td/text()").extract()
        ratios = response.xpath("//table/tbody/tr/td/span/text()").extract()
        objects = []
        rs = []
        for i,data in enumerate(datesAndOther[:-1]):
            if (i % 4 == 0):
                objNum = len(objects)
                objects.append(dict())
                objects[objNum]["date"] = self.cleanDate(data)
            if ((i - 1) % 4 == 0):
                objNum = len(objects) - 1
                objects[objNum]["denom"] = self.cleanDenom(data)
        for i,data in enumerate(ratios[:-1]):
            if (i % 3 == 0):
                objects[i/3]["num"] = self.cleanNum(data)
        for o in objects:
            o["factorial"] = float(o["num"]) / float(o["denom"])
        # now we insert the date symbol name and the factorial into the DB
        for o in objects:
            IM = InsertModel("jdfkasdklfj")#tableName)
            IM.insert("e", o["date"])
            IM.insert("symbol", symbol)
            IM.insert("Ratio", o["factorial"])

    def cleanDate(self, date):
        t = time.strptime(date, '%b %d, %Y')
        date = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
        return date

    def cleanDenom(self, data):
        data = int(data.split(" : ")[1])
        return data

    def cleanNum(self, num):
        num = int(num)
        return num
