import Motor_Lib as M

M.full_move(move_cmd=1,direction=1)
print("static test complete!")
M.full_move(move_cmd=1,direction=1)
print("backwards test complete!")
M.full_move(move_cmd=1,direction=2)
print("forwards test complete!")