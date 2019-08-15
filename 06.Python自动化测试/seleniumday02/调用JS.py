from  selenium import webdriver
from time import sleep

br = webdriver.Chrome()
br.get("http://192.168.2.103/ecshop/")


# 滚动条处理
# #将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=10000"
br.execute_script(js)
#
# #将滚动条移动到页面的顶部
sleep(2)
js_="var q=document.documentElement.scrollTop=0"
br.execute_script(js_)

sleep(2)
hello = "alert('Hello JS')"
br.execute_script(hello)
