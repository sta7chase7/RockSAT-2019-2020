import board
import analogio

def temp_create_input():
    return analogio.AnalogIn(board.A0)


def temp_value(tmp_obj):
    return tmp_obj.value