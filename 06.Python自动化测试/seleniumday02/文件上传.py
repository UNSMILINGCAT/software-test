from selenium import webdriver
from time import sleep

br = webdriver.Chrome()
br.get("http://192.168.2.103/ecshop/")  # 打开ecshop


# 点击请登录按钮，跳转到登录页面
br.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[1]').click()

# 输入用户名密码，提交表单
br.find_element_by_name("username").send_keys("vip")
br.find_element_by_name("password").send_keys("vip")
br.find_element_by_name("submit").click()

# 点击用户中心
sleep(1)
br.find_element_by_xpath("//*[@id=\"ECS_MEMBERZONE\"]/font/a[1]").click()

# 点击我的留言
br.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/div/a[6]').click()


# 输入留言标题
sleep(0.5)
br.find_element_by_name("msg_title").send_keys("留言主题")
#输入留言内容
br.find_element_by_name("msg_content").send_keys("留言\n内容")
#上传文件
br.find_element_by_name("message_img").send_keys(r"C:\Users\admin\Desktop\aa222.png")

#点击提交
br.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div/form/table/tbody/tr[5]/td[2]/input[2]').click()

