
class StockAnal:
    def __init__(self, bot, id, today):
        self.baseCol = "Close"
        self.id = id
        self.bot = bot
        self.stock = self.bot.get(id)
        self.min = self.stock[self.baseCol].min()
        self.minDate = self.stock[self.stock[self.baseCol] == min].index
        self.today = today
        self.todayAmt = self.stock.loc[today]["Close"]
        self.todayDiffAmt = self.todayAmt - self.min
    def print(self):
        self.bot.print(self.id)
        

