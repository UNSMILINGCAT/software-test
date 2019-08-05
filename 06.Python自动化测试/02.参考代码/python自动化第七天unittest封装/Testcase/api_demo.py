#coding=utf-8
import unittest
from Unittest_demo.Public.HTTP_API import *

class testcase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_post_api(self):
        """验证sina邮箱是否被注册"""
        p=Weburllib2()
        data=p.To_urlencode({"name":"tangzhanggai11@163.com","format":"json","from":"othermail"})
        ret=p.Post('https://login.sina.com.cn/signup/check_user.php',data,{'Content-Type': 'application/x-www-form-urlencoded'})
        retcode=p.Get_from_dict(ret,"retcode")
        self.assertEqual(retcode,100001,"请求错误")
    def test_get_api(self):
        """验证申通快递是否查询成功"""
        p=Weburllib2()
        ret=p.Get("https://www.kuaidi100.com/query?type=yuantong&postid=123456")
        retcode=p.Get_from_dict(ret,"status")
        print retcode
        self.assertEqual(retcode,"200","快递单号不存在")
if __name__=='__main__':
    unittest.main()
