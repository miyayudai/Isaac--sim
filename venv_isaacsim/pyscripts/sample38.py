from pxr import UsdPhysics
stage = omni.usd.get_context().get_stage()
panda_joint2_drive = UsdPhysics.DriveAPI.Get(stage.GetPrimAtPath("/Franka/panda_link1/panda_joint2"), "angular")
panda_joint2_drive.GetStiffnessAttr().Set(0)
from omni.isaac.dynamic_control import _dynamic_control
import numpy as np
dc = _dynamic_control.acquire_dynamic_control_interface()
#Note: getting the articulation has to happen after changing the drive stiffness
articulation = dc.get_articulation("/Franka")
dc.wake_up_articulation(articulation)
dof_ptr = dc.find_articulation_dof(articulation, "panda_joint2")
dc.set_dof_velocity_target(dof_ptr, 0.2)