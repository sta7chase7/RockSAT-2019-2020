import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

in_channel = 6
out_channel = 5

GPIO.setup(in_channel, GPIO.IN)
GPIO.setup(out_channel, GPIO.OUT)

GPIO.add_event_detect(in_channel, GPIO.RISING)  # add rising edge detection on a channel

GPIO.output(out_channel, GPIO.HIGH)
print("output pin set to high")

if GPIO.event_detected(in_channel):
    print('output!')
print("sleeping!")
time.sleep(10)
print("done sleeping!")

GPIO.cleanup()