#coding=utf-8
from appium import  webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = '127.0.0.1:6555'
desired_caps['appPackage'] = 'com.jingdong.app.mall'
desired_caps['appActivity'] = '.MainFrameActivity'
desired_caps['unicodeKeyboard'] = True

# os.system("start.bat")
# time.sleep(5)
# os.system("adb connect 127.0.0.1:6555")
# os.system("taskkill /f /im "+ name)
driver1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
try:

    time.sleep(10)
    # el=driver1.find_element_by_id("com.jingdong.app.mall:id/su")

    # print el
    h = driver1.find_element_by_xpath("//android.widget.RadioButton[contains(@index,4)]")
    h.click()
    driver1.find_element_by_id("com.jingdong.app.mall:id/e9n").click()
    driver1.find_element_by_id("com.jingdong.app.mall:id/d8s").clear()
    driver1.find_element_by_id("com.jingdong.app.mall:id/d8s").send_keys("")

    driver1.find_element_by_id("com.jingdong.app.mall:id/d8z").clear()
    driver1.find_element_by_id("com.jingdong.app.mall:id/d8z").send_keys("")

    driver1.find_element_by_id("com.jingdong.app.mall:id/d97").click()

    time.sleep(10)
except:
    driver1.quit()
driver1.quit()
