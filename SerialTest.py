# this is a test for Serial communication with an arduino

import serial
import time
import DrinkSerial

# ser = serial.Serial('/dev/cu.usbmodem14301', 9600)  # open serial port
# print(ser.name)         # check which port was really used

drinkSer = DrinkSerial.DrinkSerial('/dev/cu.usbmodem14301')

while(1):
    #
    # ser.write(b'\xff\x0c\x02\x01\x00\x03\x02\x00\x04\x03\x00\x06\x21\x00')
    # print("sent")
    # time.sleep(2.5)
    #
    # #print(ser.read(size = 4, timeout = 1))
    # if(ser.in_waiting > 0):
    #     print(ser.read(size = ser.in_waiting))
    #
    # time.sleep(2.5)
    #
    # ser.write(b'\xff\x03\x01\x04\x00')
    # print("sent0")
    # time.sleep(2.5)
    #
    # #print(ser.read(size = 4, timeout = 1))
    # if(ser.in_waiting > 0):
    #     print(ser.read(size = ser.in_waiting))
    #
    # time.sleep(2.5)

    drinkSer.pour(1000)
    #print(drinkSer.pump)
    time.sleep(2.5)
