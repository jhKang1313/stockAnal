import FinanceDataReader as fdr
from datetime import datetime as dt
'''
Stock Bot Class base on FinanceDataReader 
Stock Bot get KOSPI, KOSDAQ Stock Data
'''
class StockBot:
  def __init__(self, fromDate = "20220101", toDate = "20231231"):
    print(f"from : {fromDate}, to : {toDate}")
    self.fdr = fdr
    self.fromDate = fromDate
    self.toDate = toDate
    self.originList = self.fdr.StockListing("KRX")
    self.nameMap = self.originList.loc[:, ["Code", "Name"]].set_index("Code")["Name"].to_dict()
    self.idList = self.originList["Code"]
    self.df = {}
  def get(self, id = "012510"): #default : douzone 
    if self.df.get(id) is None:
      print(f"{self.getName(id)} : {id}")
      self.df[id] = self.fdr.DataReader(id,self.fromDate, self.toDate)
    return self.df[id]
  def getName(self, id):
    return self.nameMap[id]
  def getNStock(self, n = 0):
    idx = n if n != 0 else len(self.idList)
    for i in range(idx):
      self.get(self.idList[i])
  def print(self, id):
    print(self.getName(id))
    print(self.df.get(id))
  def printAll(self):
    for key in self.df.keys():
      self.print(key)
  def saveToExcel(self, df):
    if(df is None):
      print(f"df is None.")
    else :
      nowDate = dt.strftime(dt.now(), '%Y%m%d_%H%M%S')
      df.to_excel(f"{nowDate}_excel_data.xlsx", index = False)
      print("save Excel")
