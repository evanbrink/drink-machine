# this is a test for Serial communication with an arduino

import serial
import time
# import DrinkSerial

## ---------------SERIAL FUNCITONS-----------------------
ser = serial.Serial('/dev/cu.usbmodem14301', 9600)  # open serial port

def ping():
    ser.write(b'\xff\x03\x01\x04\x00')

def pour(pump, time):
    header = b'\xff'
    length = b'\x06'
    instr  = b'\x02'
    pnum   = bytes([pump])
    ptimeL = bytes([time%256])
    ptimeH = bytes([int(time/256)])
    CRC =  ((6+2+pump+time%256+int(time/256))%65536
            ).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum+ptimeL+ptimeH+CRC
    ser.write(packet)

def pour2(pump, time, pump2, time2):
    header = b'\xff'
    length = b'\x09'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time%256])
    time1H = bytes([int(time/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    CRC =  ((9+2+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)
            )%65536).to_bytes(2,byteorder='little')

    packet = header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+CRC
    ser.write(packet)

def pour3(pump, time, pump2, time2, pump3, time3):
    header = b'\xff'
    length = b'\x0c'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time%256])
    time1H = bytes([int(time/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    CRC =  ((12+2+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256))%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+CRC)
    ser.write(packet)


def pour4(pump, time, pump2, time2, pump3, time3, pump4, time4):
    header = b'\xff'
    length = b'\x0f'
    instr  = b'\x02'
    pnum1  = bytes([pump])
    time1L = bytes([time%256])
    time1H = bytes([int(time/256)])
    pnum2  = bytes([pump2])
    time2L = bytes([time2%256])
    time2H = bytes([int(time2/256)])
    pnum3  = bytes([pump3])
    time3L = bytes([time3%256])
    time3H = bytes([int(time3/256)])
    pnum4  = bytes([pump4])
    time4L = bytes([time4%256])
    time4H = bytes([int(time4/256)])
    CRC =  ((15+2+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)+
            pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)
             )%65536).to_bytes(2,byteorder='little')

    packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
    + time3L+time3H+pnum4+time4L+time4H+CRC)
    ser.write(packet)

    def back(pump, time):
        header = b'\xff'
        length = b'\x06'
        instr  = b'\x04'
        pnum   = bytes([pump])
        ptimeL = bytes([time%256])
        ptimeH = bytes([int(time/256)])
        CRC =  ((6+4+pump+time%256+int(time/256))%65536
                ).to_bytes(2,byteorder='little')

        packet = header+length+instr+pnum+ptimeL+ptimeH+CRC
        ser.write(packet)

    def back2(pump, time, pump2, time2):
        header = b'\xff'
        length = b'\x09'
        instr  = b'\x04'
        pnum1  = bytes([pump])
        time1L = bytes([time%256])
        time1H = bytes([int(time/256)])
        pnum2  = bytes([pump2])
        time2L = bytes([time2%256])
        time2H = bytes([int(time2/256)])
        CRC =  ((9+4+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)
                )%65536).to_bytes(2,byteorder='little')

        packet = header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+CRC
        ser.write(packet)

    def back3(pump, time, pump2, time2, pump3, time3):
        header = b'\xff'
        length = b'\x0c'
        instr  = b'\x04'
        pnum1  = bytes([pump])
        time1L = bytes([time%256])
        time1H = bytes([int(time/256)])
        pnum2  = bytes([pump2])
        time2L = bytes([time2%256])
        time2H = bytes([int(time2/256)])
        pnum3  = bytes([pump3])
        time3L = bytes([time3%256])
        time3H = bytes([int(time3/256)])
        CRC =  ((12+4+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)+
                pump3+time3%256+int(time3/256))%65536).to_bytes(2,byteorder='little')

        packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
        + time3L+time3H+CRC)
        ser.write(packet)


    def back4(pump, time, pump2, time2, pump3, time3, pump4, time4):
        header = b'\xff'
        length = b'\x0f'
        instr  = b'\x04'
        pnum1  = bytes([pump])
        time1L = bytes([time%256])
        time1H = bytes([int(time/256)])
        pnum2  = bytes([pump2])
        time2L = bytes([time2%256])
        time2H = bytes([int(time2/256)])
        pnum3  = bytes([pump3])
        time3L = bytes([time3%256])
        time3H = bytes([int(time3/256)])
        pnum4  = bytes([pump4])
        time4L = bytes([time4%256])
        time4H = bytes([int(time4/256)])
        CRC =  ((15+4+pump+time%256+int(time/256)+pump2+time2%256+int(time2/256)+
                pump3+time3%256+int(time3/256)+pump4+time4%256+int(time4/256)
                 )%65536).to_bytes(2,byteorder='little')

        packet = (header+length+instr+pnum1+time1L+time1H+pnum2+time2L+time2H+pnum3
        + time3L+time3H+pnum4+time4L+time4H+CRC)
        ser.write(packet)

# drinkSer = DrinkSerial.DrinkSerial('/dev/cu.usbmodem14301')


ping()
time.sleep(1)
ping()
time.sleep(1)

pour4(3,3000, 2, 5000, 7, 7000, 1, 1000)
time.sleep(7)
if(ser.in_waiting > 0):
   print(ser.read(size = ser.in_waiting))

# while(1):
#     ping()
#     time.sleep(1)
#     pour(1, 1500)
#     time.sleep(2.5)
#     pour(2, 1500)
#     time.sleep(2.5)
#     pour(3, 1500)
#     time.sleep(2.5)
#     pour(4, 1500)
#     time.sleep(2.5)
#     pour(5, 1500)
#     time.sleep(2.5)
#     pour(6, 1500)
#     time.sleep(2.5)
#     pour(7, 1500)
#     time.sleep(2.5)
#     pour(8, 1500)
#     time.sleep(2.5)
#     pour(9, 1500)
#     time.sleep(2.5)
#     pour(10, 1500)
#     time.sleep(2.5)
#     pour(11, 1500)
#     time.sleep(2.5)
#     pour(12, 1500)
#     time.sleep(2.5)






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

    # drinkSer.pour(1000)
    # #print(drinkSer.pump)
    # time.sleep(2.5)
