# 1.编写程序，将以下内容写入csv文件中aaa.csv
#  用户名    密码       邮箱
#  admin    123456   admin@163.com
#  hello    123456   hello@126.com
#  love     123321   love@163.com
import csv
def innerA_txt():
    """保存用户信息到aaa.csv中"""
    with open('aaa.csv',mode='w',newline='') as csvfile:
        file=csv.writer(csvfile,dialect='excel')
        file.writerow(['用户名', '密码', '邮箱'])
        file.writerow(['admin', '123456', 'admin@163.com'])
        file.writerow(['hello', '123456', 'hello@163.com'])
        file.writerow(['love', '123456', 'love@163.com'])

# innerA_txt()
# 2.编写程序，读取aaa.csv文件的内容，逐行显示


#扩展 3.编写程序，读取aaa.csv文件内容，转化为字典然后遍历字典进行显示
def out_dictionary():
    fo=open('aaa.csv',mode='r')
    csv_file = csv.reader(fo)
    csv_title = next(csv_file)  #next() 获取第一行的元素
    # print(next(csv_title))
    distRead=csv.DictReader(fo,csv_title)
    for row in distRead:
        # print(row,type(row))
        adict = {}
        for k,v in row.items():
            adict[k] = v
        print(adict)

out_dictionary()
