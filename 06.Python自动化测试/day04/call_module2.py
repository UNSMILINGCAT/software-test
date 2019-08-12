# import pypackage.m2  #引用包中的模块
# pypackage.m2.sayHello()  #调用包中模块的函数

# 引用包的另一种方式
from pypackage.m2 import *
print("---->")
sayHello()