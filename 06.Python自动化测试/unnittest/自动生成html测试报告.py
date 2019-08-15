import unittest,time
# 导入自动生成html测试报告的模块
# from HTMLTestRunner import HTMLTestRunner
from HTMLTestReportCN import HTMLTestRunner

if __name__ == "__main__":
    start_dir = r"E:\pythonCode\unnittest"
    discover = unittest.defaultTestLoader.discover(start_dir,pattern="test_*.py")

    # # 执行测试用例
    # runner = unittest.TextTestRunner()
    # runner.run(discover)
    with open(str(time.strftime('%Y%m%d%H%M%S'))+"report.html","wb") as fo:
       runner =  HTMLTestRunner(stream=fo,title="测试报告",description="系统登录的测试报告",tester="Linsir")
       runner.run(discover)
