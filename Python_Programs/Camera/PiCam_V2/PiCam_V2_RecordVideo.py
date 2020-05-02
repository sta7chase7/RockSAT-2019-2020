import time # Controls Time Intervals and sleep
import datetime #Allow recording of date and time stamps
from datetime import datetime #Need to ensure datetime module is installed
import os.path # Allows management of path names
import picamera # Nifty Pi Camera Commands
from picamera import PiCamera #Make sure function PiCamera is defined

def PiCam_Record():
    """ Controls the recording loop and saving intervals for the pi camera"""

    #Names camera and specifies recording features:
    camera = PiCamera()
    camera.framerate = 30
    video_stabilization = True

    #Start Recording and Store Video Files to the specified path
    #Concatenate the video name, datetime, and file type
    #Only store as .h624 format
    save_path = "/home/pi/Desktop/PiVideo/"
    #Stores as .h624 format (Pi Cam Default), can be converted easily with VLC Player
    file_timestamp = datetime.now().strftime("%y%m%d_%H%M%S.h264") 
    file_name = "Pi_Vid_" + file_timestamp
    video_name = os.path.join(save_path, file_name)

    try:
        #Start recording for duration of time delay:
        camera.start_recording(video_name)
        #Test Print:
        #print(video_name, "is recording and things!")

        #(WARNING: Measured in seconds, NOT mili-seconds!!!)
        time.sleep(60)
        camera.stop_recording()

    #Always end picamera module commands with camera.close():
    finally:
        camera.close()
        #Test Print:
        #print("Camera is done flurbling!")
    
    return;


#For Main create a while loop:
#While Pi Zero = On record
#Function will record in set interval (seconds).
#Note: other camera commands might be set in miliseconds):
#Example:
"""
if__name__=="__main__"

while:                                  #Sys read on, voltage reading, or other benchmark
    PiCam_Record()                      #will record in intervals over loop

    elif:
        break
        
"""

