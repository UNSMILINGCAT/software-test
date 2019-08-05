#coding=utf-8
from selenium import  webdriver
from time import sleep
from selenium.webdriver.support.select import Select
###################################初始化数据###############################################
login_username="duandongbo3"
login_passwd="123456"
admin_user="root"
admin_passwd="qwe123QWE"
login_url="http://192.168.1.222/ecshop"
admin_url="http://192.168.1.222/ecshop/admin"
#############################################################################################
#########################################初始化浏览器########################################
br=webdriver.Chrome()
br.get(login_url)
br.implicitly_wait(10)
br.maximize_window()
############################################################################################
####login
br.find_element_by_css_selector('a[href="user.php"]').click()
br.find_element_by_css_selector('input[name="username"]').send_keys(login_username)
br.find_element_by_css_selector('input[name="password"]').send_keys(login_passwd)
br.find_element_by_css_selector('input[name="submit"]').click()

#shoping
sleep(1)
br.find_element_by_css_selector('a[href="category.php?id=16"]').click()
br.find_element_by_css_selector('a[href="goods.php?id=47"]').click()
br.find_element_by_css_selector('input[name="number"]').clear()
sleep(0.5)
br.find_element_by_css_selector('input[name="number"]').send_keys("2")
br.find_element_by_css_selector('img[src="themes/default/images/buybtn1.png"]').click()
br.find_element_by_css_selector('img[src="themes/default/images/checkout.gif"]').click()

#address
try:
    sleep(1)
    Select(br.find_element_by_css_selector('[name="province"]')).select_by_visible_text("广东省")
    Select(br.find_element_by_css_selector('[name="city"]')).select_by_visible_text("深圳市")
    Select(br.find_element_by_css_selector('[name="district"]')).select_by_visible_text("南山区")
    br.find_element_by_css_selector('[name="consignee"]').send_keys(login_username)
    br.find_element_by_css_selector('[name="address"]').send_keys(u"虚拟大学园W1-A")
    br.find_element_by_css_selector('[name="tel"]').send_keys("13412341234")
    br.find_element_by_css_selector('[name="Submit"]').click()
except Exception,e:
    print "老用户下单，无需选择地址。",e

#submit order
sleep(1)

br.find_element_by_css_selector('input[name="shipping"][value="6"]').click()
br.find_element_by_css_selector('input[name="payment"][value="2"]').click()
br.find_element_by_css_selector('textarea[name="postscript"]').send_keys(u"速速发货")
br.find_element_by_css_selector('input[type="image"]').click()

#get orderno
sleep(1)
orderno=br.find_element_by_css_selector('font[style="color:red"]').text
print "订单号是：%s"%str(orderno)

#login admin
br.get(admin_url)
br.implicitly_wait(10)
br.maximize_window()
br.find_element_by_css_selector('[name="username"]').send_keys(admin_user)
br.find_element_by_css_selector('[name="password"]').send_keys(admin_passwd)
br.find_element_by_css_selector('[type="submit"]').click()
#order manage
br.switch_to.frame('header-frame') #从默认的内容切入到新的框架里面
br.find_element_by_css_selector('a[href="order.php?act=list"]').click()
br.switch_to.default_content()
#br.switch_to_default_content()#是selenium2.5* 的老的方法
#search order
br.switch_to.frame("main-frame")
br.find_element_by_css_selector('[name="order_sn"]').send_keys(orderno)
br.find_element_by_css_selector('input[type="submit"]').click()
sleep(1)
br.find_element_by_link_text('查看').click()
sleep(1)
br.find_element_by_css_selector('[name="confirm"]').click() #确认订单
br.find_element_by_link_text('订单信息').click()
br.find_element_by_css_selector('[name="pay"]').click()
br.find_element_by_css_selector('[name="action_note"]').send_keys('ok')
br.find_element_by_css_selector('[name="submit"]').click()#确认付款

#配货
br.find_element_by_link_text('订单信息').click()
sleep(1)
br.find_element_by_css_selector('[name="prepare"]').click()
br.find_element_by_link_text('订单信息').click()
br.find_element_by_css_selector('[name="ship"]').click()#生成发货单
br.find_element_by_css_selector('[name="delivery_confirmed"]').click()#确定生成发货单
br.find_element_by_link_text('订单信息').click()
br.find_element_by_css_selector('[name="to_delivery"]').click()#去发货

sleep(1)
br.find_element_by_link_text('查看').click()
br.find_element_by_css_selector('[name="delivery_confirmed"]').click()#发货
br.find_element_by_link_text("发货单查看").click()