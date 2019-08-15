from  selenium import webdriver
from selenium.webdriver.common.keys import Keys  #需要使用类键盘操作需要引入Keys类
from time import sleep

br = webdriver.Chrome()
# br.get("http://192.168.2.103/ecshop/")
# br.maximize_window()
#
# sleep(1)
# br.find_element_by_xpath("//*[@id=\"keyword\"]").send_keys("aabbaa")

#  Keys 类键盘操作的常用方法：
# 　　send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# sleep(1)
# kw = br.find_element_by_xpath("//*[@id=\"keyword\"]")
# kw.send_keys(Keys.BACK_SPACE*3)


# 　　send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# kw.send_keys(Keys.CONTROL,'a')

# 　　send_keys(Keys.SPACE)  空格键(Space)
# kw.send_keys(Keys.SPACE)

br.get("http://192.168.2.103/ecshop/user.php?act=register")
# 　　send_keys(Keys.TAB)  制表键(Tab)
sleep(1)
user = br.find_element_by_id("username")
user.send_keys("user111")
# user.send_keys(Keys.TAB)

# 　　send_keys(Keys.ESCAPE)  回退键（Esc）
# 　　send_keys(Keys.ENTER) 回车键（Enter）
# user.send_keys(Keys.ENTER)

sleep(2)
# 　　send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
user.send_keys(Keys.CONTROL,'a')
user.send_keys(Keys.CONTROL,'c')
# 　　send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# 　　send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
br.find_element_by_id("email").send_keys(Keys.CONTROL,'v')