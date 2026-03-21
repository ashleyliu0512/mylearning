#返回函数值，方便调用并进行其他计算
def add(x,y):  #注意有个冒号
    return x+y,x-y #函数返回了x+y的值

in_x=int(input("输入一个整数"))
in_y=int(input("输入一个整数"))
out_a,out_b=add(in_x,in_y) #调用函数，将函数的两个返回值分别赋给out_a,out_b

print("和"+str(out_a))
print("差"+str(out_b))
print(out_a*2)           #调用out_a进行其他处理

for i in range(10,35,5):  #(起始值（包括），结束值（不包括），间隔）
    print (i)