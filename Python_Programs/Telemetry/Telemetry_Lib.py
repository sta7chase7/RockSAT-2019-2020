import time
import serial

def serial_default():
#make serial object: needs 19200 baud, no parity, 8 bits/byte, and 1 stop bit
        serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 19200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
        )

serial_send(serial_object, data):
        #encode the input value to a byte array [migrate out of this loop later]
        thing_to_send = bytes(str(data) + "\n", encoding='utf8')
        ser.write(thing_to_send)

        #calls list objects 
list_collect():
        #re-initialize with blank values every call - helps with troubleshooting
        list_collection = [None] * 10

        list_collection[0] = #mission time
        list_collection[1] = #TE-1 line state
        list_collection[2] = #TE-R line state
        list_collection[3] = #Motor state array
        list_collection[4] = #MADV state array
        list_collection[5] = #secondary camera state info
        list_collection[6] = #accelerometer data 
        list_collection[7] = #temperature sensor data #1
        list_collection[8] = #temperature sensor data #2
        list_collection[9] = #distance sensor data


        return list_collection
    #Define default array elements
                #include non-standard escape character as last array element: "*"
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
        #Secondary camera state info

        #note to add static indexes to values
        #Regularly convert all data to bytes
        #work out timing; function should wait for a time interval, not the presence of all data elements, to 
        #return array of byte values

#array_filesave():
        #take input from array_collect
        #convert to [numpy?] array and save as txt every few minutes
        #figure out how to avoid having missed values

#telemetry_send():
        #Take in correctly formatted byte array
        #Send it without delay
