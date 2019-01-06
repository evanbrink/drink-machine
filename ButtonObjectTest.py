from guizero import *
import serial
import time

## ---------------GLOBAL VARIALBES-------------------
window_height = 400
window_width = 700
image_size = 250

## Calibration constants
cc1 = 1
cc2 = 0.98
cc3 = 1.1
cc4 = 1
cc5 = 1.2
cc6 = 1
cc7 = 0.8
cc9 = 0.95
cc10 = 1.02
cc11 = 1.15
cc12 = 1

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

## ---------------CUSTOM OBJECTS-------------------------
## buttons
class DrinkButton:
    def __init__(self, command, img, page, x, y):
        self.button = Picture(page, grid = [x,y], image =img)
        self.button.when_clicked = command

class Pump:
    def __init__(self, num, calib):
        self.number = num
        self.calibration = calib








app = App(title="ButtonObject Test", width = window_width,
          height = window_height, layout = "grid")

page_one = Box(app, grid = [0,0], align = "top", layout = "grid")
page_one_text = Text(page_one, grid = [1,0], align = "top", text = "PAGE ONE")

page_two = Box(app, grid = [0,0], align = "top", layout = "grid", enabled = False, visible = False)
page_two_text = Text(page_two, grid = [0,0], align = "top", text = "PAGE TWO")


raw_page = Box(app, grid = [0,0], align = "top", layout = "grid", enabled = False, visible = False)

button_box = Box(app, grid = [0,2], align = "top", layout = "grid")






## Navigation functions
def go_to_page(page):
    if page == 0:
        page_one.hide()
        page_one.disable()
        page_two.hide()
        page_two.disable()
        raw_page.hide()
        raw_page.disable()
        button_box.hide()
        button_box.disable()


    if page == 1:

        page_two.hide()
        page_two.disable()
        raw_page.hide()
        raw_page.disable()

        page_one.show()
        page_one.enable()
        button_box.enable()
        button_box.show()

    if page == 2:
        page_one.hide()
        page_one.disable()

        raw_page.hide()
        raw_page.disable()

        page_two.show()
        page_two.enable()
        button_box.enable()
        button_box.show()
    if page == -1:
        page_one.hide()
        page_one.disable()
        page_two.hide()
        page_two.disable()
        button_box.show()
        button_box.enable()

        raw_page.show()
        raw_page.enable()

## Button Box Setup
button_one = PushButton(button_box, command = go_to_page, args = [1],
                        text = "1", grid = [0,0])
button_two = PushButton(button_box, command = go_to_page, args = [2],
                        text = "2", grid = [1,0])
raw_button = PushButton(button_box, command = go_to_page, args = [-1],
                        text = "Ingredients", grid = [2,0])

def cmd01():
    print("BUTTON PRESSED!")
    pour3(4,805,2,5022,3,2000)

def cmd02():
    ping()

mojitoButton = DrinkButton(cmd01, "MojitoButton.png", page_one, 0,0)
pinaColadaButton = DrinkButton(cmd02, "Pina-Colada.jpg", page_one, 0,1)

app.display()
