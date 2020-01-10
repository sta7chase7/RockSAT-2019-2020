#imports
import analogio
import board
import time
import busio
import multiprocessing
import RPi.GPIO

#Motor stuff
from adafruit_motorkit import MotorKit

#Accelerometer
import Sensors.Accelerometer_Code_ADXL377

#Distance sensor
import Sensors.Distance_Code_vl53l0x

#temp sensor import
import Sensors.Temperature_Code_TMP36

#UV sensor

#May need separate folders and inits for each file import
#https://stackoverflow.com/questions/50559539/import-a-file-from-another-location-python

#create input objects for all sensors



#GPIO:
#send "power on" signal to MADV
#Send "start recording" signal to MADV




#List of things to do (unordered)
#--------------------------------
#
#set delay for time between GSE-On and launch (see CDR)
#offset timer by GSE-On delay
#
#--------------------------------