 #import 模块名  导入模块。要在同一个文件夹下才可以导入
 #模块名.函数名（）
 #函数文件夹最好只有函数，没有print
 #想导入一个模块中一个函数： from 模块名import 函数名 print（函数名（））
from function_1 import add 
in_x=int(input("输入一个整数"))
in_y=int(input("输入一个整数"))
print (add(int_x,int_y))