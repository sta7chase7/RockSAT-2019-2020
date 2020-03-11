import RPi.GPIO

channel = 

GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel

if GPIO.event_detected(channel):
    print('output!')