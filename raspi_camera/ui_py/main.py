import pymysql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QCoreApplication
import random
from pill_ui2 import *

class main_form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.con = pymysql.connect(host='localhost', user='test', password='1234', db='pill_list', charset='utf8')

        self.cur = self.con.cursor()

        self.ui.btn_ch.clicked.connect(self.get_pill)

    def get_pill(self):
        sql = "select name, time, efficacy from pill where num = " + str(self.ui.num) + ";"
        self.cur.execute(sql)

        l = self.cur.fetchone()
        l = list(l)

        self.ui.cont_name.setText(l[0])
        self.ui.cont_time.setText(l[1])
        self.ui.cont_info.setText(l[2])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = main_form()
    m.show()
    sys.exit(app.exec_())
    
