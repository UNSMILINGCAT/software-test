#string模块
import string
# capwords(string)该函数可把字符串的首个字符替换成大写。
str1 = "my name is linSir  name"
print(string.capwords(str1))

# lower(string)该函数把字符串转化为小写
print(str1.lower())
# upper(string)该函数把字符串转化为大写
print(str1.upper())
# replace(string,old,new[,maxsplit])字符串的替换函数，把字符串中的old替换成new。默认是把string中所有的old值替换成new值，如果给出maxsplit值，还可控制替换的个数，如果maxsplit为1，则只替换第一个old值。
str2 = str1.replace("name","username")
print(str2)

# split(string,sep=None,maxsplit=-1)从string字符串中返回一个列表，以sep的值为分界符。
str="192.168.1.2"
s=str.split(".")
print(s)

# join(string[,sep])返回用sep连接的字串，默认的sep是空格。
x="hello"
y="1234"
p=x.join(y)
print(p)  #1hello2hello3hello4
pp=y.join(x)  #h1234e1234l1234l1234o
print(pp)

ss = x.join("   ")
ss = " ".join(x)
print(ss)
