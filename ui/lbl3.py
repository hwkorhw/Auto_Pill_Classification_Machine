# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lbl3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1.setGeometry(QtCore.QRect(670, 670, 90, 90))
        self.lbl1.setObjectName("lbl1")
        self.lbl9 = QtWidgets.QLabel(self.centralwidget)
        self.lbl9.setGeometry(QtCore.QRect(30, 40, 90, 90))
        self.lbl9.setObjectName("lbl9")
        self.lbl8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl8.setGeometry(QtCore.QRect(70, 170, 90, 90))
        self.lbl8.setObjectName("lbl8")
        self.lbl2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl2.setGeometry(QtCore.QRect(530, 630, 90, 90))
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl3.setGeometry(QtCore.QRect(440, 570, 90, 90))
        self.lbl3.setObjectName("lbl3")
        self.lbl7 = QtWidgets.QLabel(self.centralwidget)
        self.lbl7.setGeometry(QtCore.QRect(110, 270, 90, 90))
        self.lbl7.setObjectName("lbl7")
        self.lbl6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl6.setGeometry(QtCore.QRect(160, 360, 90, 90))
        self.lbl6.setObjectName("lbl6")
        self.lbl4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl4.setGeometry(QtCore.QRect(340, 520, 90, 90))
        self.lbl4.setObjectName("lbl4")
        self.lbl5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl5.setGeometry(QtCore.QRect(250, 450, 90, 90))
        self.lbl5.setObjectName("lbl5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl1.setText(_translate("MainWindow", "TextLabel"))
        self.lbl9.setText(_translate("MainWindow", "TextLabel"))
        self.lbl8.setText(_translate("MainWindow", "TextLabel"))
        self.lbl2.setText(_translate("MainWindow", "TextLabel"))
        self.lbl3.setText(_translate("MainWindow", "TextLabel"))
        self.lbl7.setText(_translate("MainWindow", "TextLabel"))
        self.lbl6.setText(_translate("MainWindow", "TextLabel"))
        self.lbl4.setText(_translate("MainWindow", "TextLabel"))
        self.lbl5.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
