from selenium import webdriver

br = webdriver.Chrome()
br.get("http://192.168.2.103/ecshop/")
# 打印信息（断言的信息）：
# 　　title
# 　　返回当前页面的标题
print(br.title)

# 　　current_url
# 　　获取当前加载页面的URL
print(br.current_url)

# 　　text
# 　　获取元素的文本信息
txt = br.find_element_by_xpath('//*[@id="ECS_MEMBERZONE"]/a[2]').text
print(txt)