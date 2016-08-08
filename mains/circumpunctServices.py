from Common.utility.TimeAction import TimeAction
from circumpunct.Processes import runWatchList

def watchList():
    ta = TimeAction(runWatchList,3600)
    while True:
        ta.sleepPerform()


#response.xpath("//div[@class='genTable']/table/tr/th/a/text()").extract()
#response.xpath("//div[@class='genTable']/table/tr/td/text()").extract()
#response.xpath("//ul[@class='pager']/li/a/text()").extract()