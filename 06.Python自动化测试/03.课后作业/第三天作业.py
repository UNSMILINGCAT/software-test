#encoding=gbk
###############prac1:ʵ�ֵ�¼ע�Ṧ�ܣ�ע����Ϣд���ļ�###########################


###############HomeWork:��д���ӵ��Ա��ϵͳ###########################
## """
## 1.�洢Ա����Ϣ
## 2.��ѯԱ����Ϣ(��ѯ���ַ�ʽname��age��sal)
## 3.����Ա����Ϣ����ʽ����������룩
## 4.�˳�����
## 5.�޸�(����id �޸����䡢нˮ)
## 6.ɾ��(����idɾ��)
## ʹ���ļ�����
## """
def menu(menuMsg):
    """�˵�ѡ����������Ҫ��ʾ�Ĳ˵���Ϣ�������û���ѡ��ֵ"""
    return raw_input(menuMsg)

def addEmp():
    """�˺���ʵ������Ա����Ϣ�Ĳ��������سɹ���ʧ�ܵ���ʾ��Ϣ"""
    empList=read_file("emp.txt")
    empInfor,empId,flag="","1",1
    if(len(empList)!=0):
        empId=str(int(empList[-1].split(" ")[0])+1)
    while(flag):
        empInfor=raw_input("����������\n����������Ա�����������䡢нˮ(�ո�ֿ�,���䡢нˮΪ����):")
        if(len(empInfor.split(" "))==3 and checkFloat(empInfor.split(" ")[1]) and checkFloat(empInfor.split(" ")[2])):
            flag=0
        else:
            print("\n��ERROR����ʽ��������!����������..")
    if(write_file("emp.txt",empId+" "+empInfor+"\n")):
        return "����Ա�� (%s) �ɹ���"%empInfor
    else:
        return "����Ա�� (%s) ʧ�ܣ�"%empInfor

def delEmp():
    """�˺���ʵ��ɾ��Ա����Ϣ�Ĳ��������سɹ���ʧ�ܵ���ʾ��Ϣ"""
    empId=raw_input("������Ҫɾ��Ա����ID��")
    empList = read_file("emp.txt")
    emp=findEmp(empId)
    if(emp!=""):
        empList.remove(emp)
        if (write_file("emp.txt",empList,"w")):
            return "ɾ��Ա�� %s �ɹ���" % empId
        else:
            return  "ɾ��Ա�� %s ʧ�ܣ�" % empId
    else:
        return "û�в��ҵ�Ա�� %s ��ɾ��ʧ�ܣ�" % empId

def modifyEmp():
    """�˺���ʵ���޸�Ա����Ϣ�Ĳ��������سɹ���ʧ�ܵ���ʾ��Ϣ"""
    empId = raw_input("������Ҫ�޸�Ա����ID��")
    empList = read_file("emp.txt")
    emp = findEmp(empId)
    if (emp != ""):
        index=empList.index(emp)
        empList.remove(emp)
        print("��ǰԱ����ϢΪ(ID name age sal):  %s"%emp)
        inforList=emp.split(" ")
        flag=1
        while(flag):
            newInfor=raw_input("������������º�������нˮ��Ϣ:(�ո����,ֻ��������)")
            if (len(newInfor.split(" ")) == 2 and checkFloat(newInfor.split(" ")[0]) and checkFloat(newInfor.split(" ")[1])):
                flag=0
                newEmp=inforList[0]+" "+inforList[1]+" "+newInfor.split(" ")[0]+" "+newInfor.split(" ")[1]+"\n"
                empList.insert(index,newEmp)
                if(write_file("emp.txt",empList,"w")):
                    return "�޸�Ա�� %s �ɹ���" % empId
                else:
                    return "�޸�Ա�� %s ʧ�ܣ�" % empId
            else:
                print("\n��ERROR����ʽ��������!����������..\n")
    else:
        return "û�в��ҵ�Ա�� %s ���޸�ʧ�ܣ�" % empId

