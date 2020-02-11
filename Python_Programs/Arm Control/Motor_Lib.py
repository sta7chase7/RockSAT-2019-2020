import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
#________________________________
#Inputs:
#move_cmd - 0 or 1 - whether or not the motor is being commanded to move
#direction - 0 or 1 - backward or forward, respectively
#running - 0 or 1 - whether or not the motor is currently running
#________________________________
def full_move(move_cmd,direction,running):
    kit = MotorKit()
    direction_map = [BACKWARD, FORWARD]
    if move_cmd == 1:
        if running == 1:
            break
        if running == 0:
            try:
                status_array[2] = 1
                status_array[1] = direction
                for i in range(100):
                    kit.stepper1.onestep(direction=stepper.direction_map[direction], style=stepper.DOUBLE)
                    time.sleep(0.001)
            except:
                break
    if move_cmd == 0:
        status_array = [0,0,0]
    return status_array