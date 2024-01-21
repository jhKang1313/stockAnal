
class StockAnal:    
    def __init__(self, bot, today):
        self.baseCol = "Close"
        self.bot = bot
        self.today = today
    def setStockInfo(self, id):
        self.id = id
        self.stock = self.bot.get(id)
        self.min = self.stock[self.baseCol].min()
        self.minDate = self.stock[self.stock[self.baseCol] == min].index
        self.todayAmt = self.stock.loc[self.today]["Close"]
        self.todayDiffAmt = self.todayAmt - self.min
    def doAnal(self):
        pass
    def print(self, all=False):
        if all == True:
            self.bot.print(self.id)
        print(f"-min : {self.min}")
        print(f"-minDate : {self.minDate}")
        print(f"-todayAmt : {self.todayAmt}")
        print(f"-today Diff Amt : {self.todayDiffAmt}")

        

