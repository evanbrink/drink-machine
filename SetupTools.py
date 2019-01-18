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
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)  # Raspberry pi
except:
    try:
        ser = serial.Serial('/dev/cu.usbmodem14301', 9600)  # Mac
    except:
        try:
            ser = serial.Serial('/dev/cu.usbmodem14401', 9600)  # Mac
        except:
            ser = serial.Serial('/dev/cu.usbmodem14201', 9600)  # Mac


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
page_one_text = Text(page_one, grid = [0,0], align = "top", text = "PAGE ONE")
page_two = Box(app, grid=[0,0], align="top", layout="grid",
               enabled=False, visible=False)
page_two_text = Text(page_two, grid = [0,0], align = "top", text = "PAGE TWO")

button_box = Box(app, grid = [0,1], align = "top", layout = "grid")


# Navigation functions
def clear_screen():
    page_one.hide()
    page_one.disable()
    page_two.hide()
    page_two.disable()
    button_box.hide()
    button_box.disable()


def go_to_page(page):
    clear_screen()
    if page == 1:
        page_one.show()
        page_one.enable()
        button_box.enable()
        button_box.show()
    if page == 2:
        page_two.show()
        page_two.enable()
        button_box.enable()
        button_box.show()
    app.update()

# Button Box Setup
button_one = PushButton(button_box, command = go_to_page, args = [1],
                        text = "Page 1", grid = [0,0])
button_two = PushButton(button_box, command = go_to_page, args = [2],
                        text = "Page 2", grid = [1,0])

def PrimePumps():
    pour4(1, pr1, 2, pr2, 3, pr3, 4, pr4)
    time.sleep(max([pr1, pr2, pr3, pr4])/1000.0)

    pour4(5, pr5, 6, pr6, 7, pr7, 8, pr8)
    time.sleep(max([pr5, pr6, pr7, pr8])/1000.0)

    pour4(9, pr9, 10, pr10, 11, pr11, 12, pr12)
    time.sleep(max([pr9, pr10, pr11, pr12])/1000.0)


def EmptyPumps():
    info(title="Warning", text="Are you sure you want to empty?")
    back4(1, pr1, 2, pr2, 3, pr3, 4, pr4)
    time.sleep(max([pr1, pr2, pr3, pr4])/1000.0)

    back4(5, pr5, 6, pr6, 7, pr7, 8, pr8)
    time.sleep(max([pr5, pr6, pr7, pr8])/1000.0)

    back4(9, pr9, 10, pr10, 11, pr11, 12, pr12)
    time.sleep(max([pr9, pr10, pr11, pr12])/1000.0)



primeButton = PushButton(page_one, command = PrimePumps,
                        text = "Prime", grid = [0,0])
emptyButton = PushButton(page_two, command = EmptyPumps,
                        text = "Empty", grid = [1,0])

oneButton = PushButton(page_one, command=pour, args=[1,1000],
                       text="P1", grid=[1,0])
twoButton = PushButton(page_one, command=pour, args=[2,1000],
                       text="P2", grid=[2,0])
threeButton = PushButton(page_one, command=pour, args=[3,1000],
                       text="P3", grid=[3,0])
fourButton = PushButton(page_one, command=pour, args=[4,1000],
                       text="P4", grid=[4,0])
fiveButton = PushButton(page_one, command=pour, args=[5,500],
                       text="P5", grid=[5,0])
sixButton = PushButton(page_one, command=pour, args=[6,500],
                       text="P6", grid=[0,1])
sevenButton = PushButton(page_one, command=pour, args=[7,500],
                       text="P7", grid=[1,1])
eightButton = PushButton(page_one, command=pour, args=[8,500],
                       text="P8", grid=[2,1])
nineButton = PushButton(page_one, command=pour, args=[9,500],
                       text="P9", grid=[3,1])
tenButton = PushButton(page_one, command=pour, args=[10,500],
                       text="P10", grid=[4,1])
elevenButton = PushButton(page_one, command=pour, args=[11,500],
                       text="P11", grid=[5,1])
twelveButton = PushButton(page_one, command=pour, args=[12,500],
                       text="P12", grid=[6,1])

app.display()
