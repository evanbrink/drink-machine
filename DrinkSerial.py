## This is the Serial Communication Library for MouthSmash (Drink Machine)
import serial

## ---------------SERIAL FUNCITONS-----------------------
class DrinkSerial:
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600) # open serial port

    def ping():
        self.ser.write(b'\xff\x03\x01\x04\x00')

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
        self.ser.write(packet)

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
