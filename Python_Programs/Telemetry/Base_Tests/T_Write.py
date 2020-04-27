import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

while 1:
        #encode the counter variable to a binary string
        thing_to_send = bytes(str(counter), encoding='utf8')
        ser.write(thing_to_send)
        time.sleep(1)
        counter += 1
        print(thing_to_send)
