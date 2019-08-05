#encoding=gbk
###############prac1:实现登录注册功能，注册信息写入文件###########################


###############HomeWork:编写复杂点的员工系统###########################
## """
## 1.存储员工信息
## 2.查询员工信息(查询三种方式name，age，sal)
## 3.所有员工信息（格式化输出，对齐）
## 4.退出程序
## 5.修改(根据id 修改年龄、薪水)
## 6.删除(根据id删除)
## 使用文件操作
## """
def menu(menuMsg):
    """菜单选择函数，传入要显示的菜单信息，返回用户的选择值"""
    return raw_input(menuMsg)

def addEmp():
    """此函数实现新增员工信息的操作，返回成功或失败的提示信息"""
    empList=read_file("emp.txt")
    empInfor,empId,flag="","1",1
    if(len(empList)!=0):
        empId=str(int(empList[-1].split(" ")[0])+1)
    while(flag):
        empInfor=raw_input("—————\n请依次输入员工姓名、年龄、薪水(空格分开,年龄、薪水为数字):")
        if(len(empInfor.split(" "))==3 and checkFloat(empInfor.split(" ")[1]) and checkFloat(empInfor.split(" ")[2])):
            flag=0
        else:
            print("\n【ERROR】格式输入有误!请重新输入..")
    if(write_file("emp.txt",empId+" "+empInfor+"\n")):
        return "新增员工 (%s) 成功！"%empInfor
    else:
        return "新增员工 (%s) 失败！"%empInfor

def delEmp():
    """此函数实现删除员工信息的操作，返回成功或失败的提示信息"""
    empId=raw_input("请输入要删除员工的ID：")
    empList = read_file("emp.txt")
    emp=findEmp(empId)
    if(emp!=""):
        empList.remove(emp)
        if (write_file("emp.txt",empList,"w")):
            return "删除员工 %s 成功！" % empId
        else:
            return  "删除员工 %s 失败！" % empId
    else:
        return "没有查找到员工 %s ，删除失败！" % empId

def modifyEmp():
    """此函数实现修改员工信息的操作，返回成功或失败的提示信息"""
    empId = raw_input("请输入要修改员工的ID：")
    empList = read_file("emp.txt")
    emp = findEmp(empId)
    if (emp != ""):
        index=empList.index(emp)
        empList.remove(emp)
        print("当前员工信息为(ID name age sal):  %s"%emp)
        inforList=emp.split(" ")
        flag=1
        while(flag):
            newInfor=raw_input("请依次输入更新后的年龄和薪水信息:(空格隔开,只接收数字)")
            if (len(newInfor.split(" ")) == 2 and checkFloat(newInfor.split(" ")[0]) and checkFloat(newInfor.split(" ")[1])):
                flag=0
                newEmp=inforList[0]+" "+inforList[1]+" "+newInfor.split(" ")[0]+" "+newInfor.split(" ")[1]+"\n"
                empList.insert(index,newEmp)
                if(write_file("emp.txt",empList,"w")):
                    return "修改员工 %s 成功！" % empId
                else:
                    return "修改员工 %s 失败！" % empId
            else:
                print("\n【ERROR】格式输入有误!请重新输入..\n")
    else:
        return "没有查找到员工 %s ，修改失败！" % empId

def findEmp(empId):
    """此函数根据员工ID查找员工信息，若查找到则以字符串的形式返回员工信息，若没找到则返回空字符串"""
    empList = read_file("emp.txt")
    empInfor=""
    for emp in empList:
        if(empId==emp.split(" ")[0]):
            empInfor=emp
            break
    return empInfor

def findEmpsByMsg():
    """此函数根据用户输入的关键字信息查找出所有相关的员工信息，并返回查询到的信息"""
    empMsg=raw_input("请输入查询关键字：")
    empList = read_file("emp.txt")
    searchList=[]
    result=""
    for emp in empList:
        if empMsg in emp:
            searchList.append(emp)
    if(len(searchList)==0):
        result = "没有查找到任何有关 %s 的信息！"%empMsg
    else:
        result ="查询到的员工有:\n\t%-8s\t%-12s\t%-8s\t%-s\n———————————————————————————\n" % ("ID", "NAME", "AGE", "SAL")
        for i in searchList:
            emp = i.split(" ")
            result+="\t%-8s\t%-12s\t%-8s\t%-s"%(emp[0], emp[1], emp[2], emp[3])
    return result

def listAllEmp():
    """此函数用来返回所有员工信息"""
    empList = read_file("emp.txt")
    result=""
    if (len(empList) == 0):
        result = "员工列表:空"
    else:
        result = "全部员工列表为:\n\t%-8s\t%-12s\t%-8s\t%-s\n———————————————————————————\n"% ("ID","NAME", "AGE", "SAL")
        for i in empList:
            emp=i.split(" ")
            result += "\t%-8s\t%-12s\t%-8s\t%-s" % (emp[0],emp[1],emp[2],emp[3])
    return result

def checkFloat(str):
    """此函数检查字符串是否可以转换为数字，返回True或者False"""
    try:
        float(str)
        return True
    except:
        return False

def write_file(filename,data,mode="a"):
    """此函数用来向指定文件写入数据的操作，写入成功返回True,写入失败返回False"""
    try:
        empFile=open(filename,mode)
        empFile.writelines(data)
        empFile.close()
        return True
    except:
        return False

def read_file(filename):
    """此函数用来读入指定文件中的数据，并将读取的数据以列表的形式返回给调用处，若读取失败则返回空列表"""
    data=[]
    try:
        empFile=open(filename,"r")
        data=empFile.readlines()
        empFile.close()
    finally:
        return data

menu1="""————————————————————————————
  >>>>【 员工管理系统 】<<<<
\n\t1.新增员工信息
\t2.删除员工信息
\t3.修改员工信息
\t4.查询员工信息
\t5.列出所有员工
\t0.退出系统
============================
请输入您的选择："""
exit=1
while(exit):
    choice=menu(menu1)
    if(choice=="1"):
        print (addEmp())
        raw_input("===>回车继续...")
    elif(choice=="2"):
        print (delEmp())
        raw_input("===>回车继续...")
    elif(choice=="3"):
        print(modifyEmp())
        raw_input("===>回车继续...")
    elif (choice == "4"):
        print(findEmpsByMsg())
        raw_input("===>回车继续...")
    elif (choice == "5"):
        print(listAllEmp())
        raw_input("===>回车继续...")
    elif (choice == "0"):
        exit=0
        print("\n系统已安全退出...\n———————————————————————————— ")
    else:
        print("\n【ERROR】输入格式有误！按回车重新输入..")
        raw_input()

