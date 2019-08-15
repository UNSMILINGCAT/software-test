from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

br = webdriver.Chrome()  # 打开谷歌浏览器

# 打开ecshop后台管理的首页
br.get("http://192.168.2.103/ecshop/admin/privilege.php?act=login")

#输入账号密码进行登录
br.find_element_by_name("username").send_keys("admin")
pwd = br.find_element_by_name("password")
pwd.send_keys("admin888")
pwd.send_keys(Keys.ENTER)  # 按下回车进行表单提交

sleep(1)
#点击商品列表
# 找到对应的frame   可以根据id或者name属性值查找
br.switch_to.frame("header-frame")  # id="header-frame"
br.find_element_by_link_text("商品列表").click()

# 需要先出去，然后再进去另一个frame
# br.switch_to.default_content()
br.switch_to.parent_frame()


# 勾选商品
sleep(1)
br.switch_to.frame("main-frame")  # name="main-frame"
br.find_element_by_xpath('//*[@value="69"]').click()

# 选择下拉选项
from selenium.webdriver.support.select import Select
sleep(1)
sele = br.find_element_by_id("selAction")
# sele.click()
# 选中回收站
# Select(sele).select_by_value("trash")  #value值
Select(sele).select_by_visible_text("回收站")  #显示的文本

sleep(1)
# br.switch_to.alert.accept()   # accept 表示同意，其实就是点击确定（ok）按钮
br.switch_to.alert.dismiss()    # 点击取消按钮