def findEmp(empId):
    """�˺�������Ա��ID����Ա����Ϣ�������ҵ������ַ�������ʽ����Ա����Ϣ����û�ҵ��򷵻ؿ��ַ���"""
    empList = read_file("emp.txt")
    empInfor=""
    for emp in empList:
        if(empId==emp.split(" ")[0]):
            empInfor=emp
            break
    return empInfor

def findEmpsByMsg():
    """�˺��������û�����Ĺؼ�����Ϣ���ҳ�������ص�Ա����Ϣ�������ز�ѯ������Ϣ"""
    empMsg=raw_input("�������ѯ�ؼ��֣�")
    empList = read_file("emp.txt")
    searchList=[]
    result=""
    for emp in empList:
        if empMsg in emp:
            searchList.append(emp)
    if(len(searchList)==0):
        result = "û�в��ҵ��κ��й� %s ����Ϣ��"%empMsg
    else:
        result ="��ѯ����Ա����:\n\t%-8s\t%-12s\t%-8s\t%-s\n������������������������������������������������������\n" % ("ID", "NAME", "AGE", "SAL")
        for i in searchList:
            emp = i.split(" ")
            result+="\t%-8s\t%-12s\t%-8s\t%-s"%(emp[0], emp[1], emp[2], emp[3])
    return result

def listAllEmp():
    """�˺���������������Ա����Ϣ"""
    empList = read_file("emp.txt")
    result=""
    if (len(empList) == 0):
        result = "Ա���б�:��"
    else:
        result = "ȫ��Ա���б�Ϊ:\n\t%-8s\t%-12s\t%-8s\t%-s\n������������������������������������������������������\n"% ("ID","NAME", "AGE", "SAL")
        for i in empList:
            emp=i.split(" ")
            result += "\t%-8s\t%-12s\t%-8s\t%-s" % (emp[0],emp[1],emp[2],emp[3])
    return result

def checkFloat(str):
    """�˺�������ַ����Ƿ����ת��Ϊ���֣�����True����False"""
    try:
        float(str)
        return True
    except:
        return False

def write_file(filename,data,mode="a"):
    """�˺���������ָ���ļ�д�����ݵĲ�����д��ɹ�����True,д��ʧ�ܷ���False"""
    try:
        empFile=open(filename,mode)
        empFile.writelines(data)
        empFile.close()
        return True
    except:
        return False

def read_file(filename):
    """�˺�����������ָ���ļ��е����ݣ�������ȡ���������б����ʽ���ظ����ô�������ȡʧ���򷵻ؿ��б�"""
    data=[]
    try:
        empFile=open(filename,"r")
        data=empFile.readlines()
        empFile.close()
    finally:
        return data

menu1="""��������������������������������������������������������
  >>>>�� Ա������ϵͳ ��<<<<
\n\t1.����Ա����Ϣ
\t2.ɾ��Ա����Ϣ
\t3.�޸�Ա����Ϣ
\t4.��ѯԱ����Ϣ
\t5.�г�����Ա��
\t0.�˳�ϵͳ
============================
����������ѡ��"""
exit=1
while(exit):
    choice=menu(menu1)
    if(choice=="1"):
        print (addEmp())
        raw_input("===>�س�����...")
    elif(choice=="2"):
        print (delEmp())
        raw_input("===>�س�����...")
    elif(choice=="3"):
        print(modifyEmp())
        raw_input("===>�س�����...")
    elif (choice == "4"):
        print(findEmpsByMsg())
        raw_input("===>�س�����...")
    elif (choice == "5"):
        print(listAllEmp())
        raw_input("===>�س�����...")
    elif (choice == "0"):
        exit=0
        print("\nϵͳ�Ѱ�ȫ�˳�...\n�������������������������������������������������������� ")
    else:
        print("\n��ERROR�������ʽ���󣡰��س���������..")
        raw_input()

