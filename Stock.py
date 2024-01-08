import StockBot as sb

#print(dir(datetime))
bot = sb.StockBot(fromDate = "20230101", toDate = "20231231")
#bot.getTop10Kospi()
bot.getTop1Kospi()

stock1 = bot.get("005930")
bot.print("005930")
#print(stock1.loc["2023-12-04"]["Open"])
# Date -> Index 필드로 지정할 수 있음
minClose = 0

print(f"min Close is {stock1['Close'].min()}")
# for key in stock1.index:
#   if minClose == 0 or minClose > stock1.loc[key]['Close']:
#     minClose = stock1.loc[key]['Close']  
# print(f"min Close is {minClose}")




