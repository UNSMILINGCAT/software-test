from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


br = webdriver.Chrome()
# br.get("http://192.168.2.103/ecshop/")


# br.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[2]').click()
# # 脚本中的等待时间：
# # sleep()：
# sleep(2)
# br.find_element_by_id("username").send_keys("aabbaa")

# python提供设置固定休眠时间的方法。
# implicitly_wait()：
# 是webdirver提供的一个超时等待。
# br.implicitly_wait(0.01)
# br.get("http://192.168.2.103/ecshop/")
#
# br.find_element_by_name("keywords").send_keys("哈哈")


# WebDriverWait()：
# 同样也是webdirver
# 提供的方法。
br.get('https://huilansame.github.io')
locator = (By.LINK_TEXT, 'CSDN')
try:
    WebDriverWait(br, 5, 0.5).until(EC.presence_of_element_located(locator))
    print(br.find_element_by_link_text('CSDN').get_attribute('href'))
finally:
    # br.close()
    pass