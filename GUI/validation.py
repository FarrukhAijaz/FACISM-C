import os
from tkinter import messagebox

def validate_inputs(swc_name, directory):
    """Validate user inputs and show appropriate error messages."""
    if not swc_name:
        messagebox.showerror("Validation Error", "SWC name cannot be empty.")
        return False
    if not directory:
        messagebox.showerror("Validation Error", "Directory cannot be empty.")
        return False
    if not os.path.isdir(directory):
        messagebox.showerror("Validation Error", f"'{directory}' is not a valid directory.")
        return False
    return True
