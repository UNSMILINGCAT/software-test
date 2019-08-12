# 定义一个函数，列出指定目录下所有的txt文件，并输出每个文件的创建日期和大小，格式如下
#  最后修改时间  文件大小  文件名    eg:2007-05-16  205  cmd.txt

# 提示:1.可使用os.listdir()及os.system()来做
#        2.如使用os.listdir()需使用os.stat()获得相应的属性
#           并输出
#        3.如使用os.system()需要解析字符串并重新输出。
# 比较两种方法的优缺点
import os,stat,time
path = "C:\\Users\\admin\\Desktop\\testOS"
filelist = os.listdir(path)
for ff in filelist:
    fo = open(path+"\\"+ff) #打开文件
    st = os.fstat(fo.fileno()) #获取文件的详细信息
    mdate = st[stat.ST_MTIME] #最后修改时间
    filesize = st[stat.ST_SIZE] #文件大小
    filename = ff #文件名
    fo.close()
    print(time.strftime("%Y-%m-%d",time.gmtime(mdate)),"\t",filesize,"\t",filename)

