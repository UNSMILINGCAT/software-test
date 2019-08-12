#比较运算符
# >  <  >=  <=  ==  !=
print('a'>'b')  #Ascll比较   a=65   A=97

#逻辑运算符  结果就是bool值
# and  or  not
print(6>5 and 10>8)
print(3>5 and 10>8)
#结论：and运算符，有一假（false）则为假

print(3>5 or 10>8)
print(3>5 or 10>12)
#结论：or运算符，有一真（true）则真

print(not (3>5 and 10>12))
#结论：not运算符，如果为true则加上not变成false,反之，false变为true

age=int(input("请输入您的芳龄:"))
print("旧的写法：",age>=18 and age<=22)
print("新的写法：",18<=age<=22)
