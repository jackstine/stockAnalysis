from datetime import *
from time import *
from calendar import *


SUNDAY = 6
SECONDS_IN_DAY = 86400

def now():
    return datetime.utcnow()

def todaysTime():
    now = now()
    return timedelta(hours = now.hour, minutes = now.minute, seconds = now.seconds)

def isWeekDay(day = None):
    if day == None:
        today = date.today()
    else:
        today = day
    return (today.weekday() == 6 or today.weekday() == 5)
        

def timeTillMonday():
    now = datetime.utcnow()
    daysTillSunday = SUNDAY - now.date().weekday()
    secondsLeftInDay = timeTillEndOfDay()
    return secondsLeftInDay + secondsInDay(daysTillSunday)


def timeTillEndOfDay():
    """ returns the time remaining till tomorrow UTC 0:00:0000..."""
    to = convertDateToDateTime(tomorrow())
    timeLeft = to - datetime.utcnow()
    return timeLeft.seconds
    
def timeTillEndOfWeekend(t = None):
    """ returns the time remaining till Monday UTC 0:00:000...."""
    if (t == None):
        return timeTillMonday()
    else:
        return timeTillMonday() + t.seconds

def timeTillNext(t):
    """ t must be timedelta and only caculates hours, minutes, seconds"""
    todaysTime = todaysTime()
    if (t > todaysTime):
        return t.seconds - todaysTime.seconds
    else:
        return timeTillEndOfDay + t.seconds

def sleepUntilEndOfWeekend(t = None):
    sleep(timeTillEndOfWeekend(t))

def sleepUntilNextTime(t = None):
    sleep(timeTillNext(t))

def sleepWeekendOrUntil(t, lastDay):
    if (isWeekDay(lastDay)):
        sleepUntilEndOfWeekend(t)
    elif (isFriday(lastDay)):
        sleepUntilEndOfWeekend(t)
    else:
        sleepUntilNextTime(t)

def isFriday(t):
    return t.weekday() == 4

def convertDateToDateTime(date):
    return datetime(year = date.year, month = date.month, day = date.day)

def secondsInDay(days):
    return days * SECONDS_IN_DAY

def today():
    return date.today()

def tomorrow():
    return date.today() + timedelta(days = 1)

def oneDay():
    return timedelta(days = 1)

def convertSQLStringDate(string):
    return datetime.strptime(string, "%Y-%m-%d").date()

def addYears(d, years):
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

def subYears(d, years):
    try:
        return d.replace(year = d.year - years)
    except ValueError:
        return d + (date(d.year - years, 1, 1) - date(d.year, 1, 1))

def aQuarterAgo():
    return date.today() - timedelta(days = 90)

def halfAYearAgo():
    return date.today() - timedelta(days = 180)

def aYearAgo():
    return subYears(date.today(),1)

def threeYearsAgo():
    return subYears(date.today(),3)

def fiveYearsAgo():
    return subYears(date.today(),5)

def tenYearsAgo():
    return subYears(date.today(),10)

def twentyYearsAgo():
    return subYears(date.today(),20)

def thirtyYearsAgo():
    return subYears(date.today(),30)

def addDays(tTime, number):
    return tTime + timedelta(days = number)

def getSecondsFrom(tTime):
    return (tTime - now).total_seconds()

def addSeconds(tTime, number):
    return tTime + timedelta(seconds=number)

def isAfter_mill(tTime, seconds):
    return addSeconds(tTime, seconds) < now()

class t(timedelta):
    def __init__(self, **kwargs):
        timedelta.__init__(self, **kwargs)