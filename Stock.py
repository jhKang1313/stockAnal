import StockBot as sb

#print(dir(datetime))
bot = sb.StockBot(fromDate = "20231201", toDate = "20231231")
#bot.getTop10Kospi()
bot.getTop1Kospi()

stock1 = bot.get("005930")
bot.saveToExcel(stock1)

#Test
#아안녕하세요
#ㄴㅇㅁㄴㅇㅁㄴ