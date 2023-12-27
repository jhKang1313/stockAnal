import FinanceDataReader as fdr

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
      break
  def print(self, id):
    print(self.df.get(id))
  def printAll(self):
    for key in self.df.keys():
      self.print(key)