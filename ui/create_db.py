import pymysql
import cv2

con = pymysql.connect(host='localhost', user='test', password='1234', db='test', charset='utf8')


cur = con.cursor()

sql = "select path from image where name = '1';"


cur.execute(sql)

data = cur.fetchall()
path = str(data[0][0])

img = cv2.imread(path)
cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()

con.close()




