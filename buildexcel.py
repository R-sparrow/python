import os
import openpyxl
def showpath():
  path = os.getcwd()
  print(path)
showpath()
os.chdir(r"C:\Users\admin\Desktop\新建文件夹")
showpath()
wb = openpyxl.load_workbook('新表.xlsx')
print(wb)
print(type(wb))