import RPi.GPIO as GPIO

GPIO.setup(26, 'output')

# Switch on
GPIO.output(26, GPIO.HIGH)

# To read the state
state = GPIO.input(26)
if state:
   print('on')
else:
   print('off')