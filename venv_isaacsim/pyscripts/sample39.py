from omni.isaac.dynamic_control import _dynamic_control
import numpy as np
dc = _dynamic_control.acquire_dynamic_control_interface()
articulation = dc.get_articulation("/Franka")
dc.wake_up_articulation(articulation)
joint_efforts = [-np.random.rand(9) * 1000]
dc.set_articulation_dof_efforts(articulation, joint_efforts)