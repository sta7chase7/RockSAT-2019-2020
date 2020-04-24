import time
#start a mission timer before anything else
initial_time_s = time.perf_counter()

#basic imports
import board
import busio
import RPi.GPIO

#Motor stuff
from adafruit_motorkit import MotorKit
#sensor imports (for sensors we have)
import Sensors.Distance_Code_vl53l0x as Dist
import Sensors.Temperature_Code_TMP006 as T6

import GPIO_Config.edge_detect_demo as Edge

#motor import
import Arm_Control.Motor_Lib as motor_lib

#create input objects:
distance_input = Dist.distance_create_input()

#May need separate folders and inits for each file import
#https://stackoverflow.com/questions/50559539/import-a-file-from-another-location-python

#need to define input pins for input objects

#read and print data:

#GPIO:
#send "power on" signal to MADV
#Send "start recording" signal to MADV

telemetry_array = []
