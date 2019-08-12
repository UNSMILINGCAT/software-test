# 常用模块os
import os

# os.name字符串指示你正在使用的平台。比如对于Windows，它是‘nt’，而对于Linux/Unix用户，它是‘posix’。
print(os.name)
# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用‘\r\n’，Linux使用‘\n’而Mac使用‘\r’。
# print(os.linesep)

# os. sep 操作系统特定的路径分割符。 Windows为’\’,Unix为’/’
print(os.sep)

# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
print(os.getenv("path"))  # 获取指定的环境变量

# os.remove()函数用来删除一个文件。
# os.remove("C:\\Users\\admin\\Desktop\\bbb.csv")

# os.system()函数用来运行shell命令。
# os.system("mkdir aabbaa")


# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
print(os.getcwd())
# os.listdir()返回指定目录下的所有文件和目录名。
print(os.listdir("E:\\Python37"))

# os.path.split()函数返回一个路径的目录名和文件名。
print(os.path.split("E:\\Python37\\Scripts\\pip.exe"))

# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。
# os.path.exists()函数用来检验给出的路径是否真的存在
# print(os.path.exists("E:\\Python37\\Scripts\\pip88.exe"))

import stat
# 底层文件操作
# open() 打开文件
fo = open("../aaa.txt","r",encoding="utf8")
# close() 关闭文件
# fstat() 获得文件属性
st = os.fstat(fo.fileno())
print(st[stat.ST_SIZE])

#     fp = open("d:\\resesswd.sql")
# st = os.fstat(fp.fileno())
# print  st[stat.ST_SIZE]
# read() 读文件
for row in fo.readlines():
    print(row)
# write() 写文件

fo.close()