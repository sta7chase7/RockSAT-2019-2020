# This code will be used to control the distance sensor
#Documentation https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython

import board
import busio
import adafruit_vl53l0x

#Create sensor object
def dist_create_input():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_vl53l0x.VL53L0X(i2c)
    return sensor

#return range value
def dist_print_data(sensor):
    #distance is in mm
    return sensor.range
