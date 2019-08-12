#time模块
import time
print(time.time())   # 获取当前时间的时间戳（当前时间距离1970年1月1日0点0分0秒的时间秒差）
print(time.localtime())  # 获取当前时间的元组
print(time.ctime())    #获取当前时间的字符串

# 将元组的日期转化为字符串日期
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#将元组转化为秒
print(time.mktime(time.localtime()))
#将秒转化为元组
print(time.gmtime(1566336823))
#将秒转化为字符串
print(time.ctime(1566336823))


#sleep 休眠
# time.sleep(3)

#关于时区
print(time.timezone)  # 时区对应的秒  东八区  -28800   -8*60*60
print(time.tzname)  # 时区名称

