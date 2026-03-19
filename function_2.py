#函数
def add(x,y): 
    print('x:',str(x))  #str函数是将数字转为字符串，就是以字符串输出数字
    sum=x+y  #sum属于局部变量
    print(sum)
    
in_x=int(input("输入一个整数"))
in_y=int(input("输入一个整数"))
add(in_x,in_y)   #调用add函数，并将in_x传给函数

# print(sum *2)没有return将sum赋值，所以没法调用sum经行其他计算