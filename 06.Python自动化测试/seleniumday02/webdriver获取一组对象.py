from  selenium import webdriver
from time import sleep

br = webdriver.Chrome()

br.get('http://192.168.2.103/ecshop/user.php?act=register')

sleep(3)
inputs = br.find_elements_by_tag_name("input")  #根据标签名获取一组标签，返回列表list
for ip in inputs:
    tp = ip.get_attribute("type")
    if tp == "checkbox":
        ip.click()

#  webdriver提供定位一组对象的方法：
#
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_class_name()
# find_elements_by_tag_name()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_xpath()
# find_elements_by_css_selector()