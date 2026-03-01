num=7
i=1
while i <6:
    x=int(input("输入0-9的整数："))
    if x==num:
        print("right")
        break
    else:
        print("sorry")
    i=i+1
else:
    print("end")