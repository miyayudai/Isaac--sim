from omni.isaac.dynamic_control import _dynamic_control
dc = _dynamic_control.acquire_dynamic_control_interface()

# Get a handle to the Franka articulation
# This handle will automatically update if simulation is stopped and restarted
art = dc.get_articulation("/Franka")

# Get information about the structure of the articulation
num_joints = dc.get_articulation_joint_count(art)
num_dofs = dc.get_articulation_dof_count(art)
num_bodies = dc.get_articulation_body_count(art)

# Get a specific degree of freedom on an articulation
dof_ptr = dc.find_articulation_dof(art, "panda_joint2")

# print the information
print("Articulation:", art)
print("Joint count:", num_joints)
print("DOF count:", num_dofs)
print("Body count:", num_bodies)
print("DOF pointer for panda_joint2:", dof_ptr)