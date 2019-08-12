print("1.程序运行开始.....")
try:  # 可能会出现异常的代码
    a = 10/0
except ZeroDivisionError:
    print("2.除数不能为0...")
else:
    print("3.没有异常执行的代码......")
finally:
    print("4.不管程序是否出现异常都会执行的代码...")
print("5.程序结束.........")