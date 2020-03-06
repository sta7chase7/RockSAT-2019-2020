import serial
ser = serial.Serial(port="/dev/ttyAMA0")    #Open named port 
ser.baudrate = 19200                     #Set baud rate to 9600
data = ser.read(10)                     #Read ten characters from serial port to data
ser.write(data)                         #Send back the received data
ser.close()