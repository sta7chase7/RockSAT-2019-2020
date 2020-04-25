import board
import busio
import time
import Temperature_Code_TMP006 as T6
import Distance_Code_vl53l0x as D

#create sensor objects
dist_sensor = D.dist_create_input()
temp_sensor = T6.create_TMP006()

print("temp output!")
print(T6.return_temp_TMP006(temp_sensor))
print("\n")

print("dist output!")
print(D.dist_print_data(dist_sensor))
print("\n")