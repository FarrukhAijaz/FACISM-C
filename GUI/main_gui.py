import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from SWC.swc_creator import create_autosar_structure  # Import the SWC creation function


def launch_gui():
    """Launch the GUI."""
    def browse_directory():
        """Open a file explorer to select a directory."""
        selected_directory = filedialog.askdirectory(initialdir="~/Downloads", title="Select Directory")
        if selected_directory:
            entry_directory.delete(0, tk.END)  # Clear the current text in the entry
            entry_directory.insert(0, selected_directory)  # Insert the selected directory

    def toggle_manual_inputs():
        """Show or hide manual input fields based on the checkbox state."""
        if predefined_settings_var.get():
            # Hide manual input fields
            label_solver.grid_remove()
            entry_solver.grid_remove()
            label_time_step.grid_remove()
            entry_time_step.grid_remove()
            label_coder_format.grid_remove()
            entry_coder_format.grid_remove()
        else:
            # Show manual input fields
            label_solver.grid(row=5, column=0, padx=10, pady=5)
            entry_solver.grid(row=5, column=1, padx=10, pady=5)
            label_time_step.grid(row=6, column=0, padx=10, pady=5)
            entry_time_step.grid(row=6, column=1, padx=10, pady=5)
            label_coder_format.grid(row=7, column=0, padx=10, pady=5)
            entry_coder_format.grid(row=7, column=1, padx=10, pady=5)

    def create_swc():
        """Validate inputs, collect data, and pass them to the SWC creation function."""
        swc_name = entry_swc_name.get()
        directory = entry_directory.get()
        use_predefined = predefined_settings_var.get()  # Get the state of the checkbox

        if not swc_name:
            messagebox.showerror("Validation Error", "SWC name cannot be empty.")
            return
        if not directory:
            messagebox.showerror("Validation Error", "Please select a valid directory.")
            return

        # Get the number of subcomponents and units
        num_subcomponents = int(combo_subcomponents.get())
        num_units = int(combo_units.get())

        # Collect data based on the checkbox state
        if use_predefined:
            swc_data = {
                "SWC Name": swc_name,
                "Directory": directory,
                "Configuration": "Pre-defined"
            }
        else:
            # Validate manual inputs
            solver = entry_solver.get()
            time_step = entry_time_step.get()
            coder_format = entry_coder_format.get()

            if not solver or not time_step or not coder_format:
                messagebox.showerror("Validation Error", "All configuration fields must be filled.")
                return

            swc_data = {
                "SWC Name": swc_name,
                "Directory": directory,
                "Configuration": {
                    "solver": solver,
                    "time_step": time_step,
                    "coder_format": coder_format
                }
            }

        # Debugging: Print collected data (replace with actual SWC creation logic)
        print(f"Collected Data: {swc_data}")
        
        # Pass the data to the SWC creation function
        try:
            create_autosar_structure(swc_name, num_subcomponents, num_units, directory)
            messagebox.showinfo("Success", f"SWC '{swc_name}' created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while creating the SWC: {str(e)}")

    # Initialize the main window
    root = tk.Tk()
    root.title("SWC Generator")

    # SWC Name Input
    tk.Label(root, text="SWC Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_swc_name = tk.Entry(root)
    entry_swc_name.grid(row=0, column=1, padx=10, pady=5)

    # Directory Input
    tk.Label(root, text="Directory:").grid(row=1, column=0, padx=10, pady=5)
    entry_directory = tk.Entry(root)
    entry_directory.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=browse_directory).grid(row=1, column=2, padx=5, pady=5)

    # Pre-Defined Settings Checkbox
    predefined_settings_var = tk.BooleanVar()
    predefined_settings_var.set(False)  # Default is unchecked (manual mode)
    predefined_checkbox = tk.Checkbutton(
        root, 
        text="Use Pre-Defined Settings", 
        variable=predefined_settings_var,
        command=toggle_manual_inputs
    )
    predefined_checkbox.grid(row=2, column=0, columnspan=2, pady=5)

    # Number of Subcomponents Dropdown
    tk.Label(root, text="Number of Subcomponents:").grid(row=3, column=0, padx=10, pady=5)
    combo_subcomponents = ttk.Combobox(root, values=[1, 2, 3, 4, 5], state="readonly")
    combo_subcomponents.set(0)  # Default value
    combo_subcomponents.grid(row=3, column=1, padx=10, pady=5)

    # Number of Units Dropdown
    tk.Label(root, text="Number of Units (per Subcomponent):").grid(row=4, column=0, padx=10, pady=5)
    combo_units = ttk.Combobox(root, values=[1, 2, 3, 4, 5], state="readonly")
    combo_units.set(0)  # Default value
    combo_units.grid(row=4, column=1, padx=10, pady=5)

    # Manual Configuration Fields (Hidden by Default)
    label_solver = tk.Label(root, text="Solver:")
    entry_solver = tk.Entry(root)
    label_time_step = tk.Label(root, text="Time Step:")
    entry_time_step = tk.Entry(root)
    label_coder_format = tk.Label(root, text="Coder Format:")
    entry_coder_format = tk.Entry(root)

    # Create SWC Button
    tk.Button(root, text="Create SWC", command=create_swc).grid(row=8, column=0, columnspan=2, pady=10)

    toggle_manual_inputs()  # Ensure fields are shown/hidden based on default state
    root.mainloop()


if __name__ == "__main__":
    launch_gui()
