# gui/validation.py
import os

def validate_inputs(swc_name, directory):
    if not swc_name:
        raise ValueError("SWC name cannot be empty.")
    if not directory or not os.path.isdir(directory):
        raise ValueError("Invalid directory specified.")
    return True