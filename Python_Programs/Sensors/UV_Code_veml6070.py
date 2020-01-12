# This code will be used to controll the UV sensor
# https://learn.adafruit.com/adafruit-veml6070-uv-light-sensor-breakout/python-circuitpython

import time
import busio
import board
import adafruit_veml6070

def UV_values():
    with busio.I2C(board.SCL, board.SDA) as i2c:
        uv = adafruit_veml6070.VEML6070(i2c)
        uv_raw = uv.read
        risk_level = uv.get_index(uv_raw)
    return [uv_raw,risk_level]

def UV_print(uv_raw, risk_level):
    print('Reading: {0} | Risk Level: {1}'.format(uv_raw, risk_level))