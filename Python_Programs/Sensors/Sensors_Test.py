import board
import busio
import time

#Note: Include relative directory for main import
import Sensor_Libs_RSX.Temperature_Code_TMP006 as T6
import Sensor_Libs_RSX.Distance_Code_vl53l0x as D

#Note: Python does appear to be okay with making imports multiple times;
#The imported project code libraries also contain imports of regular Python libraries.

#create sensor objects
dist_sensor = D.dist_create_input()
temp_sensor = T6.create_TMP006()

print("temp output!")
print(T6.return_temp_TMP006(temp_sensor))

print("dist output!")
print(D.dist_print_data(dist_sensor))
print("\n")
