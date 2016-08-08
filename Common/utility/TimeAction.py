from time import sleep

from Common.utility import now,isAfter_mill, addSeconds


class TimeAction():
    def __init__(self, action, seconds):
        self.timeInSeconds = seconds
        self.action = action
        self.lastTimeAction = addSeconds(now(),-1 * seconds)

    def isTime(self):
        if (isAfter_mill(self.lastTimeAction, self.timeInSeconds)):
            return True
        else:
            return False

    def perform(self):
        if (self.isTime()):
            self.action()
            self.lastTimeAction = now()

    def getTimeLeft(self):
        return (addSeconds(self.lastTimeAction, self.timeInSeconds) - now()).total_seconds()

    def sleepTill(self):
        seconds = self.getTimeLeft()
        if (seconds > 0):
            sleep(int(seconds))

    def sleepPerform(self):
        self.sleepTill()
        self.perform()

