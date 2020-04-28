import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0

while 1:
        #encode the counter variable to a binary string
        thing_to_send = bytes(str(counter) + "\n", encoding='utf8')
        ser.write(thing_to_send)
        time.sleep(1)
        counter += 1
        print(thing_to_send)


#array_collect():
        #Define default array elements
                #include non-standard escape character as last array element
        #mission time [locally counted by pi's]
                #ms?
        #TE-(1,R) line state
                #0 or 1 for each
        #sensor data [ADXL377,TMP006,TMP36,Distance]
                #make substructures for each
                #decide upon & record units of measurement
        #motor state info
                #See relevant script; move_cmd, direction, running?
        #MADV state info [power, recording state]
                #Get further details once it's tested
        #note to add static indexing to values
        #Regularly convert all data to bytes
        #work out timing; function should wait for a time interval, not the presence of all data elements, to 
        #return array of byte values

#array_filesave():
        #take input from array_collect
        #convert to [numpy?] array and save as txt every few minutes
        #figure out how to avoid having missed values

#telemetry_send():
        #Take in byte array
        #Send it with no delay
        