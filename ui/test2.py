# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rot1_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import test_db

class test2_ui(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.num = 9
        self.lbl1 = QtWidgets.QPushButton(MainWindow)
        self.lbl1.setGeometry(QtCore.QRect(20, 10, 100, 100))
        self.lbl1.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QPushButton(MainWindow)
        self.lbl2.setGeometry(QtCore.QRect(130, 50, 100, 100))
        self.lbl2.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QPushButton(MainWindow)
        self.lbl3.setGeometry(QtCore.QRect(230, 110, 100, 100))
        self.lbl3.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl3.setObjectName("lbl3")
        self.lbl4 = QtWidgets.QPushButton(MainWindow)
        self.lbl4.setGeometry(QtCore.QRect(320, 180, 100, 100))
        self.lbl4.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl4.setObjectName("lbl4")
        self.lbl5 = QtWidgets.QPushButton(MainWindow)
        self.lbl5.setGeometry(QtCore.QRect(410, 250, 100, 100))
        self.lbl5.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl5.setObjectName("lbl5")
        self.lbl6 = QtWidgets.QPushButton(MainWindow)
        self.lbl6.setGeometry(QtCore.QRect(490, 330, 100, 100))
        self.lbl6.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl6.setObjectName("lbl6")
        self.lbl7 = QtWidgets.QPushButton(MainWindow)
        self.lbl7.setGeometry(QtCore.QRect(560, 420, 100, 100))
        self.lbl7.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl7.setObjectName("lbl7")
        self.lbl8 = QtWidgets.QPushButton(MainWindow)
        self.lbl8.setGeometry(QtCore.QRect(630, 510, 100, 100))
        self.lbl8.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl8.setObjectName("lbl8")
        self.lbl9 = QtWidgets.QPushButton(MainWindow)
        self.lbl9.setGeometry(QtCore.QRect(690, 610, 100, 100))
        self.lbl9.setStyleSheet("border-style: solid; border-width: 10px; border-color: #666666; border-radius: 50px;")
        self.lbl9.setObjectName("lbl9")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        list_p = test_db.pill_test()
        self.lbl1.setText(_translate("MainWindow", list_p[0 + self.num]))
        self.lbl2.setText(_translate("MainWindow", list_p[1 + self.num]))
        self.lbl3.setText(_translate("MainWindow", list_p[2 + self.num]))
        self.lbl4.setText(_translate("MainWindow", list_p[3 + self.num]))
        self.lbl5.setText(_translate("MainWindow", list_p[4 + self.num]))
        self.lbl6.setText(_translate("MainWindow", list_p[5 + self.num]))
        self.lbl7.setText(_translate("MainWindow", list_p[6 + self.num]))
        self.lbl8.setText(_translate("MainWindow", list_p[7 + self.num]))
        self.lbl9.setText(_translate("MainWindow", list_p[8 + self.num]))