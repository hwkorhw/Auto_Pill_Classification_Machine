# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rot1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QDialog

class rot2(object):
    def __init__(self,MainWindow):
        super().__init__()
        MainWindow.setObjectName("sub")
        MainWindow.resize(800, 800)
        img = QImage('rot1.jpeg')
        p = QPalette()
        p.setBrush(10, QBrush(img))
        MainWindow.setPalette(p)
        self.colorlist = ['#ff0000', '#ff6600', '#ffcc00', '#99cc33', '#003300', '#0066cc', '#000033', '#663399', '#ff6699', '#666666']
        self.lbl1 = QtWidgets.QLabel(MainWindow)
        self.lbl1.setGeometry(QtCore.QRect(50, 286, 50, 50))
        self.lbl1.setObjectName("lbl1")
        self.lbl1.setStyleSheet("color: #ff0000;")
        self.lbl1.setFont(QFont('맑은 고딕', 15))
        self.lbl2 = QtWidgets.QLabel(MainWindow)
        self.lbl2.setGeometry(QtCore.QRect(125, 308, 50, 50))
        self.lbl2.setObjectName("lbl2")
        self.lbl2.setStyleSheet("color: #ff6600;")
        self.lbl2.setFont(QFont('맑은 고딕', 15))
        self.lbl3 = QtWidgets.QLabel(MainWindow)
        self.lbl3.setGeometry(QtCore.QRect(195, 339, 40, 40))
        self.lbl3.setObjectName("lbl3")
        self.lbl3.setStyleSheet("color: #ffcc00;")
        self.lbl3.setFont(QFont('맑은 고딕', 15))
        self.lbl4 = QtWidgets.QLabel(MainWindow)
        self.lbl4.setGeometry(QtCore.QRect(265, 385, 40, 40))
        self.lbl4.setObjectName("lbl4")
        self.lbl4.setStyleSheet("color: #99cc33;")
        self.lbl4.setFont(QFont('맑은 고딕', 15))
        self.lbl5 = QtWidgets.QLabel(MainWindow)
        self.lbl5.setGeometry(QtCore.QRect(325, 435, 40, 40))
        self.lbl5.setObjectName("lbl5")
        self.lbl5.setStyleSheet("color: #003300;")
        self.lbl5.setFont(QFont('맑은 고딕', 15))
        self.lbl6 = QtWidgets.QLabel(MainWindow)
        self.lbl6.setGeometry(QtCore.QRect(370, 490, 40, 40))
        self.lbl6.setObjectName("lbl6")
        self.lbl6.setStyleSheet("color: #0066cc;")
        self.lbl6.setFont(QFont('맑은 고딕', 15))
        self.lbl7 = QtWidgets.QLabel(MainWindow)
        self.lbl7.setGeometry(QtCore.QRect(410, 550, 40, 40))
        self.lbl7.setObjectName("lbl7")
        self.lbl7.setStyleSheet("color: #000033;")
        self.lbl7.setFont(QFont('맑은 고딕', 15))
        self.lbl8 = QtWidgets.QLabel(MainWindow)
        self.lbl8.setGeometry(QtCore.QRect(440, 620, 40, 40))
        self.lbl8.setObjectName("lbl8")
        self.lbl8.setStyleSheet("color: #663399;")
        self.lbl8.setFont(QFont('맑은 고딕', 15))
        self.lbl9 = QtWidgets.QLabel(MainWindow)
        self.lbl9.setGeometry(QtCore.QRect(460, 705, 40, 40))
        self.lbl9.setObjectName("lbl9")
        self.lbl9.setStyleSheet("color: #ff6699;")
        self.lbl9.setFont(QFont('맑은 고딕', 15))
        self.formLayoutWidget = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 430, 221, 311))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.c_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_1.setObjectName("label")
        self.c_1.setStyleSheet("color: "+self.colorlist[0]+";")
        self.gridLayout.addWidget(self.c_1, 0, 0, 1, 1)
        self.n_1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_1.setObjectName("label_14")
        self.gridLayout.addWidget(self.n_1, 0, 1, 1, 1)
        self.c_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_2.setObjectName("label_15")
        self.c_2.setStyleSheet("color: " + self.colorlist[1] + ";")
        self.gridLayout.addWidget(self.c_2, 1, 0, 1, 1)
        self.n_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_2.setObjectName("label_4")
        self.gridLayout.addWidget(self.n_2, 1, 1, 1, 1)
        self.c_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_3.setObjectName("label_2")
        self.c_3.setStyleSheet("color: " + self.colorlist[2] + ";")
        self.gridLayout.addWidget(self.c_3, 2, 0, 1, 1)
        self.n_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.n_3, 2, 1, 1, 1)
        self.c_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_4.setObjectName("label_6")
        self.c_4.setStyleSheet("color: " + self.colorlist[3] + ";")
        self.gridLayout.addWidget(self.c_4, 3, 0, 1, 1)
        self.n_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_4.setObjectName("label_5")
        self.gridLayout.addWidget(self.n_4, 3, 1, 1, 1)
        self.c_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_5.setObjectName("label_7")
        self.c_5.setStyleSheet("color: " + self.colorlist[4] + ";")
        self.gridLayout.addWidget(self.c_5, 4, 0, 1, 1)
        self.n_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_5.setObjectName("label_8")
        self.gridLayout.addWidget(self.n_5, 4, 1, 1, 1)
        self.c_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_6.setObjectName("label_9")
        self.c_6.setStyleSheet("color: " + self.colorlist[5] + ";")
        self.gridLayout.addWidget(self.c_6, 5, 0, 1, 1)
        self.n_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_6.setObjectName("label_10")
        self.gridLayout.addWidget(self.n_6, 5, 1, 1, 1)
        self.c_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_7.setObjectName("label_11")
        self.c_7.setStyleSheet("color: " + self.colorlist[6] + ";")
        self.gridLayout.addWidget(self.c_7, 6, 0, 1, 1)
        self.n_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_7.setObjectName("label_16")
        self.gridLayout.addWidget(self.n_7, 6, 1, 1, 1)
        self.c_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_8.setObjectName("label_17")
        self.c_8.setStyleSheet("color: " + self.colorlist[7] + ";")
        self.gridLayout.addWidget(self.c_8, 7, 0, 1, 1)
        self.n_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_8.setObjectName("label_12")
        self.gridLayout.addWidget(self.n_8, 7, 1, 1, 1)
        self.c_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.c_9.setObjectName("label_18")
        self.c_9.setStyleSheet("color: " + self.colorlist[8] + ";")
        self.gridLayout.addWidget(self.c_9, 8, 0, 1, 1)
        self.n_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.n_9.setObjectName("label_13")
        self.gridLayout.addWidget(self.n_9, 8, 1, 1, 1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl1.setText(_translate("MainWindow", "●"))
        self.lbl2.setText(_translate("MainWindow", "●"))
        self.lbl3.setText(_translate("MainWindow", "●"))
        self.lbl4.setText(_translate("MainWindow", "●"))
        self.lbl5.setText(_translate("MainWindow", "●"))
        self.lbl6.setText(_translate("MainWindow", "●"))
        self.lbl7.setText(_translate("MainWindow", "●"))
        self.lbl8.setText(_translate("MainWindow", "●"))
        self.lbl9.setText(_translate("MainWindow", "●"))
        self.c_1.setText(_translate("MainWindow", "\t●"))
        self.n_1.setText(_translate("MainWindow", "1"))
        self.c_2.setText(_translate("MainWindow", "\t●"))
        self.n_2.setText(_translate("MainWindow", "2"))
        self.c_3.setText(_translate("MainWindow", "\t●"))
        self.n_3.setText(_translate("MainWindow", "3"))
        self.c_4.setText(_translate("MainWindow", "\t●"))
        self.n_4.setText(_translate("MainWindow", "4"))
        self.c_5.setText(_translate("MainWindow", "\t●"))
        self.n_5.setText(_translate("MainWindow", "5"))
        self.c_6.setText(_translate("MainWindow", "\t●"))
        self.n_6.setText(_translate("MainWindow", "6"))
        self.c_7.setText(_translate("MainWindow", "\t●"))
        self.n_7.setText(_translate("MainWindow", "7"))
        self.c_8.setText(_translate("MainWindow", "\t●"))
        self.n_8.setText(_translate("MainWindow", "8"))
        self.c_9.setText(_translate("MainWindow", "\t●"))
        self.n_9.setText(_translate("MainWindow", "9"))