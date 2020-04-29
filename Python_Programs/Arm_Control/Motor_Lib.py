import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

#clean up & case test

#recheck and make sure this is up to date with code syntax
#________________________________
#Inputs:
#move_cmd - 0 or 1 - whether or not the motor is being commanded to move
#direction - 0 or 1 - null, backward or forward, respectively
#running - 0 or 1 or 2 - null, not running, running, respectively
#________________________________
def full_move(move_cmd,direction=0,running=1):
    kit = MotorKit()
    direction_map = [stepper.BACKWARD, stepper.FORWARD]
    step_count = 100
    status_array = []
    sleep_between_steps = 0.01
    if move_cmd == 1:
        #set move_cmd state to true
        status_array.append(1)
        if running == 2:
            print("Process already running!")
            return status_array
        if running == 1:
            try:
                #update direction state in output list
                status_array.append(direction)
                #show whether or not the process is running
                status_array.append(2)

                for i in range(step_count):
                    kit.stepper1.onestep(direction=direction_map[direction], style=stepper.DOUBLE)
                    time.sleep(sleep_between_steps)
                return status_array
            except:
                print("error!")
                return status_array
    if move_cmd == 0:
#        status_array = [0,0,0]
        return status_array
    return status_array
    