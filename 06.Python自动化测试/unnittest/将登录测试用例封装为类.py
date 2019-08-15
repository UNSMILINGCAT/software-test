from selenium import webdriver
from time import sleep

class testcase_login():
    # http://192.168.2.103/ecshop/user.php
    def __init__(self):
        print("初始化方法...")
        self.br = webdriver.Chrome()
        self.br.get("http://192.168.2.103/ecshop/user.php")


    def testcase001(self):
        '''正确的用户名密码，登录成功'''
        print("登录用例1执行...")
        sleep(1)
        # 输入正确的用户名密码，点击登录
        self.br.find_element_by_name("username").send_keys("vip")
        self.br.find_element_by_name("password").send_keys("vip")
        self.br.find_element_by_name("submit").click()

        # 判断其登录是否成功
        sleep(4)
        if self.br.current_url == "http://192.168.2.103/ecshop/":
            #登录成功
            self.br.quit()
            self.br = webdriver.Chrome()
            self.br.get("http://192.168.2.103/ecshop/user.php")
        else:
            #登录失败
            self.br.quit()
            self.br = webdriver.Chrome()
            self.br.get("http://192.168.2.103/ecshop/user.php")
        sleep(2)

    def testcase002(self):
        '''正确的用户名错误的密码，登录失败'''
        print("登录用例2执行....")
        # 输入正确的用户名密码，点击登录
        self.br.find_element_by_name("username").send_keys("vip")
        self.br.find_element_by_name("password").send_keys("123")
        self.br.find_element_by_name("submit").click()

        # 判断其登录是否成功
        sleep(4)
        if self.br.current_url == "http://192.168.2.103/ecshop/":
            # 登录成功
            self.br.quit()
            self.br = webdriver.Chrome()
            self.br.get("http://192.168.2.103/ecshop/user.php")
        else:
            # 登录失败
            self.br.quit()
            self.br = webdriver.Chrome()
            self.br.get("http://192.168.2.103/ecshop/user.php")
        sleep(2)
    def testcase003(self):
        '''用户名密码为空，登录失败'''
        print("登录用例3执行....")

    def __del__(self):
        print("测试用例执行完成...")


if __name__ == "__main__":
    testLogin = testcase_login()  # 实例化登录测试用例
    testLogin.testcase001()
    testLogin.testcase002()
    testLogin.testcase003()