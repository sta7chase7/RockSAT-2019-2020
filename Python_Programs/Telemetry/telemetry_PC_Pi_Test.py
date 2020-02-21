import serial
import time


def readlineCR(port):
    rv = ""
    while True:
        ch = port.read()
        rv += ch
        if ch == '\r' or ch == '':
            return rv


port = serial.Serial("/dev/ttyAMA0", baudrate = 7200, timeout = 2)

while True: 
    rcv = readlıneCR(port)
    port.write("I typed: " + repr(rcv))
    print(rcv)