#Author:			Segev Moran
#
#General Description:		Program for Arm Function
#
#Version:			2.1
#
#Note: Please use the Mountain Time zone and 24-hour/military time.
#Daylight/Standard Time:	Daylight
#Start Date/Time:		11/27/2019, 17:45
#End-of-Revision Date/Time:	11/27/2019, 18:42
#Copyright:			CCoC RocketSat 2019/2020


#Inputs:			
  #TE2 Status from rocket VIA GPIO pins
#False = fairing is on
#True = fairing has deployed
							
#Outputs:			same standard as for inputs

  #camera_arm_satus Output status for GPIO pins to Telemetry Analog line


							
#Test Input/Output Values:
#	Input Values:
#	Output Values:



#Import
from adafruit_motorkit import MotorKit
 #instructions for installing motor library
 #https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software

kit1 = MotorKit()
#stepper1 == armDoor motor 
#stepper2 == cameraArm motor


#Internal Variable Definitions

TE2 = False
#variable saying TE2 has happened

camera_arm = True
#cameraArm = True == arm retracted
#cameraArm = False == arm extended

camera_arm_satus = False
#variable for if the camera has extended


#Function Definitions
def arm_extend():
  #extends arm 
  for i in range(100):
    #range needs to change depending on arm requirements
    kit1.stepper1.onestep(direction.FORWARD)
    kit1.stepper2.onestep(direction.FORWARD)
    camera_arm = False
    camera_arm_satus = True

def arm_retract():
  #extends arm 
  for i in range(100):
    #range needs to change depending on arm requirements 
    kit1.stepper1.onestep(direction.BACKWARD)
    kit1.stepper2.onestep(direction.BACKWARD)
    camera_arm = True
    camera_arm_satus = False

#Timer Events
TE2_Timer = Threading.Timer(8.0,arm_extend)

retract_timer = Threading.Timer(220.0,arm_retract)


#Events
if TE2 = True:
  when speed =< 10hz:
    #checks accelormeter for rocket speed
    TE2_Timer.start()
    retract_timer.start()