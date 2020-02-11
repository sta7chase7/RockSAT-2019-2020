import time
initial_time_s = time.perf_counter()

#imports
import board
import busio
import multiprocessing
import RPi.GPIO

#Motor stuff
from adafruit_motorkit import MotorKit
#sensors
import Sensors.Distance_Code_vl53l0x as D
#import Sensors.Temperature_Code_TMP36
import Sensors.Temperature_Code_TMP006 as T6

import Arm_Control.Motor_Lib as motor_lib

#May need separate folders and inits for each file import
#https://stackoverflow.com/questions/50559539/import-a-file-from-another-location-python

#create input objects:

distance_input = distance_create_input()

#need to define input pins for input objects

#read and print data:

#GPIO:
#send "power on" signal to MADV
#Send "start recording" signal to MADV

telemetry_array = []
