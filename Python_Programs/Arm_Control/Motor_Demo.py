"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
from adafruit_motorkit import MotorKit

kit = MotorKit()
try:
    for i in range(100):
        kit.stepper1.onestep()
        time.sleep(0.001)
except:
    print("error!")