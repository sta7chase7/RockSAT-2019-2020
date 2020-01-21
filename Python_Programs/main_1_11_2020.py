import time
initial_time_s = time.perf_counter()

#imports
import analogio
import board
import busio
import multiprocessing
import RPi.GPIO
import subprocess

#Motor stuff
from adafruit_motorkit import MotorKit
#sensors
import Sensors.Accelerometer_Code_ADXL377
import Sensors.Distance_Code_vl53l0x
import Sensors.Temperature_Code_TMP36

#May need separate folders and inits for each file import
#https://stackoverflow.com/questions/50559539/import-a-file-from-another-location-python

#create input objects:

xyz_accel_list = accel_create_input_3ax(x_pin,y_pin,z_pin)
temp_input = temp_create_input(temp_pin)
distance_input = distance_create_input()
#need to define input pins for input objects

#read and print data:


#GPIO:
#send "power on" signal to MADV
#Send "start recording" signal to MADV





#List of things to do (unordered)
#--------------------------------
#
#set delay for time between GSE-On and launch (see CDR)
#offset timer by GSE-On delay
#--------------------------------