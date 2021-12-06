from _serial import ser
import RPi.GPIO as GPIO
from time import sleep
from pigpiomaster import pigpio
import os
#os.system('sudo /home/pi/serv/pigpiomaster/pigpiod')


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

in1 = 12
out = 37

GPIO.setup(in1, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(out, GPIO.IN)


GPIO.output(16,GPIO.HIGH)

pi = pigpio.pi()
 
StepPins = [13,11,38,40]
#핀 출력 설정

for pin in StepPins:

  GPIO.setup(pin,GPIO.OUT)

  GPIO.output(pin,False)




def moves(pin,d, s=0.3):
    m = 500 + round(2000.0 * (d / 180.0))
    pi.set_servo_pulsewidth(pin, m) #16번 채널에연결된 서보모터를 꺼줍니다.
    sleep(s)
 

def push():
    
    GPIO.output(16,GPIO.LOW)
    sleep(0.3)
    moves(6,65) # bcm6 = board 31
    moves(6,105)# bcm6 = board 31
    sleep(0.3)
    GPIO.output(16,GPIO.HIGH)
    print('pushed!')

def shot():
    sleep(0.2)
    
    
    for x in range(9): #9
        moves(19,115-((x+1)*10),0.1) # bcm19 = board 35
    moves(19,115)
    print('shot!')
    ser.write('i'.encode())
    
def stop():
    global stopping
    
    stopping =1
    
    GPIO.output(16,GPIO.LOW)
    sleep(0.3)
    
    shot()
    
    while True:
        if ser.readable():
            if ser.read().decode()=='f':
                print('1')
                break;
    
    GPIO.output(16,GPIO.HIGH)
    stopping =0
    
def servm():
    StepCounter = 0 #스텝 수 세는 변수
    StepPins = [13,11,38,40]
    # 싱글 코일 여자 방식 시퀀스

    StepCount = 4

    Seq = [[1,0,1,0],

           [0,1,1,0],

           [0,1,0,1],

           [1,0,0,1]]
    
    Seq2 = [[1,0,0,1],
            [0,1,0,1],
            [0,1,1,0],
            [1,0,1,0]]
    
    try:

        for x in range(100): #무한 반복

            for pin in range(0, 4):

                xpin = StepPins[pin]

                if Seq[StepCounter][pin]!=0: # Seq[][]가 0이 아니면 동작

                    GPIO.output(xpin, True)

                else:

                    GPIO.output(xpin, False)

            StepCounter += 1 # 1 증가

            # 시퀀스가 끝나면 다시 시작

            if (StepCounter==StepCount):

                StepCounter = 0

            if (StepCounter<0):

                StepCounter = StepCount

            #다음 동작 기다리기

            sleep(0.005)
    except KeyboardInterrupt: #Ctrl+c => 종료

        GPIO.cleanup()
        
    
    
    

for x in range(14):
    servm()

i=0
ing =0

gopush =0
pushed = 0
stopping =0

while True:
    
    try :
        #-------------------------------------------
        if (GPIO.input(in1) == False) :
            if not ing :
                ing=1
                print(i)
                if i < 300000:
                    if not pushed :
                        #t = threading.Thread(target=push,daemon=True)
                        #t.start()
                        pushed =1
                        push()
                        
                
                else :
                    pushed =0
                    i=0
            
        elif (GPIO.input(in1) == True) :
            
            i+=1
            ing =0
            
        
    
        #----------------------------------------
        if (GPIO.input(out) == False) :
            stop()
            
        #if i > 2000000:
            #if i%2000000 ==0:
                #servm()
                
         
        if i > 1000000:
            if i%1000000 ==0:
                servm()
            
    except KeyboardInterrupt: #Ctrl+c => 종료

        GPIO.cleanup()
        GPIO.output(16,GPIO.LOW)
   
  



    
    
#myPwm = GPIO.PWM(7, 148) # pin, frequency
#myPwm.start(15) #dutycycle (0~100사이 값). 아두이노로 치면 analogWrite(18, 128)과 동일.
#time.sleep(0.05)
#myPwm.stop()
    
    

