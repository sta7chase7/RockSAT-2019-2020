import RPi.GPIO as GPIO
import time
import 

#Pin modes
#0 = GPIO.OUT
#1 = GPIO.IN
#40 = GPIO.SERIAL
#41 = GPIO.SPI
#42 = GPIO.I2C
#43 = GPIO.HARD_PWM
#-1 = GPIO.UNKNOWN

#Reference BCM pin convention; see pinout.xyz.
#GPIO pinout does not vary across Pi models.
GPIO.setmode(GPIO.BCM)



#Assign I/O channel BCM numbers.
#Max BCIM number on Pi's appears to be 26.
in_channel_TE1 = 17
in_channel_TER = 27

out_channel_TE1 = 5
out_channel_TER = 6

#Reconfigure the following pins to the proper modes;
    #BCM 17,27 - Inputs
    #BCM 5, 6 - Outputs
GPIO.setup(in_channel_TE1, GPIO.IN)
GPIO.setup(in_channel_TER, GPIO.IN)

GPIO.setup(out_channel_TE1, GPIO.OUT)
GPIO.setup(out_channel_TER, GPIO.OUT)

str = """GPIO.wait_for_edge(in_channel_TE1, GPIO.RISING)

GPIO.output(out_channel, GPIO.HIGH)
print("output pin set to high")

if GPIO.event_detected(in_channel):
    print('output!')
"""

#GPIO.cleanup()
