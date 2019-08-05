#coding=utf-8
#***************************************练习*********************************************************
#猜数字，随机产生一个数字，
#给用户输入一个数字，并且提示他跟这个随机的数字比较是大 还是小
#直到用户猜出来为止，程序结束运行
# import random
# i = random.randint(1, 99)
# while 1:
#     num=input("imput number:")
#     if num>i:
#         print "大了"
#     elif num<i:
#         print "小了"
#     else:
#         print "对了"
#         break
# 1.写一个登陆的小程序，用户名admin和密码为888888
# 2.提示用户输入用户名和密码，接下来你要判断用户输入的是否正确
# 3.如果不正确，给他三次机会，
# 4.如果都正确，打印恭喜你，登陆成功
# num = 0
# while 1:
#     user = raw_input("input your user:")
#     passwd = raw_input("input your passwd:")
#     if user=="admin" and passwd=="888888":
#         print "login success!"
#         break
#     else:
#         num += 1
#         if num==3:
#             print "三次输入错误，程序终止运行"
#             break
#         print "login failed %d times,pls try:" % num
################################################字符串#########################################################
# str="asdfgh"
# #\ 续行符号
# str='hello ' \
#     'python'
# str="""  test """
# str='''  test python'''
# print str
# #三引号是可以换行的，其他的不行
# str="""  ##
# asdf
# asdf
# asdf
# """
# print str
##切片运算  $1000
#str="hello python.txt"
#取单个
# print  str[0]  #从前面往后面取字符，那么下标从0开始计数
# print  str[-1] #从后面往前面取字符，那么下标从-1开始计数
#取范围
# print str[2:4]  #开始值  中间是冒号    后面是结束值
# print str[-4:-2]  #倒取的时候要注意   小的数字放前面
# print str[3:]   #取下标开始后面的所有字符
# print str[:3]   #取下标开始前面的所有字符
# print  str[-4:]
# print  str[:-4]
#字符串复制 *
#print str*20
#字符串连接 +
#print str+"abc"
#字符串空格处理
str= "test|Hello|python"
# print str.strip() #去掉两边空格
# print  str.lstrip() #去掉左边的空格
# print  str.rstrip()  #去掉右边的空格
# #大小写转换
# print  str.upper()    #全部转换为大写
# print  str.lower()   #全部转换为小写
#print   str.capitalize()
#字符串切割
# str=str.split("|")  #字符串切割，后面跟你需要切割的参数，也就是你需要按照某种规律来切割
# print str
#字符替换
#print str.replace("t","1234")  #两个参数，第一个是需要替换的字符，第二个替换后的字符
#判断字符在什么范围里面
# x=raw_input("asdf:::")
# print x
# if x=="null":
#     print "sadf"

#字符串查找
# str="duan@163.com"
# print str.find("@")  #如果找到了就显示下标位置；
# print str.find("#")  #如果没有找到永远显示-1；
# if str.find("@")!=-1:
#     print "found ok"
#***********************************************课堂练习*************************************************
# while 1:
#     str=raw_input("input string:")
#     if str=="" or len(str)==0:
#         print "pls try "
#     else:
#         if   str[0] in "aeiou" or str[0] in "AEIOU":
#             print str+"ay"
#         else:
#             print str[1:]+str[0]+'ay'
############################################列表##############################################################
# x=[]
# print type(x)
#列表是中括号表示，以逗号分隔，作为单个元素；
# 可以存储任意长度   任意类型的数据int float str list
#列表里面的数据成为元素，一个个的元素。
# x=[1,"qwe",1.2,"中文"]
#切片运算
# print  x[-1]   #按照下标运算的时候，从前往后0开始计算；从后往前面-1开始计算
# print  x[1:]  #取范围跟字符串一样的
#其他的范围可以参考字符串
#列表操作（增、删、改）
# x.append('abc')     #不管列表中原来有什么，加在最后面的元素
# print x             #print不能够取打印行为。
# for i in range(10):    #循环操作列表增加元素
#     x.append(i)
# print x
# x.insert(21,1.0001) #插入，可以插入你需要的下标位置；后面跟两个参数，第一个是下标的值，第二个是插入的数据
# print x
# x=[1,"qwe",1.2,"中文"]
# #删除
# del   x[2:]     #del 删除指定的下标元素。
# x.remove("qwe") #remove 删除指定的值。
# print x
# #修改
# #######################x[1]="qwertyuio"  #越界
# x[0]="test"
# print x

#列表嵌套
# x=[1,2,34,5.0]
# y=["q","w","e",["r",100,999]]
# x.append(y)   #x=[1, 2, 34, 5.0, ['q', 'w', 'e', ['r', 100, 999]]]
# print x
# print x[4][3][2]
# print x[4]
#列表遍历   列表相加  列表复制  列表排序
# list=[1,"qwe",1.2,"中文"]
# for  i  in  list:
#     if i ==1.2:
#         print "ok"
#     else:
#         print "other"

#列表相加
# list1=[11,2.5,32]
# list2=[40,5.7,6]
# list3= list1+list2  #列表相加 生成一个新的列表
# print list3
# print "hello "+"python"
#
# #列表复制
# print list1*5
#列表排序
# print list3
# list3.sort()   #正序排列
# list3.sort(reverse=True)  #倒序排列
# print list3
#字符串转列表
# str="asdfasdfasd"
# s=[1,2,3,4,5]
# print list(str)
# print  tuple(s) #列表转元组
######################################元组###########################################################
x=()
#元组是小括号声明；存储任意长度，任意类型的数据；x
# x=(1,1.1,"asd","哈哈")
# s=[1,1.1,"asd","哈哈"]
# #元组和list区别：1.元组不能操作（增加，删除，修改）；2.做大数据遍历的时候，速度嗖嗖的快
# #切片运算
# print x[-1]  #下标切片运算参照字符串就行
# #元组嵌套
# x=(1,2,3,("q","w","e",1.1),[11,22,33])
# print x[3][1]
# x[-1][1]="5555"
# print x
#*****************************************课堂练习***********************************************
# if "a"  in  "aeiou":
#     print "ok"
#
# if   "a" in ["a","e","i","o","u"]:
#     print "ok"
#
# if   "a"  in ("a","e","i","o","u"):
#     print "ok"
#
# for i in ["a","e","i","o","u"]:   #采用这种方式会稍微慢一些
#      if "a"==i:
#          print "ok"

#逆序输出字符串
# str='apple9234567tyuipfhjki'
# str1=''
# i=len(str)
# print i
# while i>0:
#     str1+=str[i-1]
#     print str1,str[i-1],i
#     raw_input()
#     i-=1
# print str1
#####################################################字典####################################################
dit={}
#映射   一一对应关系，大括号；键----值
dit={"name":"duan","age":23,"addr":"shenzhen"}
# #键----值 冒号：每一组元素以逗号区分
# print dit  #
# #字典增加
# dit["sex"]='男'
# dit["身高"]=170
# print dit
# #修改字典；如果键存在的话，那就就作为修改；如果键不存在，那么就添加进去
# dit["age"]=45
# print dit
#删除字典元素
# del dit['age']
# print dit
#查询字典元素
# print dit.keys()   #取出所有的键
# print dit.values() #取出所有的值
# print  dit["age"]

#遍历字典
# for key,name in dit.items():
#     print key,name
#     print type(key),type(name)

# for name in dit.items():
#     print name[0],name[1]
#





