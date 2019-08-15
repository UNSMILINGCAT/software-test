# 测试断言

import unittest

class test_assert(unittest.TestCase):

    def setUp(self):
        print("测试用例执行开始...")

    def tearDown(self):
        print("用例执行结束....")

    def test001(self):
        print("用例1执行...")
        self.assertEqual(1,1,msg="测试用例不通过...")

    def test002(self):
        print("用例2执行...")
        self.assertNotEqual(1,2,msg="测试用例2执行不通过...")

if __name__ == "__main__":
    unittest.main()