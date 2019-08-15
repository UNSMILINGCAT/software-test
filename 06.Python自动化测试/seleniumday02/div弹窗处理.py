from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

br = webdriver.Chrome()
# br.get("https://study.163.com")
# sleep(2)
# br.find_element_by_xpath('//*[@id="ux-modal"]/div[3]/span').click()
# sleep(3)
# br.find_element_by_xpath('//*[@id="ux-modal"]/div[1]/a/i').click()

br.get("https://www.dytt8.net/")
sleep(3)
br.find_element_by_xpath('//*[@id="cs_DIV_cscpvrich5041C"]/a/div').click()