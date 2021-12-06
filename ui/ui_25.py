# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_25_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import get_db, pill_ui2
import main_raspi_gogogogog as m
import threading

class Ui_MainWindow(object):
    def start_clicked(self):
        m._init()
        threading.Thread(target=m.main_loop).start()
    def pause_clicked(self):
        print('a')
    def resume_clicked(self):
        print('a')
    def stop_clicked(self):
        print('a')
    def start_main(self):
        self.mapping_num = list()
        self.count = 0

    def get_signal(self, num):
        if self.count == 0:
            self.mapping_num.append(num)
            self.count = self.count + 1
            i = 0
        else:
            for i in range(self.count):
                if self.mapping_num[i] == num:
                    break
                else:
                    if i + 1 == self.count:
                        self.mapping_num.append(num)
                        self.count = self.count + 1
                        i = i + 1

        data = get_db.get_one(self.mapping_num[i])

        self.set_lbl(i, data, self.mapping_num[i])

    def __init__(self, MainWindow):
        super().__init__()
        self.start_main()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1200)
        self.lbl = list()
        for i in range(25):
            self.lbl.append(QtWidgets.QPushButton(MainWindow))
        self.btn_start = QtWidgets.QPushButton(MainWindow)
        self.btn_resume = QtWidgets.QPushButton(MainWindow)
        self.btn_pause = QtWidgets.QPushButton(MainWindow)
        self.btn_stop = QtWidgets.QPushButton(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def setupUi(self):
        self.lbl[0].setGeometry(QtCore.QRect(80, 390, 80, 80))
        self.lbl[0].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[1].setGeometry(QtCore.QRect(160, 310, 80, 80))
        self.lbl[1].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[2].setGeometry(QtCore.QRect(240, 240, 80, 80))
        self.lbl[2].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[3].setGeometry(QtCore.QRect(320, 160, 80, 80))
        self.lbl[3].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[4].setGeometry(QtCore.QRect(400, 90, 80, 80))
        self.lbl[4].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[5].setGeometry(QtCore.QRect(480, 20, 80, 80))
        self.lbl[5].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[6].setGeometry(QtCore.QRect(620, 20, 80, 80))
        self.lbl[6].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[7].setGeometry(QtCore.QRect(710, 85, 80, 80))
        self.lbl[7].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[8].setGeometry(QtCore.QRect(800, 150, 80, 80))
        self.lbl[8].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[9].setGeometry(QtCore.QRect(890, 215, 80, 80))
        self.lbl[9].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[10].setGeometry(QtCore.QRect(980, 300, 80, 80))
        self.lbl[10].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[11].setGeometry(QtCore.QRect(1060, 365, 80, 80))
        self.lbl[11].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[12].setGeometry(QtCore.QRect(1060, 480, 80, 80))
        self.lbl[12].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[13].setGeometry(QtCore.QRect(980, 565, 80, 80))
        self.lbl[13].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[14].setGeometry(QtCore.QRect(890, 650, 80, 80))
        self.lbl[14].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[15].setGeometry(QtCore.QRect(800, 735, 80, 80))
        self.lbl[15].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[16].setGeometry(QtCore.QRect(710, 820, 80, 80))
        self.lbl[16].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[17].setGeometry(QtCore.QRect(620, 920, 80, 80))
        self.lbl[17].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[18].setGeometry(QtCore.QRect(470, 920, 80, 80))
        self.lbl[18].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[19].setGeometry(QtCore.QRect(380, 860, 80, 80))
        self.lbl[19].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[20].setGeometry(QtCore.QRect(290, 780, 80, 80))
        self.lbl[20].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[21].setGeometry(QtCore.QRect(200, 700, 80, 80))
        self.lbl[21].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[22].setGeometry(QtCore.QRect(110, 620, 80, 80))
        self.lbl[22].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[23].setGeometry(QtCore.QRect(20, 540, 80, 80))
        self.lbl[23].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.lbl[24].setGeometry(QtCore.QRect(20, 450, 80, 80))
        self.lbl[24].setStyleSheet("border-style: solid; border-width: 5px; border-color: #666666; border-radius: 40px;")
        self.btn_start.setGeometry(QtCore.QRect(520, 410, 150, 50))
        #self.btn_start.clicked.connect(self.start_clicked)
        self.btn_pause.setGeometry(QtCore.QRect(520, 410, 150, 50))
        self.btn_pause.clicked.connect(self.pause_clicked)
        self.btn_pause.hide()
        self.btn_resume.setGeometry(QtCore.QRect(520, 410, 150, 50))
        self.btn_resume.clicked.connect(self.resume_clicked)
        self.btn_resume.hide()
        self.btn_stop.setGeometry(QtCore.QRect(520, 480, 150, 50))
        self.btn_stop.clicked.connect(self.stop_clicked)
        self.btn_start.setText('Start')
        self.btn_pause.setText('Pause')
        self.btn_resume.setText('Resume')
        self.btn_stop.setText('Stop')
        self.get_signal(2)
        for i in range(25):
            self.lbl[i].setDisabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def show_info(self, i, num):
        self.MainD = QtWidgets.QDialog()
        self.detail_info = pill_ui2.Ui_MainWindow(self.MainD)
        self.detail_info.show_ui(i, num)
        self.MainD.show()

    def set_lbl(self, i, data, num):
        self.lbl[i].setStyleSheet("border-style: solid; border-width: 5px; border-color: #3333ff; border-radius: 40px;")
        self.lbl[i].setText(data[0])
        self.lbl[i].setDisabled(False)
        self.lbl[i].clicked.connect(lambda: self.show_info(i, num))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi()
    MainWindow.show()
    sys.exit(app.exec_())