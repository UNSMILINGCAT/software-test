# 抽取指定文本文件中所有的邮件地址
import re

# filepath = input("请输入文件路径:")
#
# fo = open(filepath,"r",encoding="utf8")  # 打开文件
#
# content = fo.read()  #读取文本文件的内容
#
# result = re.findall("(\w+@[a-z0-9]+\.[a-z]{2,4})",content)  #使用正则表达式匹配文件内容
# result = "\n".join(result)
# print(result)
#
# fo.close()

fo = open("abc.txt","r",encoding="utf8")  # 打开文件
content = fo.read()
reg = re.compile("(\w+@[a-z0-9]+\.[a-z]{2,4})")  #编译正则表达式字符串，将字符串转化为正则表达式对象

result = reg.findall(content)

print(result)
fo.close()


