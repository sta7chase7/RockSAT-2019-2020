import time
from picamera import PiCamera

#possible mode states: "event" xor "time" xor "hybrid"
def PiCam_Record(mode,save_dir_string,recording_interval_s=None,event_call=None):
    camera = PiCamera()
    camera.start_recording(save_dir_string)
    if mode == "time":
        time.sleep()
        camera.stop_recording()
    if mode == "event":
        if event_call == True:
            camera.stop_recording()
    if mode == "hybrid":
        if (bool(time.sleep(recording_interval_s)) == False) or (event_call == True):
            camera.stop_recording()