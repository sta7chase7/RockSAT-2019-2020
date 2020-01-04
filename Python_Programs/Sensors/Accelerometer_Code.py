# This code will be used to controll the Accelerometer sensor
# Documantation @ https://learn.adafruit.com/adafruit-mma8451-accelerometer-breakout/python-circuitpython
import board
import busio
import adafruit_mma8451

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mma8451.MMA8451(i2c)

x, y, z = sensor.acceleration
print('Acceleration: x={0:0.3f} m/s^2 y={1:0.3f} m/s^2 z={2:0.3f} m/s^2'.format(x, y, z))
