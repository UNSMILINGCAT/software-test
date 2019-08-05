#coding=gbk
import os
from time import sleep
tips="""
#########################################################
#       欢迎使用新研员工信息管理系统                   #
#       版本：1.02                                      #
#       备注：函数化，增加权限控制                       #
#########################################################       
"""
menu="""
*********************************************************
    1.增加员工信息 
    2.修改员工信息 
    3.查询员工信息 
    4.显示所有员工信息 
    5.删除员工信息 
    6.退出
**********************************************************
"""
def Readfile(filepath,mode):
    data=[]
    with open(filepath,mode) as f:
        for line in f:
            line = line.strip()
            data.append(line)
    return data

def Writefile(filepath,data,mode='w'):
    if isinstance(data,list): #功能为去修改 删除信息
        fp = open(filepath, "w")
        for i in data:
            fp.write(i+'\n')
        fp.close()
    else:
        fp = open(filepath, mode)
        fp.write(data)
        fp.close()

def Add_emp(filepath):
    print "---员工初始密码为123456,权限默认为普通员工-----"
    name = raw_input("请输入姓名：")
    age = raw_input("请输入年龄：")
    sex = raw_input("请输入性别：")
    salary = raw_input("请输入工资：")
    data=name + "|" + age + "|" + sex + "|" + salary + '|123456'+'|1'+"\n"
    Writefile(filepath, data, "a")
    print "员工增加成功"

def All_emp(filepath):
    emplist=Readfile(filepath,"r")
    print "%-10s%-10s%-10s%-10s" % ("name", "age", "sex", "salary")
    for info1 in emplist:
        print "%-10s%-10s%-10s%-10s" % (
        info1.split("|")[0], info1.split("|")[1], info1.split("|")[2], info1.split("|")[3])

def Del_emp(filepath):
    if permission=="0":
        emplist = Readfile(filepath, "r")
        while 1:
            flag = 0
            name2 = raw_input('请输入要删除员工的用户名：')
            for info3 in emplist:
                if info3.split('|')[0] == name2:
                    flag += 1
                    count1 = emplist.index(info3)
                    del emplist[count1]
                    print name2 + "用户信息删除成功！"
                    Writefile(filepath,emplist)
            if flag == 0:
                print "没有查询到该用户的信息，请重试！"
            break
    else: print "没有权限，请联系管理员"
def Edit_emp(filepath):
    emplist = Readfile(filepath, "r")
    while 1:
        name1 = raw_input("请输入需要修改信息的员工姓名：")
        flag = 0
        for info1 in emplist:
            if info1.split("|")[0] == name1:
                flag += 1
                count = emplist.index(info1)
                salary1 = raw_input("请输入要修改的工资：")
                info1 = info1.split("|")[0] + "|" + info1.split("|")[1] + "|" + info1.split("|")[2] + "|" + salary1 \
                        +"|"+info1.split("|")[4]+"|"+info1.split("|")[5]
                emplist[count] = info1
                print name1 + "用户信息修改成功！"
                Writefile(filepath,emplist,"w")
        if flag == 0:
            print "您输入的用户名不存在，请重新输入！"
        break
def Query_emp(filepath):
    emplist = Readfile(filepath, "r")
    while 1:
        choose1 = raw_input("1.根据姓名查询 2.根据年龄查询 3.退出\n 请选择：")
        if choose1 == "1":
            flag = 0
            check1 = raw_input("请输入要查询的用户名：")
            print "%-10s%-10s%-10s%-10s" % ("name", "age", "sex", "salary")
            for info1 in emplist:
                if info1.split("|")[0] == check1:
                    flag += 1
                    print "%-10s%-10s%-10s%-10s" % (
                    info1.split("|")[0], info1.split("|")[1], info1.split("|")[2], info1.split("|")[3],
                    info1.split("|")[4], info1.split("|")[5])
            if flag == 0:
                print "没有查询到该用户的信息，请重试！"
        elif choose1 == "2":
            flag = False
            check2 = raw_input("请输入要查询的年龄：")
            print "%-10s%-10s%-10s%-10s" % ("name", "age", "sex", "salary")
            for info1 in emplist:
                if info1.split("|")[1] == check2:
                    flag = True
                    print "%-10s%-10s%-10s%-10s" % (
                    info1.split("|")[0], info1.split("|")[1], info1.split("|")[2], info1.split("|")[3],
                    info1.split("|")[4],info1.split("|")[5])
            if flag == False:
                print "没有查询到该用户的信息，请重试！"
        elif choose1 == "3":
            break
        else:
            print "没有该选项，请重新输入！"

def Init_sys(filepath):
    data="admin|23|1|0000|admin123|0\n"
    if not os.path.exists(filepath):
        Writefile(filepath,data,"w")
        sleep(0.5)
    emplist=Readfile(filepath,"r")
    flag  = 0
    count = 0
    while True:
        loginname=raw_input("请输入用户名：")
        loginpasswd=raw_input("请输入密码：")
        for emp  in emplist:
            if loginname==emp.split("|")[0] and loginpasswd==emp.split("|")[4]:
                flag+=1
                global permission
                permission=emp.split("|")[5]
                print "登录成功"
                return True
                break
        if flag==0:
            count += 1
            print "登录失败，请重试！还剩余%s次机会"%(3-count)
            if count==3:
                print "3次机会已经用完，程序退出！"
                return False
                exit()

def Main(filepath):
    os.system("cls")
    print menu
    choose = raw_input("请选择：")
    if   choose=="1":    Add_emp(filepath)
    elif choose=="2":    Edit_emp(filepath)
    elif choose=="3":    Query_emp(filepath)
    elif choose=="4":    All_emp(filepath)
    elif choose=="5":    Del_emp(filepath)
    elif choose=="6":    exit()
    else: print "没有该选项，请重新输入！"

if __name__ == '__main__':
    permission=""
    print tips
    if  Init_sys('userdata'):
        if permission=="0":
            print "欢迎回来，管理员"
        while True:
            Main('userdata')