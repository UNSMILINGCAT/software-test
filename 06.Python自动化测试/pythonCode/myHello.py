print("Hello Pycharm")
# 输出内容到控制台
print("Hello")
# abs 函数  计算绝对值
print(abs(35))
# 打印字符串变量
myStr = "Hello World!!!"
print(myStr)
# 逗号可以作为连接字符串的符号
print("呵呵 ",myStr)  # 呵呵  Hello World!!!
# python 占位符替换   s%表示字符串   %d表示整数   %f表示小数
print("%s  is number %d!"%("Python", 1))

# 输入
#name = input("请输入用户名：")
#print("我的名字叫 ",name)

# 默认用户输入的内容都是字符串类型，所以如果想进行数值运算，必须转化为数值
# int() 转化为整数   float() 转化为浮点数
# str() 转化为字符串
age = input("输入年龄：")
print("年龄是",int(age)+100)



