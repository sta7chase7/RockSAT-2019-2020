import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#BCM correlates to an integer for gpio_function

#0 = GPIO.OUT
#1 = GPIO.IN
#40 = GPIO.SERIAL
#41 = GPIO.SPI
#42 = GPIO.I2C
#43 = GPIO.HARD_PWM
#-1 = GPIO.UNKNOWN

#The GPIO.UNKNOWN pins should be our primary candidates for TE-1 and TE-R inputs

for g in range(54):
    print("gpio {} is {}".format(g, GPIO.gpio_function(g)))
