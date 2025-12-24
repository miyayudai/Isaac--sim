from omni.isaac.dynamic_control import _dynamic_control
dc = _dynamic_control.acquire_dynamic_control_interface()

# Print the state of each degree of freedom in the articulation
art = dc.get_articulation("/Franka")
dof_states = dc.get_articulation_dof_states(art, _dynamic_control.STATE_ALL)
print(dof_states)

# Get state for a specific degree of freedom
dof_ptr = dc.find_articulation_dof(art, "panda_joint2")
dof_state = dc.get_dof_state(dof_ptr, _dynamic_control.STATE_ALL)
# print position for the degree of freedom
print(dof_state.pos)