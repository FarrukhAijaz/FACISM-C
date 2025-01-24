import os
import matlab.engine    

def create_autosar_structure(swc_name, num_subcomponents, num_units, use_predefined_settings, base_directory):
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()
    
    # Define the base directory (Downloads in Ubuntu)
    if base_directory is None:
        base_directory = os.path.expanduser('~/Downloads')
    
    # Create SWC directory
    swc_dir = os.path.join(base_directory, swc_name)
    os.makedirs(swc_dir, exist_ok=True)
    
    # Create SWC .slx file
    swc_slx = os.path.join(swc_dir, f"{swc_name}.slx")
    eng.new_system(swc_name, nargout=0)
    eng.save_system(swc_name, swc_slx, nargout=0)
    

    
    for i in range(1, num_subcomponents + 1):
        subcomponent_name = f"subcomponent_{i}"
        subcomponent_dir = os.path.join(swc_dir, subcomponent_name)
        os.makedirs(subcomponent_dir, exist_ok=True)
        
        # Create Subcomponent .slx file
        subcomponent_slx = os.path.join(subcomponent_dir, f"{subcomponent_name}.slx")
        eng.new_system(subcomponent_name, nargout=0)
        eng.save_system(subcomponent_name, subcomponent_slx, nargout=0)
        
        for j in range(1, num_units + 1):
            unit_name = f"sc_{i}_unit_{j}"
            unit_dir = os.path.join(subcomponent_dir, unit_name)
            os.makedirs(unit_dir, exist_ok=True)
            
            # Create Unit .slx file
            unit_slx = os.path.join(unit_dir, f"{unit_name}.slx")
            eng.new_system(unit_name, nargout=0)
            eng.save_system(unit_name, unit_slx, nargout=0)
    
    # Stop MATLAB engine
    eng.quit()

    print(f"Successfully created AUTOSAR structure for {swc_name} at {swc_dir}")

# Example usage with default values
swc_name = "SWC_Example"
num_subcomponents = 2
num_units = 3
use_predefined_settings = True  # Placeholder for predefined settings logic
base_directory = None  # Will default to the Downloads folder in Ubuntu

create_autosar_structure(swc_name, num_subcomponents, num_units, use_predefined_settings, base_directory)
