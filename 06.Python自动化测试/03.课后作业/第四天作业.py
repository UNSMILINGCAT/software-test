#coding=gbk
import os
from time import sleep
tips="""
#########################################################
#       ��ӭʹ������Ա����Ϣ����ϵͳ                   #
#       �汾��1.02                                      #
#       ��ע��������������Ȩ�޿���                       #
#########################################################       
"""
menu="""
*********************************************************
    1.����Ա����Ϣ 
    2.�޸�Ա����Ϣ 
    3.��ѯԱ����Ϣ 
    4.��ʾ����Ա����Ϣ 
    5.ɾ��Ա����Ϣ 
    6.�˳�
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
    if isinstance(data,list): #����Ϊȥ�޸� ɾ����Ϣ
        fp = open(filepath, "w")
        for i in data:
            fp.write(i+'\n')
        fp.close()
    else:
        fp = open(filepath, mode)
        fp.write(data)
        fp.close()

def Add_emp(filepath):
    print "---Ա����ʼ����Ϊ123456,Ȩ��Ĭ��Ϊ��ͨԱ��-----"
    name = raw_input("������������")
    age = raw_input("���������䣺")
    sex = raw_input("�������Ա�")
    salary = raw_input("�����빤�ʣ�")
    data=name + "|" + age + "|" + sex + "|" + salary + '|123456'+'|1'+"\n"
    Writefile(filepath, data, "a")
    print "Ա�����ӳɹ�"

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
            name2 = raw_input('������Ҫɾ��Ա�����û�����')
            for info3 in emplist:
                if info3.split('|')[0] == name2:
                    flag += 1
                    count1 = emplist.index(info3)
                    del emplist[count1]
                    print name2 + "�û���Ϣɾ���ɹ���"
                    Writefile(filepath,emplist)
            if flag == 0:
                print "û�в�ѯ�����û�����Ϣ�������ԣ�"
            break
    else: print "û��Ȩ�ޣ�����ϵ����Ա"
def Edit_emp(filepath):
    emplist = Readfile(filepath, "r")
    while 1:
        name1 = raw_input("��������Ҫ�޸���Ϣ��Ա��������")
        flag = 0
        for info1 in emplist:
            if info1.split("|")[0] == name1:
                flag += 1
                count = emplist.index(info1)
                salary1 = raw_input("������Ҫ�޸ĵĹ��ʣ�")
                info1 = info1.split("|")[0] + "|" + info1.split("|")[1] + "|" + info1.split("|")[2] + "|" + salary1 \
                        +"|"+info1.split("|")[4]+"|"+info1.split("|")[5]
                emplist[count] = info1
                print name1 + "�û���Ϣ�޸ĳɹ���"
                Writefile(filepath,emplist,"w")
        if flag == 0:
            print "��������û��������ڣ����������룡"
        break
def Query_emp(filepath):
    emplist = Readfile(filepath, "r")
    while 1:
        choose1 = raw_input("1.����������ѯ 2.���������ѯ 3.�˳�\n ��ѡ��")
        if choose1 == "1":
            flag = 0
            check1 = raw_input("������Ҫ��ѯ���û�����")
            print "%-10s%-10s%-10s%-10s" % ("name", "age", "sex", "salary")
            for info1 in emplist:
                if info1.split("|")[0] == check1:
                    flag += 1
                    print "%-10s%-10s%-10s%-10s" % (
                    info1.split("|")[0], info1.split("|")[1], info1.split("|")[2], info1.split("|")[3],
                    info1.split("|")[4], info1.split("|")[5])
            if flag == 0:
                print "û�в�ѯ�����û�����Ϣ�������ԣ�"
        elif choose1 == "2":
            flag = False
            check2 = raw_input("������Ҫ��ѯ�����䣺")
            print "%-10s%-10s%-10s%-10s" % ("name", "age", "sex", "salary")
            for info1 in emplist:
                if info1.split("|")[1] == check2:
                    flag = True
                    print "%-10s%-10s%-10s%-10s" % (
                    info1.split("|")[0], info1.split("|")[1], info1.split("|")[2], info1.split("|")[3],
                    info1.split("|")[4],info1.split("|")[5])
            if flag == False:
                print "û�в�ѯ�����û�����Ϣ�������ԣ�"
        elif choose1 == "3":
            break
        else:
            print "û�и�ѡ����������룡"

def Init_sys(filepath):
    data="admin|23|1|0000|admin123|0\n"
    if not os.path.exists(filepath):
        Writefile(filepath,data,"w")
        sleep(0.5)
    emplist=Readfile(filepath,"r")
    flag  = 0
    count = 0
    while True:
        loginname=raw_input("�������û�����")
        loginpasswd=raw_input("���������룺")
        for emp  in emplist:
            if loginname==emp.split("|")[0] and loginpasswd==emp.split("|")[4]:
                flag+=1
                global permission
                permission=emp.split("|")[5]
                print "��¼�ɹ�"
                return True
                break
        if flag==0:
            count += 1
            print "��¼ʧ�ܣ������ԣ���ʣ��%s�λ���"%(3-count)
            if count==3:
                print "3�λ����Ѿ����꣬�����˳���"
                return False
                exit()

def Main(filepath):
    os.system("cls")
    print menu
    choose = raw_input("��ѡ��")
    if   choose=="1":    Add_emp(filepath)
    elif choose=="2":    Edit_emp(filepath)
    elif choose=="3":    Query_emp(filepath)
    elif choose=="4":    All_emp(filepath)
    elif choose=="5":    Del_emp(filepath)
    elif choose=="6":    exit()
    else: print "û�и�ѡ����������룡"

if __name__ == '__main__':
    permission=""
    print tips
    if  Init_sys('userdata'):
        if permission=="0":
            print "��ӭ����������Ա"
        while True:
            Main('userdata')