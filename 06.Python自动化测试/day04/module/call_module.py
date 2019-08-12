# 调用模块
# import module1
# print(module1.add(1,1))  # 调用模块的方法  模块名称.函数()

# import module1.add   不能通过import 导入指定模块的函数

# 导入指定模块的指定函数
# from module1 import add,sub
# print(add(1,2))
# print(sub(1,2))
# print(mul(1,2))

# 导入指定模块的所有函数
# from module1 import *
# print(add(1,2))
# print(sub(1,2))
# print(mul(1,2))



# from time import sleep as suijiao   # 如果有冲突，可以使用别名区别   as 别名
#
# def sleep():
#     print("sleep....")
#
# suijiao(5)
# print("休眠结束....")

# import time
# time.sleep(5)


# 包：其实就是将多个模块放到一起
# import pypackage.m2
# m2.sayHello()

import module1
#help(module1)  # 获取模块对应的帮助文档  包含模块名，模块注释（描述），函数，文件

# dir(module1)  没效
#help(module1.add)  # 获取模块对应函数的信息


