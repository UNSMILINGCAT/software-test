#coding=utf-8
##################################################class类###########################################################
# 定义类
class Person:
    '''这是一个描述人的类'''
    # 类方法
    # self指代当前对象p
    def eat(self):
        # print "He/She is eating!"
        print "%s is eating!" % self.name
    def work(self):
        print "He/She is working!"

# 定义类
class Person:
    '''这是一个描述人的类'''

    # 构造函数
    def __init__(self, name, age, height):
        # print "In __init__ func."
        # 初始化三个属性
        self.name = name
        self.age = age
        self.height = height
        return

    # 类方法
    # self指代当前对象p
    def eat(self, food):
        print "%s is eating %s!" % (self.name, food)

    def work(self):
        print "%s is working!" % self.name

if __name__ == '__main__':
    # 创建对象
    p = Person("jack", 17, 1.75)
    p1 = Person("lucy", 27, 1.65)
    # print "对象创建成功"


    # 调用类方法: 对象.方法()
    p.eat("apple")
    p1.eat("banana")
    p.work()

##################################################类的练习实例######################################################
# 一个银行账户的类
class Account:
    "这是一个银行账户的类"
    # 类变量,不属于某个对象,属于类
    count = 0

    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money
        Account.count += 1
        return

    # 查询余额
    def check(self):
        return self.money

    # 存钱
    def deposit(self, amount):
        "存钱成功返回True,否则返回False"
        if amount <= 0:
            print "存钱失败"
            return False
        self.money += amount
        return True

    # 取钱
    def withdraw(self, amount):
        if amount <= 0:
            # print "取钱金额不能小于等于0"
            return False
        elif amount > self.money:
            # print "余额不足!"
            return False
        else:
            self.money -= amount
            print "取钱成功"
            return True


if __name__ == '__main__':
    ac = Account('jack', "11223344", 1000)
    print "账户余额:", ac.check()
    ac.deposit(2500)
    print "存了2500后,账户余额:", ac.check()
    if not ac.withdraw(3000):
        #     if not ac.withdraw(5000):
        print "取钱失败!"
    print "账户余额:", ac.check()

    ac1 = Account('mary', "11223355", 1000)

    # 访问类变量方法: 类.类变量
    print "当前程序一共创建了%d个Account对象" % Account.count
##################################################父类子类派生类####################################################
# 一个银行账户的类
class Account:
    "这是一个银行账户的类"
    # 类变量,不属于某个对象,属于类
    count = 0

    def __init__(self, name, number, money):
        self.name = name
        self.number = number
        self.money = money
        Account.count += 1
        return

    # 查询余额
    def check(self):
        return self.money

    # 存钱
    def deposit(self, amount):
        "存钱成功返回True,否则返回False"
        if amount <= 0:
            print "存钱失败"
            return False
        self.money += amount
        return True

    # 取钱
    def withdraw(self, amount):
        if amount <= 0:
            # print "取钱金额不能小于等于0"
            return False
        elif amount > self.money:
            # print "余额不足!"
            return False
        else:
            self.money -= amount
            print "取钱成功"
            return True

# Account 父类, 基类,超类super
# VipAccount 子类,派生类
# VIP账户的类
class VipAccount(Account):
    "这是一个VIP账户的类"

    def __init__(self, name, number, money, overdraft):
        self.name = name
        self.number = number
        self.money = money
        self.overdraft = overdraft
        return

    # 覆写父类方法 override
    def withdraw(self, amount):
        if amount <= 0:
            # print "取钱金额不能小于等于0"
            return False
        elif amount > self.money + self.overdraft:
            # print "余额不足!"
            return False
        else:
            self.money -= amount
            # print "取钱成功"
            return True
    # 子类添加新方法
    def order(self, drink):
        print "Give me a %s" % drink

if __name__ == '__main__':
    v1 = VipAccount("jack", '11223344', 500, 1000)
    print "账户余额是:", v1.check()
    if not v1.withdraw(1500):
        #     if not v1.withdraw(2000):
        print "取钱失败!"
    print "账户余额是:", v1.check()
    v1.deposit(2500)
    print "账户余额是:", v1.check()
    v1.order("java")
##################################################unittest单元测试框架###############################################
import unittest
import testfunc
# 定义测试用例的类
class Maths(unittest.TestCase):
    # 类里每一个test开头的方法对应一个测试用例
    def test_add(self):
        self.assertEqual(testfunc.add(3, 5), 8, "3 + 5 != 8,用例执行失败!")
    def test_sub(self):
        self.assertEqual(testfunc.sub(3, 5), -2, "3 -5 != -2,用例执行失败!")
if __name__ == '__main__':
    unittest.main()

#######################################################单元测试用例###################################################
import unittest
import testclass
class Foo(unittest.TestCase):
    # 执行每个测试用例函数之前会先执行setUp,初始化执行环境
    def setUp(self):
        # print "setUp..."
        self.m = testclass.Maths()

    def test_add(self):
        m = self.m
        ret = m.add(3, 5)
        self.assertEqual(ret, 8, "3 + 5 != 8")

    def test_sub(self):
        m = self.m
        ret = m.sub(3, 5)
        self.assertEqual(ret, -2, "3 - 5 != -2")

    def test_mul(self):
        m = self.m
        ret = m.mul(3, 5)
        self.assertEqual(ret, 15, "3 * 5 != 15")

    # 执行完每个测试用例函数后,会执行tearDown函数,清理执行环境
    def tearDown(self):
        del self.m

if __name__ == '__main__':
    # unittest.main()
    # 创建测试套件
    ts = unittest.TestSuite()

    # 把测试用例添加到测试套件
    ts.addTest(Foo('test_add'))
    ts.addTest(Foo('test_mul'))

    # 创建可以执行测试套件的对象
    runner = unittest.TextTestRunner()
    # 执行测试套件
    # runner.run(ts)
    runner.run(Foo("test_add"))
