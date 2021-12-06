import RPi.GPIO as gp
import os
import time
import cv2 as cv
import sys

try:
    gp.setwarnings(False)
    gp.setmode(gp.BOARD)

    # camera gpio
    gp.setup(7, gp.OUT)
    gp.setup(11,gp.OUT)
    gp.setup(12,gp.OUT)
    
    up_cam = 'C'
    down_cam = 'B'
    
    # led gpio
    up_led = 32
    down_led = 36
    gp.setup(up_led,gp.OUT)
    gp.setup(down_led,gp.OUT)
    print('---Camera is Ready---')
except:
    print('---Camera Error---')
    sys.exit()


# camera module map
adapter_info = {   "A":{   "i2c_cmd":"i2cset -y 1 0x70 0x00 0x04",
                            "gpio_sta":[0,0,1],
                    },
                "B":{
                        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x05",
                        "gpio_sta":[1,0,1],
                    },
                "C":{
                        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x06",
                        "gpio_sta":[0,1,0],
                    },
                "D":{
                        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x07",
                        "gpio_sta":[1,1,0],
                    },
             }


# pic width, height
width = 800
height = 800


def change_cam(_camera):
    channel_info = adapter_info.get(_camera)

    if channel_info == None:
        print("Channel_info Failed!")

    os.system(channel_info["i2c_cmd"]) # i2c write
    gpio_sta = channel_info["gpio_sta"] # gpio write
    gp.output(7, gpio_sta[0])
    gp.output(11, gpio_sta[1])
    gp.output(12, gpio_sta[2])
    


def take_pic(_camera, _gpio):
    cam = cv.VideoCapture(0)

    if cam == None:
        print("Camera innit Failed!")

    cam.set(3,width)
    cam.set(4,height)

    change_cam(_camera)

    gp.output(_gpio,True) # light on
    time.sleep(0.1) # prevent lightness change

    ret, frame = cam.read()

    if ret == False:
        print("Camera read Failed!", _camera)

    gp.output(_gpio,False) # light off

    cam.release()
    time.sleep(1)

    return frame


if __name__ == '__main__':
    import numpy as np
    # up camera
    frame_up = take_pic(up_cam, up_led)
    #cv.imshow('up',frame_up)
    # down camera
    frame_down = take_pic(down_cam, down_led)
    #cv.imshow('down',frame_down)

    net_input = np.hstack((frame_up,frame_down))
    cv.imshow('tot',net_input)
    cv.waitKey(0)
    cv.destroyAllWindows()

