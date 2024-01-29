from datetime import datetime as dt

FDATE = "%Y%m%d"
BASE_COL = "Close"
CRITI_RATE = 5

class StockAnal:
  def __init__(self, bot, today):
    self.minRow = None
    self.stock = None
    self.todayMinDiffAmt = None
    self.bot = bot
    self.today = today
    self.id = None

  def setStockInfo(self, id):
    self.id = id
    self.stock = self.bot.get(id)
    self.minRow = self.stock.loc[self.stock[BASE_COL].idxmin()]
    self.min = self.minRow[BASE_COL]
    self.minDate = self.minRow.name
    self.minDateStr = self.minDate.strftime(FDATE)

    self.maxRow = self.stock.loc[self.stock[BASE_COL].idxmax()]
    self.max = self.maxRow[BASE_COL]
    self.maxDate = self.maxRow.name
    self.maxDateStr = self.maxDate.strftime(FDATE)

    self.todayAmt = self.stock.loc[self.today][BASE_COL]
    self.todayMinDiffAmt = self.todayAmt - self.min
    self.todayMinDiffDays = (dt.strptime(self.today, FDATE) - self.minDate).days
    self.todayMinDiffRate = (self.todayMinDiffAmt / self.todayAmt) * 100
    self.isGoodFlag = self.todayMinDiffRate <= CRITI_RATE

    self.buyDate = None
    self.buyAmount = None
    if id in self.bot.buyList.index:
      buyRow = self.bot.buyList.loc[id]
      self.buyDate = buyRow["buyDate"]
      self.buyAmount = buyRow["buyAmount"]
  def getStockInfo(self):
    return {
      'id' : self.id,
      'name' : self.bot.getName(self.id),
      'minDate' : self.minDateStr,
      'min' : self.min,
      'maxDate' : self.maxDateStr,
      'max' : self.max,
      'today' : self.today,
      'minDiffAmt': self.todayMinDiffAmt,
      'minDiffDays' : self.todayMinDiffDays,
      'minDiffRate' : self.todayMinDiffRate,
      'buyDate' : self.buyDate,
      'buyAmount' : self.buyAmount
    }
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
    if self.todayMinDiffRate < CRITI_RATE:
      print(f"is Good?")
    print("-----------------------------")

  def doLocale(self, num):
    return "{:,}".format(num)
