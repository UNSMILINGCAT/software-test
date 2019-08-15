import unittest
import test_register
import test_login

if __name__ == "__main__":
    suite = unittest.TestSuite()  # 创建测试套件
    # 往测试套件中放入测试用例
    suite.addTest(test_register.test_register("testcase002"))
    suite.addTest(test_register.test_register("testcase001"))
    suite.addTest(test_login.test_login("testcase005"))
    suite.addTest(test_login.test_login("testcase002"))
    suite.addTest(test_login.test_login("testcase003"))

    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(suite)