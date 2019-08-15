from selenium import webdriver
from time import sleep
import unittest

# 使用单元测试框架unittest
# 步骤：1. 导入unittest模块import unittest
#       2. 需要继承TestCase类class test_login(unittest.TestCase):
#       3. 编写FixTure函数（setUp,tearDown），实现测试用例环境的搭建和销毁
#       4. 编写TestCase 函数都是要以test开头
#       5. 运行脚本  unittest.main()
class test_login(unittest.TestCase):

    def setUp(self):
        '''该方法会在每个测试用例执行之前执行，
        一般会在该方法中做一些测试前的准备工作'''
        self.br = webdriver.Chrome()
        self.br.get("http://192.168.2.103/ecshop/user.php")

    # 测试用例方法以test开头
    def testcase001(self):
        '''正确的用户名密码，登录成功'''
        print("登录用例1执行...")
        sleep(1)
        # 输入正确的用户名密码，点击登录
        self.br.find_element_by_name("username").send_keys("vip")
        self.br.find_element_by_name("password").send_keys("vip")
        self.br.find_element_by_name("submit").click()
        sleep(4)
        # 断言
        self.assertEqual(self.br.current_url,"http://192.168.2.103/ecshop/",msg="正确的用户名密码登录失败，用例执行不通过...")


    def testcase002(self):
        '''用户名密码不匹配，登录失败'''
        print("登录用例2执行....")
        sleep(2)
        # 输入正确的用户名密码，点击登录
        self.br.find_element_by_name("username").send_keys("aaaaaaaa")
        self.br.find_element_by_name("password").send_keys("123")
        self.br.find_element_by_name("submit").click()

    # 跳过测试用例
    # @unittest.skip("测试用例3跳过，不执行....")
    def testcase003(self):
        '''用户名密码为空，登录失败'''
        print("登录用例3执行....")
        sleep(2)
        self.br.find_element_by_name("submit").click()

    def tearDown(self):
        print("测试收尾工作....")
        self.br.quit()

if __name__ == "__main__":
    unittest.main()