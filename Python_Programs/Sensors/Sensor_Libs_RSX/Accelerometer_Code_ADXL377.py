import analogio
import board
import time

#Requires testing on hardware

# Create analog inputs for each ADXL335 axis.
def accel_create_input_3ax(pin_1,pin_2,pin_3):
    return [analogio.AnalogIn(board.pin_1),analogio.AnalogIn(board.pin_2),analogio.AnalogIn(board.pin_3)]

# Define function to convert raw analog values to gravities.
def accel_value(axis):
    # Convert axis value to float within 0...1 range.
    val = axis.value / 65535
    # Shift values to true center (0.5).
    val -= 0.5
    # Convert to gravities.
    return val * 3.0

# Main loop prints acceleration every second.
def accel_array(x_axis,y_axis,z_axis):
    time.sleep(1.0)
    x = accel_value(x_axis)
    y = accel_value(y_axis)
    z = accel_value(z_axis)
    return [x,y,z]
