from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   #需要使用鼠标操作，需要引入该类
from time import sleep
br = webdriver.Chrome()
# br.get("http://192.168.2.103/ecshop/")

# ActionChains 类鼠标操作的常用方法：
#   context_click()  右击
# ii = br.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img")
# ActionChains(br).context_click(ii).perform()

# br.get("file:///C:/Users/admin/Desktop/form.html")
#   double_click()   双击
# sleep(3)
# h22 = br.find_element_by_id("h22")
# ActionChains(br).double_click(h22).perform()

#   drag_and_drop()  拖动

br.get("http://192.168.2.103/ecshop/")
#   move_to_element()  鼠标悬停在一个元素上
sleep(2)
div = br.find_element_by_xpath('//*[@id="category_tree"]/div[6]/div[1]')
ActionChains(br).move_to_element(div).perform()

sleep(0.5)
aa = br.find_element_by_xpath('//*[@id="category_tree"]/div[6]/div[2]/div[1]/a')
ActionChains(br).move_to_element(aa).perform()


#   click_and_hold()   按下鼠标左键在一个元素上

