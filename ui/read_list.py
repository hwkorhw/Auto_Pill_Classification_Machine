import csv
import pymysql
import cv2

list_p = list()

with open('/home/hw/pill_image/list_pill.csv', 'r') as f:
    reader = csv.reader(f)

    for i in reader:
        list_p.append(i)

name_list = list()
num_list = list()
time_list = list()
eff_list = list()

for i in range(1,61):
    name_list.append(list_p[i][1])
    num_list.append(list_p[i][0])
    time_list.append(list_p[i][4])
    eff_list.append(list_p[i][3])

con = pymysql.connect(host='localhost', user='test', password='1234', db='pill_list', charset='utf8')

cur = con.cursor()

for i in range(60):
    sql = "insert into pill values("+num_list[i]+",\'"+name_list[i]+"\',\'"+time_list[i]+"\',\'"+eff_list[i]+"\');"

    cur.execute(sql)
    con.commit()
    print("success")

con.close()



