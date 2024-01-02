import StockBot as sb

#print(dir(datetime))
bot = sb.StockBot(fromDate = "20231201", toDate = "20231231")
#bot.getTop10Kospi()
bot.getTop1Kospi()

stock1 = bot.get("005930")

print(stock1.loc["2023-12-04"]["Open"])
# Date -> Index 필드로 지정할 수 있음
print(stock1.index)

