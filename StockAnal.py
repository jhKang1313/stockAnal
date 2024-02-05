from datetime import datetime as dt

FDATE = "%Y%m%d"
BASE_COL = "Close"
CRITI_RATE = 5

class StockAnal:
  def __init__(self, bot, today):
    self.bot = bot
    self.today = today
    self.stockInfo = None

  def setStockInfo(self, id):
    stock = self.bot.get(id)
    minRow = stock.loc[stock[BASE_COL].idxmin()]
    min = minRow[BASE_COL]
    minDate = minRow.name
    minDateStr = minDate.strftime(FDATE)

    maxRow = stock.loc[stock[BASE_COL].idxmax()]
    max = maxRow[BASE_COL]
    maxDate = maxRow.name
    maxDateStr = maxDate.strftime(FDATE)

    todayAmt = stock.loc[self.today][BASE_COL]
    todayMinDiffAmt = todayAmt - min
    todayMinDiffDays = (dt.strptime(self.today, FDATE) - minDate).days
    todayMinDiffRate = (todayMinDiffAmt / todayAmt) * 100
    isGoodFlag = todayMinDiffRate <= CRITI_RATE

    buyDate = None
    buyAmount = None
    buyDiffAmt = None
    if id in self.bot.buyList.index:
      buyRow = self.bot.buyList.loc[id]
      buyDate = buyRow["buyDate"]
      buyAmount = buyRow["buyAmount"]
      buyDiffAmt = todayAmt - buyRow["buyAmount"]
    
    self.stockInfo = {
      'id' : id,
      'name' : self.bot.getName(id),
      'minDate' : minDateStr,
      'min' : min,
      'maxDate' : maxDateStr,
      'max' : max,
      'today' : self.today,
      'todayAmt' : todayAmt,
      'minDiffAmt': todayMinDiffAmt,
      'minDiffDays' : todayMinDiffDays,
      'minDiffRate' : todayMinDiffRate,
      'buyDate' : buyDate,
      'buyAmount' : buyAmount,
      'buyDiffAmt' : buyDiffAmt
    }

    return self.stockInfo
  
  def doAnal(self):
    if self.isGoodFlag == False:
      return
    # Type.1 산형태. 올라갔다 내려가는중...
  def print(self, all=False):
    if all == True:
      self.bot.print(self.stockInfo.id)
    print(f"{self.stockInfo['id']} : {self.bot.getName(self.stockInfo['id'])}")
    print(f"-min : {self.doLocale(self.stockInfo['min'])}")
    print(f"-minDate : {self.stockInfo['minDate']}")
    print(f"-max : {self.doLocale(self.stockInfo['max'])}")
    print(f"-maxDate : {self.stockInfo['maxDate']}")
    print(f"-todayAmt : {self.doLocale(self.stockInfo['todayAmt'])}")
    print(f"-today Diff Amt : {self.doLocale(self.stockInfo['minDiffAmt'])}")
    print(f"-today Diff Days : {self.stockInfo['minDiffDays']}")
    print(f"-today Diff Rate : {self.stockInfo['minDiffRate']}")
    if self.stockInfo['minDiffRate'] < CRITI_RATE:
      print(f"is Good?")
    print("-----------------------------")

  def doLocale(self, num):
    return "{:,}".format(num)
  