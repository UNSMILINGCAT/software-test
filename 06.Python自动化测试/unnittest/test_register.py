from selenium import webdriver
from time import sleep
import unittest

# 使用单元测试框架unittest
# 步骤：1. 导入unittest模块import unittest
#       2. 需要继承TestCase类class test_login(unittest.TestCase):
#       3. 编写FixTure函数（setUp,tearDown），实现测试用例环境的搭建和销毁
#       4. 编写TestCase 函数都是要以test开头
#       5. 运行脚本  unittest.main()
class test_register(unittest.TestCase):

    def setUp(self):
        '''该方法会在每个测试用例执行之前执行'''
        print("注册测试环境的初始化...")

    # 测试用例方法以test开头
    def testcase001(self):
        print("注册测试用例1执行...")



    def testcase002(self):
        '''用户名密码不匹配，登录失败'''
        print("注册测试用例2执行...")


    def tearDown(self):
        print("注册测试用例执行结束....")

if __name__ == "__main__":
    suite = unittest.TestSuite()  # 创建测试套件
    # 往测试套件中放入测试用例
    suite.addTest(test_register("testcase002"))
    suite.addTest(test_register("testcase001"))

    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
