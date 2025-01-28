import os

def create_unit_model(i, subcomponent_dir, subcomponent_name, num_units, eng):
    for j in range(1, num_units + 1):
            unit_name = f"sc_{i}_unit_{j}"
            unit_dir = os.path.join(subcomponent_dir, unit_name)
            os.makedirs(unit_dir, exist_ok=True)
            unit_name = f"sc_{i}_unit_{j}"
            unit_dir = os.path.join(subcomponent_dir, unit_name)
            os.makedirs(unit_dir, exist_ok=True)

            """Create a unit model with Inport, Gain block, and Outport."""
            unit_slx = os.path.join(unit_dir, f"{unit_name}.slx")
            eng.new_system(unit_name, nargout=0)

            # Add Inport, Gain block, and Outport
            eng.add_block('simulink/Sources/In1', f"{unit_name}/In1", nargout=0)
            eng.add_block('simulink/Math Operations/Gain', f"{unit_name}/Gain", nargout=0)
            eng.add_block('simulink/Sinks/Out1', f"{unit_name}/Out1", nargout=0)

            # Set Gain value (can be customized or parameterized)
            eng.set_param(f"{unit_name}/Gain", 'Gain', '5'+ j, nargout=0)

            # Position blocks for better visual layout
            eng.set_param(f"{unit_name}/In1", 'Position', '[100, 100, 130, 130]', nargout=0)
            eng.set_param(f"{unit_name}/Gain", 'Position', '[200, 100, 230, 130]', nargout=0)
            eng.set_param(f"{unit_name}/Out1", 'Position', '[300, 100, 330, 130]', nargout=0)

            # Connect blocks: Inport -> Gain -> Outport
            eng.add_line(unit_name, 'In1/1', 'Gain/1', nargout=0)
            eng.add_line(unit_name, 'Gain/1', 'Out1/1', nargout=0)

            # Save the system
            eng.save_system(unit_name, unit_slx, nargout=0)

            # Add a Model Reference block in the subcomponent and reference the unit model
            model_ref_block_name = f"{subcomponent_name}/ModelReference_{unit_name}"
            eng.add_block('simulink/Ports & Subsystems/Model', model_ref_block_name, nargout=0)
            eng.set_param(model_ref_block_name, 'ModelName', unit_name, nargout=0)
            
            # Position the Model Reference block
            block_position_x = 100 + (j * 150)
            eng.set_param(model_ref_block_name, 'Position', f"[{block_position_x}, 100, {block_position_x + 50}, 130]", nargout=0)
           

def create_subcomponent_model(swc_name, swc_dir, num_subcomponents, num_units, eng):
    for i in range(1, num_subcomponents + 1):
        subcomponent_name = f"subcomponent_{i}"
        subcomponent_dir = os.path.join(swc_dir, subcomponent_name)
        os.makedirs(subcomponent_dir, exist_ok=True)
        
        # Create Subcomponent .slx file
        subcomponent_slx = os.path.join(subcomponent_dir, f"{subcomponent_name}.slx")
        eng.new_system(subcomponent_name, nargout=0)
        
        # Create each unit within the subcomponent
        create_unit_model(i, subcomponent_dir, subcomponent_name, num_units, eng)
        
        # Save the Subcomponent system
        eng.save_system(subcomponent_name, subcomponent_slx, nargout=0)
        
        # Add a Model Reference block in the SWC and reference the subcomponent model
        model_ref_block_name_swc = f"{swc_name}/ModelReference_{subcomponent_name}"
        eng.add_block('simulink/Ports & Subsystems/Model', model_ref_block_name_swc, nargout=0)
        eng.set_param(model_ref_block_name_swc, 'ModelName', subcomponent_name, nargout=0)
        
        # Position the Model Reference block
        block_position_x_swc = 100 + (i * 200)
        eng.set_param(model_ref_block_name_swc, 'Position', f"[{block_position_x_swc}, 100, {block_position_x_swc + 50}, 130]", nargout=0)

def add_model_reference(eng, parent_name, model_name, ref_name, position):
    """Add a Model Reference block to the parent model."""
    model_ref_block_name = f"{parent_name}/{ref_name}"
    eng.add_block('simulink/Ports & Subsystems/Model', model_ref_block_name, nargout=0)
    eng.set_param(model_ref_block_name, 'ModelName', model_name, nargout=0)
    eng.set_param(model_ref_block_name, 'Position', position, nargout=0)
