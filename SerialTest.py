# this is a test for Serial communication with an arduino

import serial
import time

ser = serial.Serial('/dev/cu.usbmodem1411', 9600)  # open serial port
print(ser.name)         # check which port was really used

while(1):
    ser.write(b'\xff\x03\x01\x04\x01')
    print("sent")
    time.sleep(2.5)

    #print(ser.read(size = 4, timeout = 1))
    if(ser.in_waiting > 0):
        print(ser.read(size = ser.in_waiting))
    
    time.sleep(2.5)

