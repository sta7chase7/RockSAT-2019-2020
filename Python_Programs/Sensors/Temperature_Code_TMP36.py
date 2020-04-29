import board
import analogio

#make object
def temp_create_input(pin):
    return analogio.AnalogIn(board.pin)

#convert values and return temperature (C)
def tmp36_temperature_F(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    c_temp = (millivolts - 500) / 10
#    f_temp = c_temp *(1.8) + 32
    return c_temp
