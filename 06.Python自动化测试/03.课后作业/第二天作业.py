#coding=gbk
print "1.�洢Ա����Ϣ��"
print "2.��ѯԱ����Ϣ��"
print "3.����Ա����Ϣ��"
print "4.�˳�����"
list=[]
dit={}
while 1:
    choose=raw_input("��ѡ��[1-->4]:")
    if len(list)==0 and choose!="1":
        print "û��Ա����Ϣ���������Ա����Ϣ"
    else:
        if choose=="1":
            name=raw_input("������Ա��������")
            age=raw_input("������Ա�����䣺")
            sal=raw_input("������Ա�����ʣ�")
            dit={"name":name,"age":age,"sal":sal}
            list.append(dit)
        elif choose=="2":
            check=raw_input("ѡ���ѯԱ����name,age,sal��")
            if check in (list[0].keys()):
                name1 = raw_input("������Ա��"+check+"��")
                count = 0
                for i in range (len(list)):
                    if name1==list[i][check]:
                        print list[i]
                        count += 1
                if count ==0:
                    print "��Ա��������"
            else:
                print "ѡ�����"
        elif choose=="3":
            for i in range(len(list)):
                print "name:%s\tage:%s\tsal:%s\n"%(list[i]["name"],list[i]["age"],list[i]["sal"])
        elif choose=="4":
            exit()
        else:
            "�������"


