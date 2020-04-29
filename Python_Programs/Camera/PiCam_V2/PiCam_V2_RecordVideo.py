import time
from picamera import PiCamera

#Needs update work on state assignments/returns

#possible mode states: "event" xor "time" xor "hybrid"
def PiCam_Record(mode,save_dir_string,recording_interval_s=None,event_call=None):

    #Move the line below to main_pi3b? - making a new object may cause delays.
    camera = PiCamera()

    camera.start_recording(save_dir_string)
    camera_state = 0

    #Have the camera record for a set interval
    if mode == "time":
        time.sleep(recording_interval_s)
        camera.stop_recording()

    #Event mode assumes that pi cam will be recording already.
    if mode == "event":
        if event_call == True:
            camera.stop_recording()

    #Stop if either of the two events gets triggered
    if mode == "hybrid":
        if (bool(time.sleep(recording_interval_s)) == False) or (event_call == True):
            camera.stop_recording()