import RPi.GPIO as GPIO
import time

#These functions' pins need to be tested with a voltmeter

#Trigger voltage changes on a BCM channel
def TE_1_Event(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    #time.sleep may cause the arm function to start extend/retract cycle WHILE signal is high, not just once around. Test!
    #suspend state for 2s
    time.sleep(high_time)
    #Reset pin state
    GPIO.output(out_channel, GPIO.LOW)
    #Note: remove all print statements before final payload integration
    return 1

def TE_R_Event(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

#Get data on MADV terminal timing in order to fill these out.
#Add state information returns

def MADV_On(out_channel):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

def MADV_Off(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

def MADV_Record_Start(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

def MADV_Record_Stop(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

def MADV_Recording_Mode(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

def MADV_Storage_Mode(out_channel, high_time):
    GPIO.output(out_channel, GPIO.HIGH)
    time.sleep(high_time)
    GPIO.output(out_channel, GPIO.LOW)
    return 1

