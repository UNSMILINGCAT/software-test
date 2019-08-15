from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

br = webdriver.Chrome()
br.get("file:///C:/Users/admin/Desktop/form.html")

sleep(2)
br.find_element_by_id("prompt").click()

sleep(2)
alert = br.switch_to.alert
# alert.send_keys("asfffffff")   # 往弹出的输入框输入内容，谷歌浏览器无反应
alert.accept()



