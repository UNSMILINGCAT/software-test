# 检查指定文本文件中的英文拼写，将所有单词首字母大写,重新写入文件
# 使用命令行指定文本文件
# 文本文件可能有换行
# 需要使用file对象
# 提示：使用capwords

import string

filepath = input("请输入文件的路径:")
str = ""
try:
    fo = open(filepath,"r",encoding="utf8")  # 文件对象
    # content = fo.read()  # 读取文件中所有的文本
    # result = string.capwords(content)
    for row in fo.readlines():
        str += string.capwords(row)+"\n"
    fo.close()
except FileNotFoundError:
    print("出错啦！文件路径不对....")

with open(filepath,"w",encoding="utf8") as fo:
    fo.write(str)
    fo.close()
