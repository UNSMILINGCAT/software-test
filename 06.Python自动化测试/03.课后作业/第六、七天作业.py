#coding=gbk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time,datetime
from selenium.webdriver.common.action_chains import ActionChains
import linecache,logging

d1 = datetime.datetime.now()
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
job_page_num=11#设置需要投递几页的公司
job_name=u"软件测试工程师"
job_city="深圳"
job_company=[]


# 创建一个logger
logger = logging.getLogger('cjol.resume.logger...')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('.//log//resume.logger.log')
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


def read_company():
    #读取屏蔽公司名单列表
    with open('.//data//exclude_company.txt','r') as f:
        for line in f:
            line=line.strip()
            job_company.append(line)
    logger.info("loading exclude company success...")
    
def login_user():
    #输入用户名和密码
    driver.find_element_by_id("txtUserName").clear()
    driver.find_element_by_id("txtUserName").send_keys(user_data[0])
    ActionChains(driver).key_down(Keys.TAB).perform()
    time.sleep(1)
    driver.find_element_by_id("txtPassword").clear()
    driver.find_element_by_id("txtPassword").send_keys(user_data[1])
    try:
        driver.find_element_by_id("btnLogin_input").click()
    except:pass
    #关闭登陆后的二维码广告浮层
    try:
        driver.find_element_by_class_name("icon_closedmyapp").click()
    except:pass
    logger.info("login success...")
    
def check_auto_login():
    #判断界面的自动登录是否勾选
    if driver.find_element_by_id("cbxPeriod").is_selected():
        driver.find_element_by_id("cbxPeriod").click()
        
def serach_save_job():
    #刷新简历
    logger.info("start serach job...")
    try:
        driver.find_element_by_css_selector('i[class="icon-myrefresh"]').click()
    except:pass
    time.sleep(1)
    #输入职位名称，用于搜索工作（需要参数化）
    driver.find_element_by_id("a_MyResumeCenterAutoSearchResult").click()
    #判断学生首次登录投递的时候 界面没有输入框，需要点击一下
    if driver.find_element_by_id("a_setsearchjobs").is_displayed():
        try:
            driver.find_element_by_id("a_setsearchjobs").click()
        except:
            pass
    logger.info("start selece city...")     
    driver.find_element_by_id("txtKeyWord").clear()
    driver.find_element_by_id("txtKeyWord").send_keys(job_name)
    #判断城市是否在深圳
    try:
        if driver.find_element_by_id("txtRegion").text != u"广东深圳":
            driver.find_element_by_id("txtRegion").click()
            time.sleep(1)
            driver.find_element_by_link_text(u"深圳").click()
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='winLocation_dropdivrdiv_2008']/div/div/div/p/span").click()
            time.sleep(1)
            driver.find_element_by_id("winLocation_dropdivselected_ok").click()
            time.sleep(1)
    except:pass
    driver.find_element_by_id("txtKeyWord").click()
    driver.find_element_by_id("btnSaveAndSearch").click()#点击保存并搜索按钮
    logger.info("search job success...") 
    
def select_job():
    #开始默认全选当前页面复选框)
    time.sleep(3)
    logger.info("start  selcect company...")   
    list=driver.find_elements_by_class_name("results_list_box")
    for  i in list:
        company=i.find_element_by_class_name("list_type_second").text
        if company.encode('utf-8') not in job_company:
            try:
                cancel=i.find_element_by_class_name("list_type_checkbox").find_element_by_css_selector("input.checkbox")
                cancel.click()
            except:pass
    logger.info("select  company  end...")               
def finish_job():
    #按照规则匹配后点击投递按钮开始投递    
    logger.info("start apply job...")  
    try:
        now_handle = driver.current_window_handle         
        driver.find_element_by_id("btnApplyJob").click() 
        logger.info("switch to handle...")  
    #切换到网页弹出的子投递窗口
    except:pass
    time.sleep(2)
    try:
        driver.switch_to_frame("appjob_iframe")
        driver.find_element_by_id("btnApply").click()
        logger.info("switch to appjob_iframe...") 
    except:pass
    #点击完成按钮
    time.sleep(2)
    try:
        driver.find_element_by_id("finish").click()
        time.sleep(1)
        logger.info("apply job success....")
    except:pass
    driver.switch_to_window(now_handle)
    

def custom_select_job():
    #自定义工作的选择，设定工作循环投递几页
    logger.info("start custom_select_job...")  
    for select_job_num in range(1,job_page_num):
        if select_job_num !=1:
            driver.find_element_by_link_text(str(select_job_num)).click()
        try:
            select_job()
            finish_job()
            logger.info("starting  "+str(select_job_num)+"  page....")
        except:pass
            
    logger.info(user_data[0]+'   is success!!!\n')

if __name__=="__main__":
    logger.info("###########cjol  job   logger################")
    read_company()#读取屏蔽公司名单到list
    count  = len(open('.//data//cjol_stu_info.txt','r').readlines())
    for user_num in range(1,count+1):
        try:
            driver = webdriver.Firefox()
            base_url = "http://www.cjol.com/JobSeekers/Login.aspx"
            driver.get(base_url)
            driver.maximize_window()
            driver.implicitly_wait(10)#全程智能等待页面加载完成
            user_data  = linecache.getline('.//data//cjol_stu_info.txt',user_num).strip('\n')
            user_data  = user_data.split('\t')
            logger.info( user_data)
            login_user()
            serach_save_job()
            custom_select_job()
            driver.quit()
        except:
            logger.info(user_data[0]+'   is failed!!!\n')
            driver.quit()     
    d2 = datetime.datetime.now()-d1
    logger.info('本次投递 '+str(count)+' 个学生的简历共计用时：'+str(d2))
    driver.quit()
    logger.info("###########cjol  job   end################")
