number=[6,3,7,27,34,38]  #对应元素编号【0，1，2，3，4，5】
print(number[0])  #取出对于0元素
print(number[2:4])  #序号2-4：取出2，3号元素
print(number[:4])   #开头到三号元素
print(number[3:])   #3号元素和后面的所有元素
number.insert(3,100)#将100 加入到列表中，在3号元素位置
number.append(150) #加入150到列表末尾
number.remove(27)#删除列表中27

number.sort()#从小到大排序
number.sort(reverse=True)#从大到小排序

for f in number:  #按顺序取出元素，并放入f变量中
    print(f)
