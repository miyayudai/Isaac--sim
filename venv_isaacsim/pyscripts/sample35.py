from omni.isaac.dynamic_control import _dynamic_control
import numpy as np
dc = _dynamic_control.acquire_dynamic_control_interface()
articulation = dc.get_articulation("/Franka")
# Call this each frame of simulation step if the state of the articulation is changing.
dc.wake_up_articulation(articulation)
joint_angles = [np.random.rand(9) * 2 - 1]
dc.set_articulation_dof_position_targets(articulation, joint_angles)