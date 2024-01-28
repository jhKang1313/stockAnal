import StockBot as sb
import StockAnal as sa
import StockDate as sd
from datetime import datetime as dt

date = sd.StockDate()
latestOpenDate = date.getLatestOpenDateFromToday()
openDate = dt.strftime(latestOpenDate, '%Y%m%d')

fromDate = "20220101"
bot = sb.StockBot(fromDate = fromDate, toDate = openDate)
anal = sa.StockAnal(bot, openDate)
  
# douzoneId = "012510"
# bot.get(douzoneId)
bot.getNStock(1)

for id in bot.df.keys():
  anal.setStockInfo(id)
  anal.print()
  row = anal.getStockInfo()
  print(row)
