from PyQt5.QtCore import *
import random
import first

class Worker(QThread):
    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        while self.running:
            print("start")
            self.sleep(1)

    def resume(self):
        self.running = True
        self.start()

    def pause(self):
        self.running = False