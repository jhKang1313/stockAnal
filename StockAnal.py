
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
    def print(self):
        self.bot.print(self.id)
        

