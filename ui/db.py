import pymysql

con = pymysql.connect(host='localhost', user='root', password='1234', db='test', charset='utf8')
cur = con.cursor()