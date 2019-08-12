# fo = open("aaa.txt","r",encoding="utf8")
#
# for row in fo.readlines():
#     print(row)
#
# fo.close()

# with open("aaa.txt","r",encoding="utf8") as ff:
#     for row in ff.readlines():
#         print(row)
#     ff.close()

# fo = open("aaa.txt","a",encoding="utf8")
# fo.write("呵呵哒")
#
# fo.close()

# with open("aaa.txt","w",encoding="utf8") as ff:
#    ff.write("""
#    ####################33
#    哈哈哈哈
#    %%%%%%%%%%%%
#    """)
#    ff.close()

# import csv
# fo = open("bbb.csv","w",encoding="utf8",newline="")
# w = csv.writer(fo,dialect="excel")
# w.writerow(["姓名","年龄","成绩"])
# w.writerow(["aaa",18,88])
# w.writerow(["bbb",22,98])
# w.writerow(["ccc",23,89])
#
# fo.close()

import csv

fo = open("bbb.csv","r",encoding="utf8")
reader = csv.reader(fo)
for i  in reader:
    print(i)

fo.close()