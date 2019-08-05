#coding=utf-8
from selenium import  webdriver
from time import  sleep
from selenium.webdriver.common.keys import Keys
br=webdriver.Firefox()
br.get("http://s.cjol.com/l2008/?KeywordType=0&Keyword=%u0075%u0069&RecruitmentType=1&SearchType=1003")
br.maximize_window()
br.implicitly_wait(30)

ex_company=["拜拜科技（深圳）有限公司","广州森迪信息科技有限公司","深圳市易课文化科技有限公司"]

def choose_company():
    elelist=br.find_elements_by_class_name("results_list_box")
    print type(elelist)
    for ele in elelist:
        companytext= ele.find_element_by_class_name("list_type_second").text
        print type(companytext)
        #ele.find_element_by_css_selector('input[type="checkbox"]').click()
        if companytext.encode('utf-8') not in ex_company:
            ele.find_element_by_css_selector('input[type="checkbox"]').send_keys(Keys.SPACE)

def custom(pagenum):
    for i in range(1,pagenum+1):
        if i !=1 :
            br.find_element_by_link_text(str(i)).click()
        choose_company()

def read_file():
    pass

def login():
    pass