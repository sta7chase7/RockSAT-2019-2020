import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
#________________________________
#Inputs:
#move_cmd - 0 or 1 - whether or not the motor is being commanded to move
#direction -  or 1 or 2 - null, backward or forward, respectively
#running - 0 or 1 or 2 - null, not running, running, respectively
#________________________________
def full_move(move_cmd,direction=0,running=0):
    kit = MotorKit()
    direction_map = [BACKWARD, FORWARD]
    step_count = 100
    sleep_between_steps = 0.001
    if move_cmd == 1:
        #set move_cmd state to true
        status_array.append(0)
        if running == 2:
            print("Process already running!")
        if running == 1:
            try:
                #update direction state in output list
                status_array.append(direction)
                #show whether or not the process is running
                status_array.append(2)

                for i in range(step_count):
                    kit.stepper1.onestep(direction=stepper.direction_map[direction], style=stepper.DOUBLE)
                    time.sleep(sleep_between_steps)
            except:
                print("error!")
    if move_cmd == 0:
        status_array = [0,0,0]
    return status_array