from recording_def import Recording

video = Recording()
video.toggle_recording(recording_interval_s=15,fps=15,source_data='keyboard_cat.mp4',out_file='keyboard_cat_avi_1.avi',show_stream=False)
#video.printObject()