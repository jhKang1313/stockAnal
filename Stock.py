import StockBot as sb
from datetime import datetime as dt
#print(dir(datetime))
bot = sb.StockBot(fromDate = "20230101", toDate = "20240110")
#bot.getTop10Kospi()
#bot.getTop1Kospi()

stock1 = bot.get("012510")
#bot.print("012510")
#print(stock1.loc["2023-12-04"]["Open"])
# Date -> Index 필드로 지정할 수 있음


#today = dt.strftime(dt.now(), '%Y-%m-%d')
#print(stock1.loc[today]["Close"])

range = 500 #500

for key in stock1.index:
    stock1.loc[key]["Close"]



#print(f"min Close is {stock1['Close'].min()}")


# for key in stock1.index:
#   if minClose == 0 or minClose > stock1.loc[key]['Close']:
#     minClose = stock1.loc[key]['Close']  
# print(f"min Close is {minClose}")




