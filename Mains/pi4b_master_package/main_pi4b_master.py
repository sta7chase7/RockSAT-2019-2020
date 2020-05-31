import time
#start a mission timer before anything else
initial_time_s = time.perf_counter()

#basic imports
import board
import busio

#Includes time and GPIO
import GPIO_Lib as RSX_GPIO

#Motor stuff
from adafruit_motorkit import MotorKit
#sensor imports (for sensors we have)
import Sensors.Distance_Code_vl53l0x as Dist
import Sensors.Temperature_Code_TMP006 as T6

#motor import
import Arm_Control.Motor_Lib as motor_lib

#create input objects:
distance_input = Dist.distance_create_input()

#May need separate folders and inits for each file import
#https://stackoverflow.com/questions/50559539/import-a-file-from-another-location-python

#GPIO setup segment{
#Pin modes
#0 = GPIO.OUT
#1 = GPIO.IN
#40 = GPIO.SERIAL
#41 = GPIO.SPI
#42 = GPIO.I2C
#43 = GPIO.HARD_PWM
#-1 = GPIO.UNKNOWN

#Reference BCM pin convention; URL: pinout.xyz
#GPIO pinout does not vary across Pi models.
RSX_GPIO.setmode(RSX_GPIO.BCM)

#Assign I/O channel BCM numbers.
#Max BCIM index on Pi's appears to be 27.
in_channel_TE1 = 17
in_channel_TER = 27

out_channel_TE1 = 5
out_channel_TER = 6

#Set pin modes
RSX_GPIO.setup(in_channel_TE1, RSX_GPIO.IN)
RSX_GPIO.setup(out_channel_TE1, GPIO.OUT)

GPIO.setup(out_channel_TER, GPIO.OUT)
GPIO.setup(in_channel_TER, GPIO.IN)

#Independently wait for TE-1 and TE-R
#below line for main.py
GPIO.wait_for_edge(in_channel_TE1, GPIO.RISING)
GPIO.wait_for_edge(in_channel_TER, GPIO.RISING)
#}



#read and print sensor data

#List all telemetry output data:
#    -Acceleration [3 axes?]
#    -
#    -
#
#

#locally save data, then modify it to fit in telemetry properly

#may need multi-core processing for fast pipelining from data sources to telemetry.

#Determine maximum practical data rate
    #Trade offs: -Payload items for telemetry performance
    #            -Payload items' rate, also for telemetry performance.
    #seems trivial, UTF-8 requires very rare characters for increased byte usage
telemetry_array = []
