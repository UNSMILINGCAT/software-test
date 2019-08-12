try:
    fh = open("aaa.txt", "r")
    # fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
    # fh.close()
else:
    print("读取文件成功")
    fh.close()
