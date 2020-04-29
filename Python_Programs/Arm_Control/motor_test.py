import Motor_Lib as M

obj_static = M.full_move(move_cmd=0,direction=1)
print(obj_static,"static test complete!")
obj_backward = M.full_move(move_cmd=1,direction=0)
print(obj_backward,"backwards test complete!")
obj_forward=M.full_move(move_cmd=1,direction=1)
print(obj_forward,"forwards test complete!")
