from guizero import *
import serial
import time


#  ---------------GLOBAL VARIALBES-------------------
window_height = 700
window_width = 1000
image_size = 250

# pump prime times (in ms)
pr1 = 13500
pr2 = 13000
pr3 = 13000
pr4 = 13500
pr5 = 5000
pr6 = 5500
pr7 = 6000
pr8 = 5500
pr9 = 5500
pr10 = 5500
pr11 = 5500
pr12 = 6000


# -----------------SERIAL FUNCITONS-----------------------
# open serial port
#ser = serial.Serial('/dev/cu.usbmodem14201', 9600)  # Mac
ser = serial.Serial('/dev/ttyACM0', 9600)  # Raspberry pi


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



app = App(title="Setup Tools", width=window_width,
         height=window_height, layout="grid")

page_one = Box(app, grid=[0, 0], align="top", layout="grid")

def PrimePumps():
    pour4(1, pr1, 2, pr2, 3, pr3, 4, pr4)
    time.sleep(max([pr1, pr2, pr3, pr4])/1000.0)

    pour4(5, pr5, 6, pr6, 7, pr7, 8, pr8)
    time.sleep(max([pr5, pr6, pr7, pr8])/1000.0)

    pour4(9, pr9, 10, pr10, 11, pr11, 12, pr12)
    time.sleep(max([pr9, pr10, pr11, pr12])/1000.0)


def EmptyPumps():
    back4(1, pr1, 2, pr2, 3, pr3, 4, pr4)
    time.sleep(max([pr1, pr2, pr3, pr4])/1000.0)

    back4(5, pr5, 6, pr6, 7, pr7, 8, pr8)
    time.sleep(max([pr5, pr6, pr7, pr8])/1000.0)

    back4(9, pr9, 10, pr10, 11, pr11, 12, pr12)
    time.sleep(max([pr9, pr10, pr11, pr12])/1000.0)



primeButton = PushButton(page_one, command = PrimePumps,
                        text = "Prime", grid = [0,0])
emptyButton = PushButton(page_one, command = EmptyPumps,
                        text = "Empty", grid = [1,0])

app.display()
