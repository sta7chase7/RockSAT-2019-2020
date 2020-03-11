import RPi.GPIO as GPIO

#use BCM notation for GPIO pins
GPIO.setmode(GPIO.BCM)

in_channel = 6
out_channel = 5

GPIO.setup(in_channel, GPIO.IN)
GPIO.setup(out_channel, GPIO.OUT)

GPIO.add_event_detect(in_channel, GPIO.RISING)  # add rising edge detection on a channel

GPIO.output(out_channel, GPIO.HIGH)

if GPIO.event_detected(in_channel):
    print('output!')

GPIO.cleanup()