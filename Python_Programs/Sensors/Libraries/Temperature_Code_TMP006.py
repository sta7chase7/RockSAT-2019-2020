import time
import board
import busio
import adafruit_tmp006

# Define a function to convert celsius to fahrenheit.
#Sensor outputs C under a normal configuration.
def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

# Create library object using our Bus I2C port
def create_TMP006():
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_tmp006.TMP006(i2c)
    return sensor

# Initialize communication with the sensor, using the default 16 samples per conversion.
# This is the best accuracy but a little slower at reacting to changes.
# The first sample will be meaningless
def return_temp_TMP006(sensor):
    while True:
        obj_temp = sensor.temperature
        time.sleep(1.0)
        return obj_temp
