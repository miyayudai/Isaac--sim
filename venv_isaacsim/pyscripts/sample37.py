from pxr import UsdPhysics
stage = omni.usd.get_context().get_stage()
for prim in stage.TraverseAll():
    prim_type = prim.GetTypeName()
    if prim_type in ["PhysicsRevoluteJoint" , "PhysicsPrismaticJoint"]:
        if prim_type == "PhysicsRevoluteJoint":
            drive = UsdPhysics.DriveAPI.Get(prim, "angular")
        else:
            drive = UsdPhysics.DriveAPI.Get(prim, "linear")
        if drive:
            drive.GetStiffnessAttr().Set(0)
from omni.isaac.dynamic_control import _dynamic_control
import numpy as np
dc = _dynamic_control.acquire_dynamic_control_interface()
#Note: getting the articulation has to happen after changing the drive stiffness
articulation = dc.get_articulation("/Franka")
dc.wake_up_articulation(articulation)
joint_vels = [-np.random.rand(9)*10]
dc.set_articulation_dof_velocity_targets(articulation, joint_vels)