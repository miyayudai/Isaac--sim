from omni.isaac.dynamic_control import _dynamic_control
dc = _dynamic_control.acquire_dynamic_control_interface()

# Check to see what type of object the target prim is
obj_type = dc.peek_object_type("/Franka")
# This print statement should print ObjectType.OBJECT_ARTICULATION
print(obj_type)