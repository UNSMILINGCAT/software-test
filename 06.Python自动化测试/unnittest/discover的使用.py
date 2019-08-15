import unittest

if __name__ == "__main__":
    start_dir = r"E:\pythonCode\unnittest"
    discover = unittest.defaultTestLoader.discover(start_dir,pattern="test_*.py")
    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(discover)