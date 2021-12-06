import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDate, QTime

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()
        grid = QGridLayout()
        image_layout = QHBoxLayout()
        info_layout = QVBoxLayout()
        lbl_name = QLabel('약')
        lbl_name.setStyleSheet("color: #4D69E8; border-style: solid; border-width: 2px; border-color: #54A0FF; border-radius: 10px; ")
        lbl_name.maximumSize()
        lbl_color = QLabel('White')
        lbl_color.resize(400,200)
        info_layout.addWidget(lbl_name)
        info_layout.addWidget(lbl_color)
        btn_layout = QHBoxLayout()
        btn1 = QPushButton('OK')
        btn2 = QPushButton('Cancle')
        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        lbl_1 = QLabel()
        img_1 = QPixmap('/home/hw/pill_image/0_main.jpg')
        lbl_1.setPixmap(img_1)
        lbl_1.setStyleSheet("color: #4D69E8; border-style: solid; border-width: 2px; border-color: #7B68EE; border-radius: 10px; ")
        lbl_1.resize(600,200)
        image_layout.addWidget(lbl_1)
        image_layout.addLayout(info_layout)
        main_layout.addLayout(image_layout)

        main_layout.addLayout(btn_layout)
        self.setWindowTitle('My first Application')
        self.setGeometry(300, 300, 800, 800)
        self.setWindowIcon(QIcon('pill_icon.png'))
        self.setLayout(main_layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv) # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야함
    ex = MyApp()
    sys.exit(app.exec_())

