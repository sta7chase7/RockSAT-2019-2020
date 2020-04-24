import RPi.GPIO as GPIO
import time

#These functions' pins need to be tested with a voltmeter
def TE_1_Event(out_channel):
    GPIO.output(out_channel, GPIO.HIGH)
    #time.sleep may cause the arm function to start extend/retract cycle WHILE signal is high, not just once around. Test!
    #suspend state for 2s
    time.sleep(2)
    #Reset pin state
    GPIO.output(out_channel, GPIO.LOW)
    #Note: remove all print statements before final payload integration
    return 1

def TE_R_Event():
    GPIO.output(out_channel_TER, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(out_channel, GPIO.LOW)
    return 1