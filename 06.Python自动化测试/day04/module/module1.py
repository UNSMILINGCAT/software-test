# 自定义模块
# 我是一个计算器，计算两个数的+-*/
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        print("除数不能为0...")
    else:
        return a/b



# 每个python文件（模块）都会有隐含的变量，__name__就是其中之一，表示模块的名称
# 如果将当前模块作为脚本执行，则__name__=="__main__"，如果是将当前模块引入到其它模块执行，则__name__=="模块名"
# print(__name__)
if __name__=="__main__":  # 程序调试   单元测试
    print(div(3,0),"验证除数为0能否正常提示...")