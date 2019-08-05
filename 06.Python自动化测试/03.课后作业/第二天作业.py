#coding=gbk
print "1.存储员工信息："
print "2.查询员工信息："
print "3.所有员工信息："
print "4.退出程序"
list=[]
dit={}
while 1:
    choose=raw_input("请选择[1-->4]:")
    if len(list)==0 and choose!="1":
        print "没有员工信息，请先添加员工信息"
    else:
        if choose=="1":
            name=raw_input("请输入员工姓名：")
            age=raw_input("请输入员工年龄：")
            sal=raw_input("请输入员工工资：")
            dit={"name":name,"age":age,"sal":sal}
            list.append(dit)
        elif choose=="2":
            check=raw_input("选择查询员工（name,age,sal）")
            if check in (list[0].keys()):
                name1 = raw_input("请输入员工"+check+"：")
                count = 0
                for i in range (len(list)):
                    if name1==list[i][check]:
                        print list[i]
                        count += 1
                if count ==0:
                    print "该员工不存在"
            else:
                print "选择错误"
        elif choose=="3":
            for i in range(len(list)):
                print "name:%s\tage:%s\tsal:%s\n"%(list[i]["name"],list[i]["age"],list[i]["sal"])
        elif choose=="4":
            exit()
        else:
            "输入错误"


