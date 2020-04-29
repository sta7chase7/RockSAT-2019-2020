import time
import serial

#make serial object: needs 19200 baud, no parity, 8 bits/byte, and 1 stop bit
ser = serial.Serial(
        port='/dev/ttyUSB0',
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#read serial input and print
while 1:
        x=ser.readline()
        print(x)
