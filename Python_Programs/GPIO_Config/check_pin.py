import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for g in range(54):
    print("gpio {} is {}".format(g, GPIO.gpio_function(g)))