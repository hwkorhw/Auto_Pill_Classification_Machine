import RPi.GPIO as GPIO
import time
import sys
import cv2

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pin1 = 29
pin2 = 31
pin3 = 33
pin4 = 35

GPIO.setup(pin3, GPIO.OUT)  # 3
GPIO.setup(pin2, GPIO.OUT)#  2
GPIO.setup(pin1, GPIO.OUT) # 1
GPIO.setup(pin4, GPIO.OUT)# 4 

GPIO.output(pin2, GPIO.LOW)
GPIO.output(pin4, GPIO.LOW)


GPIO.output(pin3, GPIO.LOW)# dir pin High c low cc


ls = 8 # range per step
ld = 1.8
start_idx = 0 #fixed
now_idx = 0
final_i = 0
input_list=[]
count = len(input_list)



def low_step(new_idx, copy): # 0 - 35 index
    
    #global start_idx
    #global now_idx
    global ls
    global ld
    global new_i
    global count
    global final_i
    
    if count == 0:
        input_list.append(new_idx)
        final_i=1
        count+=1
        
        
    for i in range(count):
        if new_idx == input_list[i]:
            final_i = i
            break
        else:
            if count == i+1:
                input_list.append(new_idx)
                final_i=count
                count += 1
    
    # print(final_i)
    # print(count)
    # print(input_list)
    
    # direction
    if new_idx > now_idx:
        GPIO.output(pin3, GPIO.HIGH) # Cw
    elif new_idx <= now_idx:
        GPIO.output(pin3, GPIO.LOW) # CCw
        
    # move
    for x in range(final_i*ls): # 1.8 d = 1 range     min = 1.8*8 =14.4d 14.4* 25 = 360 
        GPIO.output(pin1, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pin1, GPIO.LOW)
        time.sleep(0.001)    

    time.sleep(0.5)


    now = time.time()
    cv2.imwrite('./image/'+ str(final_i).zfill(2) + '/' + str(now) + '.jpg' , copy)


def fin():
    #global start_idx
    #global now_idx
    global final_i
    global ls
    
    
    GPIO.output(pin3, GPIO.LOW)
        # move
    for x in range(final_i*ls): # 1.8 d = 1 range     min = 1.8*8 =14.4d 14.4* 25 = 360
        #print(final_i)
        GPIO.output(pin1, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(pin1, GPIO.LOW)
        time.sleep(0.001)
    
    start_idx = 0 #fixed
    now_idx = 0
    time.sleep(0.5)



# while True:
# 90 degree
#     for x in range(50): # 1.8 d = 1 range     min = 1.8*8 =14.4d 14.4* 25 = 360 
#         GPIO.output(pin1, GPIO.HIGH)
#         time.sleep(0.001)
#         GPIO.output(pin1, GPIO.LOW)
#        time.sleep(0.001)
#     time.sleep(0.5)
#myPwm = GPIO.PWM(pin1, 148) # pin, frequency
#myPwm.start(15) #dutycycle (0~100사이 값). 아두이노로 치면 analogWrite(18, pin38)과 동일.
#time.sleep(0.05)
#myPwm.stop()
    
    
