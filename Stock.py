import StockBot as sb
import StockAnal as sa
from datetime import datetime as dt
import locale as lc

today = dt.strftime(dt.today(), '%Y%m%d')
today = "20240122"
fromDate = "20220101"
bot = sb.StockBot(fromDate = fromDate, toDate = today)
anal = sa.StockAnal(bot, today)

# douzoneId = "012510"
# bot.get(douzoneId)

bot.getTopNKospi(1)

for id in bot.df.keys():
  anal.setStockInfo(id)
  anal.print()
  



