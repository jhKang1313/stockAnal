import StockBot as sb
from datetime import datetime as dt
import StockAnal as sa

today = dt.strftime(dt.today(), '%Y%m%d')
fromDate = "20220101"
bot = sb.StockBot(fromDate = fromDate, toDate = today)

stock1 = bot.get("012510")
#bot.print("012510")
#print(stock1.loc["2023-12-04"]["Open"])
# Date -> Index 필드로 지정할 수 있음


for id in bot.df.keys():
  tt = sa.StockAnal(bot, id, today)
  tt.print()
  
  
  

#today = dt.strftime(dt.now(), '%Y-%m-%d')
#print(stock1.loc[today]["Close"])

#for key in stock1.index:



#print(f"min Close is {stock1['Close'].min()}")


# for key in stock1.index:
#   if minClose == 0 or minClose > stock1.loc[key]['Close']:
#     minClose = stock1.loc[key]['Close']  
# print(f"min Close is {minClose}")




