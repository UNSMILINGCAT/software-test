#coding=utf-8
###########################################随机数模块#######################################################
import random
if __name__ == '__main__':
    # 产生一个1--->100之间的随机整数
    r = random.choice(range(1, 100 + 1))
    # r = random.randrange(1, 100 + 1)
    # r = random.randint(1, 100)
    while True:
        n = input("请猜一个数字[1--->100]: ")
        if n == r:
            print "恭喜,猜对啦!"
            break
        elif n > r:
            print "大了"
        else:
            print "小了"
    print "程序结束!"
 #####################################################sys模块################################################
import sys
# 模块搜索路径
print sys.path
# 当前运行的平台
print sys.platform
# stdin stdout stderr
# 类文件对象, stdout标准输出设备 stderr 标准错误输出设备 stdin 标准输入设备
sys.stdout.write("hello world\n")
sys.stderr.write("hello world\n")
print sys.stdin.read()
#####################################################os模块####################################################
import os
import time

# 与操作系统接口相关的功能模块
# 创建目录
# os.mkdir("D:\\tmp\\automation")
# 创建多级目录
# os.makedirs("D:\\tmp\\automation\\123")
# 删除文件
# os.remove("D:\\tmp\\file.txt")
# 删除目录
# os.rmdir("D:\\tmp\\automation")
# 修改目录或文件名
# os.rename("D:\\tmp\\abc.txt", "D:\\tmp\\test.txt")
# os.rename("D:\\tmp\\abc", "D:\\tmp\\ccc")
# print "当前工作目录:",os.getcwd()
# os.chdir("D:\\tmp")
# print "当前工作目录:",os.getcwd()
# os.remove("test.txt")

# 判断目录是否存在
# print os.path.isdir("D:\\tmp")
# 判断普通文件是否存在
# print os.path.isfile("D:\\tmp")
# print os.path.isfile("D:\\tmp\\test.txt")

# 判断文件是否存在
# print os.path.exists("D:\\tmpxx")
# print os.path.exists("D:\\tmp")
# print os.path.exists("D:\\tmp\\test.txt")

# print os.listdir("D:\\tmp")
a = os.stat("D:\\tmp\\test.txt")
# print "文件大小", a.st_size
mtime = a.st_mtime
lt = time.localtime(mtime)
mt = time.strftime("%Y/%m/%d %H:%M", lt)
print "%-10s%-5s%-20s" % ("test.txt", a.st_size, mt)

print "路径分割符:", os.path.sep
# print "换行字符:", os.linesep

print "========================================"
# open("D:\\tmp\\test.txt")
f = open("D:" + os.path.sep + "tmp" + os.path.sep + "test.txt", "r+")

for line in f:
    print line.strip()
    # print "当前文件指针位置:",f.tell()
print "=======再读一次文件========"
print "当前文件指针位置:", f.tell()
f.seek(2)  # 设置文件指针位置,相对于文件开始处,偏移2个字节

print "当前文件指针位置:", f.tell()
for line in f:
    print line.strip()

f.seek(0, 1)  # 第二个参数: 默认值是0,代表相对文件开始处, 1代表相对当前文件指针位置 2 相对文件尾
print "当前文件指针位置:", f.tell()
f.write("=============\n")

f.close()
# f.read()
#################################################time时间模块#################################################

from time import *

# 获取时间戳: 1970年1月1日凌晨到现在的秒数
t = time()
print t

lt = localtime()
print "localtime:", lt
# lt = localtime(1000000000)
# print "localtime:", lt
# 返回一个固定格式的表示时间日期的字符串
print asctime()
print asctime(lt)
print "================================"
# strftime()
print strftime("%Y %y")
print strftime("%A %a")
print strftime("%B %b")
print strftime("%Y/%m/%d %H:%M:%S")
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# print strftime("%Y", lt)
########################################################system####################################################
import os

# system() 执行其他程序或者cmd命令
# os.system("md C:\\createbypy")
# os.system("7time.py")

# abspath 返回一个文件的绝对路径
ap = os.path.abspath("7time.py")
print os.path.split(ap)
print os.path.dirname(ap)
print os.path.basename(ap)
####################################################异常处理#####################################################
#举个栗子一
try:
    print "in try"
    # open("xxx.txt")
    1 / 0
    print "out try"
# except ZeroDivisionError:
except ZeroDivisionError, e:
    print "不好,产生异常啦"
    print "错误信息:%s" % e
print "程序结束"
#举个栗子二
try:
    print "in try"
    open("xxx.txt")
    #1 / 0
    print "out try"
except:  # try代码块产生任何异常,都进入该except
    #print "异常!!!!"
    pass   #简单的忽略所有异常
print "程序结束"
import sys
#举个栗子三
try:
    print "in try"
    #open("xxx.txt")
    #1 / 0
    print "out try"
except IOError,e:
    print "IOError, message: %s"%e
    # 结束程序,参数可以是字符串,也可以是数字,默认是0,代表正常结束程序
    sys.exit("出错了,程序结束")
except ZeroDivisionError, e:
    print "ZeroDivisionError, message: %s"%e
else:
    print "哈哈哈哈哈哈,没有异常!"
print "程序结束"
#################################################异常的第二种######################################
import sys
try:
    f = open("test.txt", "r")
# f = open("test.txt", "r+")
except IOError:
    print "文件不存在"
    sys.exit(1)
# try:
#     f.write("Hello")
# finally:
#     print "关闭文件啦"
#     f.close()
try:
    f.write("Hello")
except IOError:
    print "文件打开方式不对!"
    sys.exit(1)
finally:
    print "关闭文件啦"
    f.close()
print "程序结束"