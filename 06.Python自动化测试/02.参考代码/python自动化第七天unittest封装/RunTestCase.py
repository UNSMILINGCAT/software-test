#coding=utf-8
from Public import  HTMLTestRunner as HTMLTestRunner#导入英文报告
#from Public import  HTMLTestRunnerCN as HTMLTestRunner#导入中文报告
import unittest,time
from  Public.Sendmail import *
if __name__ == '__main__':
    test_dir = os.path.join(os.getcwd(),'TestCase')
    test_report = os.path.join(os.getcwd(), 'Report')
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = test_report+'/result_'+now+'.html'
    fp = open(filename,'wb')
    try:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="API测试报告",description='用例执行情况：')
        runner.run(discover)
        fp.close()
        send_mail(filename, "duandongbo@itleo.cn")
    except:
        fp.close()
        send_mail(filename,"duandongbo@itleo.cn")


