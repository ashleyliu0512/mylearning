#列表和函数
def add(xy):
    sum=xy[0]+xy[1]
    print(sum)
    #pass表示什么都不干，但是不报错

list_xy=[]  #创建一个名为“list_xy”的空列表
in_x=int(input("输入第一个整数"))
list_xy.append(in_x)
in_y=int(input("输入第二个整数"))
list_xy.append(in_y)
add(list_xy)