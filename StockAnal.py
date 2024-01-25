from datetime import datetime as dt

FDATE = "%Y%m%d"

class StockAnal:
  def __init__(self, bot, today):
    self.minRow = None
    self.stock = None
    self.todayMinDiffAmt = None
    self.baseCol = "Close"
    self.bot = bot
    self.today = today
    self.id = None
    self.CRITICAL_RATE = 5  
    
  def setStockInfo(self, id):
    self.id = id
    self.stock = self.bot.get(id)
    self.minRow = self.stock.loc[self.stock[self.baseCol].idxmin()]
    self.min = self.minRow[self.baseCol]
    self.minDate = self.minRow.name
    self.minDateStr = self.minDate.strftime(FDATE)

    self.maxRow = self.stock.loc[self.stock[self.baseCol].idxmax()]
    self.max = self.maxRow[self.baseCol]
    self.maxDate = self.maxRow.name
    self.maxDateStr = self.maxDate.strftime(FDATE)

    self.todayAmt = self.stock.loc[self.today][self.baseCol]
    self.todayMinDiffAmt = self.todayAmt - self.min
    self.todayMinDiffDays = (dt.strptime(self.today, FDATE) - self.minDate).days
    self.todayMinDiffRate = (self.todayMinDiffAmt / self.todayAmt) * 100
    self.isGoodFlag = self.todayMinDiffRate <= self.CRITICAL_RATE
  def doAnal(self):
    if self.isGoodFlag == False:
      return
    # Type.1 산형태. 올라갔다 내려가는중...


  def print(self, all=False):
    if all == True:
      self.bot.print(self.id)
    print(f"{self.id} : {self.bot.getName(self.id)}")
    print(f"-min : {self.doLocale(self.min)}")
    print(f"-minDate : {self.minDateStr}")
    print(f"-max : {self.doLocale(self.max)}")
    print(f"-maxDate : {self.maxDateStr}")
    print(f"-todayAmt : {self.doLocale(self.todayAmt)}")
    print(f"-today Diff Amt : {self.doLocale(self.todayMinDiffAmt)}")
    print(f"-today Diff Days : {self.todayMinDiffDays}")
    print(f"-today Diff Rate : {self.todayMinDiffRate}")
    if self.todayMinDiffRate < 5:
      print(f"is Good?")
    print("-----------------------------")

  def doLocale(self, num):
    return "{:,}".format(num)
