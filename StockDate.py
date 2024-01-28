import holidays
from datetime import datetime, timedelta


class StockDate:
  def __init__(self):
    self.holiday = holidays.Korea()

  def getLatestOpenDateFromToday(self):
    today = datetime.today()
    for i in range(100):
      srcDate = today - timedelta(days=i)
      if self.isNormalDate(srcDate):
        return srcDate
    raise ValueError
  def isWeekend(self, date):
    return date.weekday() in [5, 6]

  def isHoliday(self, date):
    return date in self.holiday

  def isNormalDate(self, date):
    return not self.isWeekend(date) and not self.isHoliday(date)
