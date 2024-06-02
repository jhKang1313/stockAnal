import StockBot as sb
import StockAnal as sa
import StockDate as sd
import pandas as pd
from datetime import datetime as dt

FROM_DATE = "20220101"
COUNT = 200

date = sd.StockDate()
latestOpenDate = date.getLatestOpenDateFromToday()
openDate = dt.strftime(latestOpenDate, '%Y%m%d')

bot = sb.StockBot(fromDate = FROM_DATE, toDate = openDate)
anal = sa.StockAnal(bot, openDate)

print(bot.buyList)

bot.getNStock(COUNT)

df_result = pd.DataFrame([])
for id in bot.df.keys():
  newRow = anal.setStockInfo(id)
  anal.print()
  df_result = pd.concat([df_result, pd.DataFrame([newRow])], ignore_index=True)

#print(df_result)
print(df_result.loc[df_result["minDiffRate"] <= 10])
bot.saveToExcel(df_result)

