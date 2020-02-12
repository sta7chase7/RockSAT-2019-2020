#Author:              Mac Grove
#
#Language:            Python/ Bash
#
#General Description: Program for video retrival
#
#Version:			  1.0
#
#Copyright:			  CCoC RocketSat 2019/2020

import os
import subprocess
#Added escape chars by {} to make Python happy
bash_copy_string_1 = "find /home/bathan/Downloads/ -name 'carrot*' -exec cp \"{}\" /home/bathan/Documents/  \;"
bash_copy_list_1 = ["find", "/home/bathan/Downloads/", "-name", "'carrot*'", "-exec", "cp", "\"{}\"", "/home/bathan/Documents/"  "\;"]