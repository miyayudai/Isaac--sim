from omni.isaac.dynamic_control import _dynamic_control
import numpy as np
dc = _dynamic_control.acquire_dynamic_control_interface()
articulation = dc.get_articulation("/Franka")
dc.wake_up_articulation(articulation)
dof_ptr = dc.find_articulation_dof(articulation, "panda_joint2")
dc.set_dof_position_target(dof_ptr, -1.5)