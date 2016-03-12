from ..process.scrape import DailyTimedProcess
import threading

class ScrapingThread:

    def __init__(self):
        self.finance = DailyTimedProcess(DailyTimedProcess.FINANCIAL)
        self.stokcs = DailyTimedProcess(DailyTimedProcess.DAILY_INFO)
        self.daily = DailyTimedProcess(DailyTimedProcess.AMERICAN_STOCKS) 
 
    def run(self):
        threading.Thread(target=)
