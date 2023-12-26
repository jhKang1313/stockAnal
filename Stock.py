import FinanceDataReader as fdr

class StockBot:
  def __init__(self, fromDate = "20220101", toDate = "20231231"):
    self.fdr = fdr
    self.fromDate = fromDate
    self.toDate = toDate
    self.idList = self.fdr.StockListing("KOSPI")["Code"]
    self.df = {}
  def get(self, id = "012510"):
    if self.df.get(id) is None:
      print(f"get {id}")
      self.df[id] = self.fdr.DataReader(id,self.fromDate, self.toDate)
    return self.df[id]


bot = StockBot()
print(bot.get("012510"))

print(bot.get("012510"))
# bot.get()




# idList = kospiDF["Code"]
#
# def getStock(id, fromDate = "20220101", toDate = "20231231"):
#   return fdr.DataReader(id, fromDate, toDate)
#
# for idItem in idList:
#   print(getStock(idItem))
#   break




# print(df_krx["Code"])

# print(type(df_krx));
# df_dz = fdr.DataReader('012510', '2023-11-01', '2023-11-30')
# print(df_dz)
# print(len(df_dz))
#
# df = fdr.DataReader('KRX:000150', '2020-01-01')
# print(df)
#
#
# stock = fdr.StockListing('KRX')
# print(stock)


