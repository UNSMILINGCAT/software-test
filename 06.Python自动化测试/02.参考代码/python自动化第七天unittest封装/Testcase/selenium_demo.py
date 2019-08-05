#coding=utf-8
from Unittest_demo.Public.ITLEOFramework import ITleoFramework
from time import sleep
import unittest,time
from Unittest_demo.Config.ecshop_conf import *

class baiduTest(unittest.TestCase):

    def setUp(self):
        self.driver = ITleoFramework("chrome")
        self.driver.wait(10)
        self.base_url = ecshop_url

    def test_case(self):
        driver = self.driver
        driver.open(self.base_url)
        driver.click_text("请登录")
        try:
            driver.input_text('id=>username',login_name)
            driver.input_text('xpath=>/html/body/div[2]', login_passwd)
        except Exception ,e:
            driver.save_windows_img(driver.get_image_path())
            print e

        sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()