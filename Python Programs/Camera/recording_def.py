#Pi = Apollo
#Program to split video
import cv2
import numpy as np
import time

class Recording():
    def __init__(self, recording=False,show_stream=False,recording_interval_s=None,frame_width=None,frame_height=None,fps=None,source_data=None,out_file=None):
        self.recording = recording
        self.recording_interval_s = recording_interval_s
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.fps = fps
        self.source_data = source_data
        self.out_file = out_file
        self.show_stream = show_stream

    def FPS_to_FrameDelay_ms(self,fps):
        frame_delay_s = 1/fps
        return round(frame_delay_s*1000)

    def toggle_recording(self,recording_interval_s,fps,source_data,out_file,show_stream=False):
        #toggle the recording state
        self.recording = not self.recording
        #set up a recording instance if the state is set to True.
        if (self.recording == True):
            inStream = cv2.VideoCapture(source_data)
            frame_width = int(inStream.get(3))
            frame_height = int(inStream.get(4))
            outStream = cv2.VideoWriter(out_file,cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
            initial_time = time.perf_counter()
            while((time.perf_counter() - initial_time) < recording_interval_s):
                ret, frame = inStream.read()
                if (ret == True):
                    outStream.write(frame)
                    if(show_stream == True):
                        cv2.imshow('Frame',frame)
                    cv2.waitKey(self.FPS_to_FrameDelay_ms(fps))

                else:
                    break
            self.recording = not self.recording
            outStream.release()
#            outStream.destroyallWindows()
    def printObject(self):
        print("Recording state is: ",self.recording)

#video = Recording()
#video.toggle_recording(recording_interval_s=15,fps=15,source_data='keyboard_cat.mp4',out_file='keyboard_cat_avi_1.avi')
#video.printObject()
