import locale as lc
from datetime import datetime as dt

FDATE = "%Y%m%d"
class StockAnal:    
    def __init__(self, bot, today):
        self.baseCol = "Close"
        self.bot = bot
        self.today = today
        self.id = None
        lc.setlocale(lc.LC_NUMERIC, 'en_US.UTF-8')
    def setStockInfo(self, id):
        self.id = id
        self.stock = self.bot.get(id)
        self.minRow = self.stock.loc[self.stock[self.baseCol].idxmin()]
        self.min = self.minRow[self.baseCol]
        self.minDate = self.minRow.name
        self.minDateStr = self.minDate.strftime(FDATE)
        self.todayAmt = self.stock.loc[self.today][self.baseCol]
        self.todayDiffAmt = self.todayAmt - self.min
        self.todayDiffDays = (dt.strptime(self.today, FDATE) - self.minDate).days
    def doAnal(self):
        pass
    def print(self, all=False):
        if all == True:
            self.bot.print(self.id)
        print(f"-min : {self.doLocale(self.min)}")
        print(f"-minDate : {self.minDateStr}")
        print(f"-todayAmt : {self.doLocale(self.todayAmt)}")
        print(f"-today Diff Amt : {self.doLocale(self.todayDiffAmt)}")
        print(f"-today Diff Days : {self.todayDiffDays}")
    def doLocale(self, num):
        return lc.format_string('%d', num, grouping=True)
        

