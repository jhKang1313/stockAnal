import FinanceDataReader as fdr

# df_krx = fdr.StockListing('KRX')
# print(df_krx);

#df_douzone = fdr.DataReader('012510', '2023-10-20', '2023-10-30')
#
# (name, age, hobby) = ("Kang", 33, "Running") # make tuple
# print(name, age, hobby)
#
# name = "Park"
# print(name)
#
# name = "Kang"
# if name == "Kang":
# 	print("He is {}".format(name))
#
# list = range(1, 4)
# for item in list:
# 	print(item)
#
#
# index = 5
# while index != 0:
#     print("index is {0}".format(index))
#     index -= 1
#
# list = [1, 2, 3, 4, 5]
# list100 = [i + 100 for i in list]
# print(list100)
#
#
# def funcName(param, defaultParam = 100):
# 	return param + defaultParam
#
# print(funcName(200)) # expect return 300
#
# def funcName(param, defaultParam = 100):
# 	return param + (defaultParam * 2)
#
# print(funcName(param = 200, defaultParam = 50)) # expect return 300
#
#
# def funcName(param, *varParam):
# 	print("Param = {0}, varParam = {1}".format(param, varParam))
# funcName("Test", ["Kang", "Park", "Lee"])


# scoreFile = open("newFile.txt", "w", encoding='utf-8')
# print("Math = 80", file = scoreFile)
# print("Science = 40", file = scoreFile)
# scoreFile.write("English = 50\n")
# scoreFile.write("Pysic = 10")
# scoreFile.close()
#
# scoreFile = open("newFile.txt", "r", encoding='utf-8')
# #print(scoreFile.read()) # read all content
# while True:
#     line = scoreFile.readline() # read one line
#     if not line :
#         scoreFile.close()
#         break
#     print(line)
# scoreFile.readlines() # read line as list type

# import pickle
# with open("profile_file.pickle", "rb") as profileFile:
#     print(pickle.load(profileFile))
# profileFile = open("profile_file.pickle", "wb")
# profile = {"Name" : "kjh", "Age" : 33, "Hobby" : ["Running", "Recording", "Riding"]}
# pickle.dump(profile, profileFile);
# profileFile.close();
#
# profileFile = open("profile_file.pickle", "rb")
# profile = pickle.load(profileFile);
# print(profile)
# profileFile.close()

import inspect
import random

print(inspect.getfile(random))
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
class AttackUnit(Unit):
    def __init__(self, name, hp, dem):
        Unit.__init__(self, name, hp)
        self.dem = dem
    def attack(self, direction):
        print("{0} : {1} 방향에 {2} 데미지로 공격합니다.".format(self.name, direction, self.dem))

class Flyable:
  def __init__(self, speed):
    self.speed = speed
  def flying(self, name, location):
    print("{0} : {1} 방향으로 날아감 (속도 [{2}])".format(
          name, location, self.speed))

class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, dem, speed):
    AttackUnit.__init__(self, name, hp, dem)
    Flyable(self, speed)


marine1 = AttackUnit("marine", 40, 5)
marine1.attack("5시")

