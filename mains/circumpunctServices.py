from Common.utility.TimeAction import TimeAction
from circumpunct.Processes import runWatchList

def watchList():
    ta = TimeAction(runWatchList,3600)
    while True:
        ta.sleepPerform()
