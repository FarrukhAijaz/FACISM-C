import os
import matlab.engine    
from SWC.simulink_helper import create_subcomponent_model

def create_autosar_structure(swc_name, num_subcomponents, num_units, use_predefined_settings, base_directory):
    # Start MATLAB engine
    eng = matlab.engine.start_matlab()
    
    # Define the base directory (Desktop in Ubuntu)
    if base_directory is None:
        base_directory = os.path.expanduser('~/Desktop')
    
    # Create SWC directory
    swc_dir = os.path.join(base_directory, swc_name)
    os.makedirs(swc_dir, exist_ok=True)
    
    # Create SWC .slx file
    swc_slx = os.path.join(swc_dir, f"{swc_name}.slx")
    eng.new_system(swc_name, nargout=0)
    
    # Loop through each subcomponent
    create_subcomponent_model(swc_name, swc_dir, num_subcomponents, num_units, eng)    
    
    # Save the SWC system
    eng.save_system(swc_name, swc_slx, nargout=0)
    
    # Stop MATLAB engine
    eng.quit()

    print(f"Successfully created AUTOSAR structure for {swc_name} at {swc_dir}")

# Example usage with default values
swc_name = "SWC_Example"
num_subcomponents = 2
num_units = 3
use_predefined_settings = True  # Placeholder for predefined settings logic
base_directory = None  # Will default to the Desktop folder in Ubuntu

create_autosar_structure(swc_name, num_subcomponents, num_units, use_predefined_settings, base_directory)
