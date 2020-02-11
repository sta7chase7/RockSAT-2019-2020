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
    step_count = 100
    sleep_between_steps = 0.001
    if move_cmd == 1:
        #set move_cmd state to true
        status_array.append(0)
        if running == 1:
            break
        if running == 0:
            try:
                #update direction state in output list
                status_array.append(direction)
                #show whether or not the process is running
                status_array.append(1)
                for i in range(step_count):
                    kit.stepper1.onestep(direction=stepper.direction_map[direction], style=stepper.DOUBLE)
                    time.sleep(sleep_between_steps)
            except:
                break
    if move_cmd == 0:
        status_array = [0,0,0]
    return status_array