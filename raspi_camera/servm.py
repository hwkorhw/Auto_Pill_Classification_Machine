# sudo systemctl enable pigpiod  ---  시스템 시작 시 언제나 pigpiod 실행

import time
from pigpiomaster import pigpio
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

#pirPin = 8 # sensorpin

#GPIO.setup(pirPin, GPIO.IN)
    
pi = pigpio.pi() #먼저 사용할 pigpio.pi를 매칭해줍니다.

        
    

def moves(d,s=1):
    m = 500+round(2000.0*(d/180.0))
    #print(m)
    pi.set_servo_pulsewidth(23,m) #16번 채널에연결된 서보모터를 꺼줍니다. 
    sleep(s)
    


def start():

    for x in range(57):
        moves(120-x,s=0.03) # 알약 받고 이동( 약간 초과 )
        
    sleep(0.5)
    moves(75.5)# 렌즈 위치 
    #moves(35)
    
    
if __name__=='__main__':
    while True:
        start()
        moves(120)
'''
for x in range(45):
    moves(45+x,0.02)
'''
'''
pi.set_servo_pulsewidth(23, 2500) # 180도 끝으로 이동. 

sleep(1)

pi.set_servo_pulsewidth(24, 2500) # 180도 끝으로 이동. 

sleep(1)
'''
