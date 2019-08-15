from selenium import webdriver
from time import sleep

br = webdriver.Chrome()
br.get("https://www.toutiao.com/")
cuhandle = br.current_window_handle
sleep(2)

# 点击直播，跳转到直播页面
br.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/ul/li[4]/a').click()
# cuhandle2 = br.current_window_handle



# print(cuhandle == cuhandle2)
sleep(2)
# br.find_element_by_xpath('/html/body/div/div[2]/div[1]/div/div/ul/li[5]/a').click()
# br.find_element_by_link_text("全部").click()
# 多窗口的处理：
# current_window_handle
# 　　获得当前窗口句柄



# window_handles
# 　　返回的所有窗口的句柄到当前会话
handles = br.window_handles
for hd in handles:
    if hd != cuhandle:
        br.switch_to.window(hd)
        zbhanle = hd

br.find_element_by_xpath('//*[@id="App"]/div/div[1]/div[1]/div/span[3]').click()


# switch_to_window()
#       用于处理多窗口之前切换

# 关闭当前页面，如果只有一个网页，则关闭浏览器
# br.close()
sleep(2)
br.quit()   # 退出浏览器
