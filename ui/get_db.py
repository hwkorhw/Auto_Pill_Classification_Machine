import pymysql

pymysql.install_as_MySQLdb()

def get_data():
    pymysql.install_as_MySQLdb()

    con = pymysql.connect(host='localhost', user='raspi', password='1234', db='pill_db', charset='utf8')

    cur = con.cursor()

    sql = "select num from pill;"

    cur.execute(sql)

    data = cur.fetchall()
    num = list()

    for i in data:
        num.append(str(i[0]))

    con.close()

    return num

def get_one(n):
    pymysql.install_as_MySQLdb()

    con = pymysql.connect(host='localhost', user='raspi', password='1234', db='pill_db', charset='utf8')

    cur = con.cursor()
    print("db")
    sql = "select name, time, efficacy from pill where num = " + str(n) + ";"

    cur.execute(sql)

    data = cur.fetchall()
    data = list(data[0])

    con.close()

    return data