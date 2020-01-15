import board
import analogio

def temp_create_input(pin):
    return analogio.AnalogIn(board.pin)


def tmp36_temperature_F(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    c_temp = (millivolts - 500) / 10
    f_temp = c_temp *(1.8) + 32
    return f_temp