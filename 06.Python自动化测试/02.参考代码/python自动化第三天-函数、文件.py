#coding=utf-8
#******************************************函数************************************************
# def fun(x,y):#形参
#     return x**y  #返回函数结果
#     
# s=fun(2, 3)#实参
# print s
#     
# #计算闰年
# def calc_year(year):
#     """
#     函数自省；函数注释，这个函数是计算闰年的，需要传递年份；
#     """
#     if year%4==0 and year%100!=0 or year%400==0:
#         return "闰年"
#     else:
#         return "平年"
#函数调用#####################  
# print  calc_year(2016)

#函数是可重用，可调用
# 
# def printMax(a, b):
#     if a > b:
#         print a, 'is maximum'
#     else:
#         print b, 'is maximum'
# print  printMax(3, 4) #直接传实参
# 
# 
# x = 5
# y = 7
# print  printMax(x, y)

# def func(a,b=5, c=10):#默认值
#     print 'and c is', c,'a is', a, 'and b is', b
#   
#****************函数参数传递******************************    
# func(3)#如果默认值不传递参数，那么函数就会取默认值作为运算
# func(3,9)#如果传递值，那么默认的形参就去传递的值
# func(4, 50, c=10)#函数传递参数的时候，按照函数定义的参数位置来传递
# func(4, c=13)#如果你想传入指定的参数，其他的参数不变，那么就需要把函数的形参变量带上
# func(b=14, a=15, c=17)#如果你传递参数的时候，不想按照位置传递，那么也需要把函数的形参变量带上

# func(25, c=24)
# func(c=50, a=100) 

#****************函数之间调用*****************************
# def foo1(x,y):
#    
#     return x**y
# 
# def foo2(x,y):
#     x=foo1(x,y) 
#     y=foo1(x,y) 
#     return x+y
# 
# def foo3(a,b):
#     pass
#     
# print foo1(2,3)
# print foo2(2,3)

#*****************函数参数**********************
# def  foo(a,b,*arg):   #一个星号，代表前面的实参没有形参来接收的时候，全部丢给最后一个参数接收\
#     #并且以一个元组的形式返回,如果要使用取下标
#     print a
#     print b
#     print arg
# 
#     
# foo(1,2,3,4,5,6,7,8,9,0)
# 
# def foo1(x,**arg):#两个星号，代表前面的实参没有形参来接收的时候（并且有恒等关系的数据），
#     #全部丢给最后一个参数接收，返回字典
#     print x
#     print arg
#     
# # foo1(2,a=3,b=4,c=5,d=6)
#     
# def foo2(x,*arg,**dit):
#     print x
#     print arg
#     print dit
#     
# foo2(1,2,3,4,5,6,4,55,66,77777,7,a="qwert",b=12,c=13,d=14)       
#****************函数作用域********************
# a=2
# def testfun():
#     #a=4#这里的赋值，只会作用于函数的内部，不会改变外面的变量值（局部变量）
#     global a  #全局变量，一旦修改，外面的变量也跟随改变
#     a=5
#     return a
# def testfun1():
#     a=99
#     return a
# 
# print a 
# print testfun()
# print a
# print testfun1()
# print a

#**********函数自省************************
# def foo(x,y):
#     """
#     这是一个测试函数
#     用来返回x的y次方
#     当然你调用函数的时候
#     需要传递2个值，是x和y
#     """
#     return x**y
# print foo.__doc__
#*****************判断三角形**************
# def triangle(x,y,z):
#     """
#     判断三角形函数，传入三边，返回字符串
#     """
#     if x+y>z and x+z>y  and z+y>x :
#         if x==y!=z or  x==z!=y or y==z!=x:
#             return "等腰三角形"
#         elif x==y==z:
#             return "等边三角形"
#         elif x**2+y**2==z**2 or x**2+z**2==y**2 or y**2+z**2==x**2:
#             return "直角三角形"
#         else:
#             return "一般三角形"
#     else:
#         return "不是三角形"
#
# # print triangle(1, 2, 1)            
# def kill_process(name):
#     """
#     专杀windows系统进程
#     """
#     import os
#     os.system("taskkill /f /im "+name+" >nul  2>nul") #调用windows/linux系统命令;bat\shell都可以
#     #os调用系统命令的时候 注意区分平台；
# def foo_test():
#     """
#     """
#     return "ok"
# from testbase import mysqldb as s  #别名
# s.foo_Test()
####################################递归函数
# 函数返回1 + 2 + 3 + ... + n的和
# def add(n):
#     if n == 1:
#         return n
#     s = add(n - 1) + n
#     return s
# print "1 + 2 + 3... + 100 = %d" % add(100)
##############################################文件读写################################################
# 打开文件,返回一个文件对象
# # f = open("D:\\tmp\\file.txt")
# f = open(r"D:\tmp\file.txt")
# # 指定读取n个字节
# content = f.read(5)
# # content = f.read()
# print "========文件内容如下========"
# print content
# f.close()
####文件读取
# r   只读方式,文件不存在,会报错
# r+  读写方式,................
# w   只写方式,文件不存在会创建文件,文件存在,会被截断(文件大小变为0)
# w+  读写方式.................................................
# a   追加方式,文件不存在会创建文件,文件存在,会写入文件尾(追加)
# a+  读写方式.................................................
#举个栗子
# f = open("D:\\tmp\\file.txt")
# f = open("D:\\tmp\\file.txt", "r+")
# f = open("D:\\tmp\\file.txt", "w")
# f = open("D:\\tmp\\file.txt", "a")
# f.write("abc\n")
# f.close()

# file=open("file.txt","a")  #以写的方式打开一个文件，如果没有加路径# ，那么就会直接写在当前的目录下；第二个参数是模式
# #w全新写 覆盖，a 追加
# print file
# file.write("test\n \t")          #调用file对象 去写数据
# file.close()                 #文件读写，完成后都要进行关闭

# file=open(r"d:\test.txt","a")  #\转义符号 如果是其他路径，需要加双斜线;不想 加双斜线也可以，那么在路径前面加r
# #w全新写 覆盖，a 追加
# print file
# file.write("test\n \t")          #调用file对象 去写数据
# file.close()                 #文件读写，完成后都要进行关闭

# file=open("../test.txt","a")  #上层目录加../
# #w全新写 覆盖，a 追加
# print file
# file.write("test\n \t")          #调用file对象 去写数据
# file.close()                 #文件读写，完成后都要进行关闭
#
# path=u"d:\\题目.txt"           #u 处理中文路径
# file=open(path,"r")             #r  以读的方式去打开文件
# print file.read().decode('gbk') #decode函数用来处理字符编号格式
# file.close()                    #文件读写，完成后都要进行关闭

#####for来遍历文件
# f = open("D:\\tmp\\file.txt")
# # 文件对象可以直接用for来遍历,每次一行
# for line in f:
#     line = line.strip()
#     print line
# f.close()

# print "========================"
# # 在离开with代码块之前,会关闭文件
# with open("D:\\tmp\\file.txt") as f:
#     for line in f:
#         line = line.strip()
#         print line