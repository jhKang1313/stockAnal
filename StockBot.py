import FinanceDataReader as fdr
from datetime import datetime as dt
class StockBot:
  def __init__(self, fromDate = "20220101", toDate = "20231231"):
    self.fdr = fdr
    self.fromDate = fromDate
    self.toDate = toDate
    self.originList = self.fdr.StockListing("KOSPI")
    self.idList = self.originList["Code"]
    self.df = {}
  def get(self, id = "012510"): #default : douzone 
    if self.df.get(id) is None:
      print(f"get {id}")
      self.df[id] = self.fdr.DataReader(id,self.fromDate, self.toDate)
    return self.df[id]
  def getAllKospi(self):
    for idItem in self.idList:
      self.get(idItem)
  def getTop10Kospi(self):
    for i in range(10):
      self.get(self.idList[i])  
  def getTop1Kospi(self):
    self.get(self.idList[0])
  def print(self, id):
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
