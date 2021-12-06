from _serial import ser
from _camera import change_cam, take_pic, up_led, down_led, up_cam, down_cam, gp # gpio, os, time, cv
#from _ttsService import speak # os, time
#from readcsv import r,f # csv, io
from inference import infer # np, cv
from servm import * #time, move, start, pirpin
import numpy as np
import os
import cv2 as cv
import threading
from stepm import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pill_ui2

stopsign = False
complete_flag = True
idx = -1 

def _init():
    print('---Please Wait...---')
    # top
    moves(120)
    # low
    
    # leds
    gp.output(up_led,False)
    gp.output(down_led,False)
    print('Go!')

def show_info(MainD, i, num):
    app = QtWidgets.QApplication(sys.argv)
    detail_info = pill_ui2.Ui_MainWindow(MainD)
    detail_info.show_ui(i, num)
    MainD.show()

def main_loop():
    global idx
    
    while True:
        print('.')
        #if not GPIO.input(pirPin): # pill in
        if ser.read().decode() == 'i':
            complete_flag = False
            print('Pill in!')
            moves(120)
            sleep(0.8)
            

            start()
            # up camera
            frame_up = take_pic(up_cam, up_led)

            # down camera
            frame_down = take_pic(down_cam, down_led)
                         
            # inference
            # p_name, p_guide = infer(frame_up, frame_down)
            idx, copy = infer(frame_up, frame_down)

            # tts service
            # speak(p_name,p_guide)

            # down sevo
            # ser.write(str(p_guide).encode())
            # ser.write(str(0).encode())
            low_step(idx, copy)
            
            
            # top servo
            moves(35)
            moves(120)
            fin()
            # os.system('cvlc finish.mp3 --play-and-exit')
            complete_flag = True
            sleep(0.001)
            ser.write('f'.encode())
            
            if stopsign is True:
                sys.exit()
                
                

if __name__ == '__main__':
    _init()
    threading.Thread(target = main_loop).start()

    