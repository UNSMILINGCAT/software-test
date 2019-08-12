import csv
def innerA_txt():
    """保存用户信息到aaa.csv中"""
    with open('aaa.csv',mode='w',newline='') as csvfile:
        file=csv.writer(csvfile,dialect='excel')
        file.writerow(['用户名', '密码', '邮箱'])
        file.writerow(['admin', '123456', 'admin@163.com'])
        file.writerow(['hello', '123456', 'hello@163.com'])
        file.writerow(['love', '123456', 'love@163.com'])




#读取excel，字典显示
def out_dictionary():
    fo=open('aaa.csv',mode='r')
    distRead=csv.DictReader(fo)
    for row in distRead:
        print(row)


#读取excel，逐行显示
def out_line():
    fo=open('aaa.csv',mode='r')
    read=csv.reader(fo)
    for i in read:
        print(i)


# innerA_txt()  #第一题调用
out_dictionary()  #第二题调用
# out_line()  第三题调用
