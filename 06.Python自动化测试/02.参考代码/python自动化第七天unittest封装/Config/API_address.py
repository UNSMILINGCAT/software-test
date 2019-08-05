#coding=utf-8

#get
"""
1.get方法 （返回数据为json）
1.1历史上的今天（http://www.ipip5.com/today/api.php?type=json）
   入参一个，type是代表后台返回数据结果的类型
1.2查询今天的天气（http://wthrcdn.etouch.cn/weather_mini?city=%E5%8C%97%E4%BA%AC）
   入参一个，city是城市编码，例如深圳，上海；接口中需要把城市转码为url编码
1.3查询ip归属地（https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=1.1.1.1&co=&resource_id=6006）
   入参三个，query是要查询的ip；co未知，recourse_id是查询机器的编号
1.4快递100接口查询（https://www.kuaidi100.com/query?type=yuantong&postid=123456）
   入参2个，type是什么快递的拼音；postid是快递单号
1.5火车票站点数据查询（https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018）
   入参一个，站点的版本号；因为每段时间都会有新的火车站开通
1.6火车票余票查询接口（https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-14&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT）
   入参四个：购票日期  起点站编码  终点站编码  成人票 （例子是 北京-广州 8月14号的余票）
1.7火车票票价查询（https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=2400000Z3501&from_station_no=01&to_station_no=05&seat_types=14163&train_date=2017-08-14）
   入参五个；依次为列车编码、起点站编号、终点站编号、席位类型、查询日期
1.8查询火车时刻表停靠站点数据（https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=2400000Z3501&from_station_telecode=BXP&to_station_telecode=GZQ&depart_date=2017-08-14）
   入参4个；依次为列车编码、起点站编码、终点站编码、查询日期
"""
#post
"""
1.1 sina邮箱验证是否被注册（https://login.sina.com.cn/signup/check_user.php）
    入参3个：{"name":"tangzhanggai11@163.com","format":"json","from":"othermail"}
    请求头：headers={'Content-Type': 'application/x-www-form-urlencoded'})
"""
