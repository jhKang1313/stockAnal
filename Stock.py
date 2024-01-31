import StockBot as sb
import StockAnal as sa
import StockDate as sd
import pandas as pd
from datetime import datetime as dt

FROM_DATE = "20220101"
COUNT = 2

date = sd.StockDate()
latestOpenDate = date.getLatestOpenDateFromToday()
openDate = dt.strftime(latestOpenDate, '%Y%m%d')

bot = sb.StockBot(fromDate = FROM_DATE, toDate = openDate)
anal = sa.StockAnal(bot, openDate)

for id in bot.buyList.index:
  bot.get(id)
# douzoneId = "012510"
bot.getNStock(COUNT)

df_result = pd.DataFrame([])
for id in bot.df.keys():
  anal.setStockInfo(id)
  newRow = anal.getStockInfo()

  df_result = pd.concat([df_result, pd.DataFrame([newRow])], ignore_index=True)

print(df_result.loc[df_result["minDiffRate"] <= 10])
bot.saveToExcel(df_result)

