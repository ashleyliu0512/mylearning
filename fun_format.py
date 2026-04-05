name = "张三"
age = 20
# 将变量或表达式插入到字符串中，并根据需要进行格式化。
message = "我叫{0}，今年{1}岁。".format(name, age)
print(message)
print("{1} {0} {1}".format("hello", "world") ) #输出：world hello world'

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site)) #**表示解包字典
 
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 左对齐示例，默认宽度为10
print("Name:{:<10}".format("Alice")) # 输出: Name:Alice____
# 右对齐示例
print("Name:{:>10}".format("Bob")) # 输出: Name:______Bob
# 居中对齐示例
print("Name:{:^10}".format("Cindy")) # 输出: Name:__Cindy__

print("{:.2f}".format(3.1415926))        # 3.14
print("{:+.2f}".format(3.1415926))       # +3.14 （正数前显正，负数前显负）
print("{:-.2f}".format(-1))              # -1.00（只在负数时显示）
print("{:.0f}".format(2.71828))          # 3
print("{:0>2d}".format(5))               # 05  补充0左边填充
print("{:x<4d}".format(5))               # 5xxx  右边填充x
print("{:x<4d}".format(10))              # 10xx
print("{:,.0f}".format(1000000))         # 1,000,000 用逗号分隔数字
print("{:.2%}".format(0.25))             # 25.00%  百分号
print("{:.2e}".format(1000000000))       # 1.00e+09   指数
print("{:>10d}".format(13))              #         13
print("{:<10d}".format(13))              # 13
print("{:^10d}".format(13))              #     13
print("{:b}".format(11))                 # 1011   二进制
print("{:d}".format(11))                 # 11     十进制
print("{:o}".format(11))                 # 13     八进制
print("{:x}".format(11))                 #b      十六进制小写
print("{:X}".format(11))                 #B      十六进制大写
print("{:#x}".format(11))                # 0xb  带前缀的 
print("{:#X}".format(11))                # 0XB
print("{:c},{:c},{:c}".format(97,0o145,0x64))      #转Unicode字符