import serial

ser = serial.Serial(
    
    port='/dev/serial0',
    
    baudrate=115200)


print('---', ser.portstr, 'ready---')