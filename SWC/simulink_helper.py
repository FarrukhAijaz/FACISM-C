import os

def create_unit_model(eng, unit_name, unit_dir):
    """Create a unit model with Inport, Gain block, and Outport."""
    unit_slx = os.path.join(unit_dir, f"{unit_name}.slx")
    eng.new_system(unit_name, nargout=0)

    # Add Inport, Gain block, and Outport
    eng.add_block('simulink/Sources/In1', f"{unit_name}/In1", nargout=0)
    eng.add_block('simulink/Math Operations/Gain', f"{unit_name}/Gain", nargout=0)
    eng.add_block('simulink/Sinks/Out1', f"{unit_name}/Out1", nargout=0)

    # Set Gain value (can be customized or parameterized)
    eng.set_param(f"{unit_name}/Gain", 'Gain', '5', nargout=0)

    # Position blocks for better visual layout
    eng.set_param(f"{unit_name}/In1", 'Position', '[100, 100, 130, 130]', nargout=0)
    eng.set_param(f"{unit_name}/Gain", 'Position', '[200, 100, 230, 130]', nargout=0)
    eng.set_param(f"{unit_name}/Out1", 'Position', '[300, 100, 330, 130]', nargout=0)

    # Connect blocks: Inport -> Gain -> Outport
    eng.add_line(unit_name, 'In1/1', 'Gain/1', nargout=0)
    eng.add_line(unit_name, 'Gain/1', 'Out1/1', nargout=0)

    # Save the system
    eng.save_system(unit_name, unit_slx, nargout=0)
    return unit_slx

def create_subcomponent_model(eng, subcomponent_name, subcomponent_dir, unit_names):
    """Create a subcomponent model and add model references to unit models."""
    subcomponent_slx = os.path.join(subcomponent_dir, f"{subcomponent_name}.slx")
    eng.new_system(subcomponent_name, nargout=0)

    # Add Model Reference blocks for each unit
    for idx, unit_name in enumerate(unit_names, start=1):
        model_ref_block_name = f"{subcomponent_name}/ModelReference_{unit_name}"
        eng.add_block('simulink/Ports & Subsystems/Model', model_ref_block_name, nargout=0)
        eng.set_param(model_ref_block_name, 'ModelName', unit_name, nargout=0)

        # Position blocks
        block_position_x = 100 + (idx * 150)
        eng.set_param(model_ref_block_name, 'Position', f"[{block_position_x}, 100, {block_position_x + 50}, 130]", nargout=0)

    # Save the system
    eng.save_system(subcomponent_name, subcomponent_slx, nargout=0)
    return subcomponent_slx

def add_model_reference(eng, parent_name, model_name, ref_name, position):
    """Add a Model Reference block to the parent model."""
    model_ref_block_name = f"{parent_name}/{ref_name}"
    eng.add_block('simulink/Ports & Subsystems/Model', model_ref_block_name, nargout=0)
    eng.set_param(model_ref_block_name, 'ModelName', model_name, nargout=0)
    eng.set_param(model_ref_block_name, 'Position', position, nargout=0)
