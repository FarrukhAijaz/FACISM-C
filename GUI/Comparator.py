import tkinter as tk
from tkinter import ttk, messagebox
from SWC.swc_creator import create_autosar_structure
from helper import browse_directory, toggle_manual_inputs, update_dynamic_fields, validate_inputs

def launch_gui():
    root = tk.Tk()
    root.title("SWC Generator")

    tk.Label(root, text="SWC Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_swc_name = tk.Entry(root)
    entry_swc_name.grid(row=0, column=1, padx=10, pady=5)
    entry_swc_name.insert(0, "SWC_LLC_Lat")

    tk.Label(root, text="Directory:").grid(row=1, column=0, padx=10, pady=5)
    entry_directory = tk.Entry(root)
    entry_directory.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Browse", command=lambda: browse_directory(entry_directory)).grid(row=1, column=2, padx=5, pady=5)

    predefined_settings_var = tk.BooleanVar()
    predefined_checkbox = tk.Checkbutton(root, text="Use Pre-Defined Settings", variable=predefined_settings_var)
    predefined_checkbox.grid(row=2, column=0, columnspan=2, pady=5)

    tk.Label(root, text="Number of Subcomponents:").grid(row=3, column=0, padx=10, pady=5)
    combo_subcomponents = ttk.Combobox(root, values=[1, 2, 3, 4, 5], state="readonly")
    combo_subcomponents.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(root, text="Number of Units (per Subcomponent):").grid(row=4, column=0, padx=10, pady=5)
    combo_units = ttk.Combobox(root, values=[1, 2, 3, 4, 5], state="readonly")
    combo_units.grid(row=4, column=1, padx=10, pady=5)

    label_solver, entry_solver = tk.Label(root, text="Solver:"), tk.Entry(root)
    label_time_step, entry_time_step = tk.Label(root, text="Time Step:"), tk.Entry(root)
    label_coder_format, entry_coder_format = tk.Label(root, text="Coder Format:"), tk.Entry(root)

    manual_fields = [label_solver, entry_solver, label_time_step, entry_time_step, label_coder_format, entry_coder_format]
    toggle_manual_inputs(predefined_settings_var, manual_fields)

    dynamic_frame = tk.Frame(root)
    dynamic_frame.grid(row=5, column=0, columnspan=3, pady=10)

    subcomponent_entries, unit_entries = [], {}

    def on_update_fields():
        nonlocal subcomponent_entries, unit_entries
        subcomponent_entries, unit_entries = update_dynamic_fields(combo_subcomponents, combo_units, dynamic_frame)

    combo_subcomponents.bind("<<ComboboxSelected>>", lambda e: on_update_fields())
    combo_units.bind("<<ComboboxSelected>>", lambda e: on_update_fields())

    def create_swc():
        swc_name = entry_swc_name.get()
        directory = entry_directory.get()
        subcomponent_names, unit_names = validate_inputs(swc_name, directory, subcomponent_entries, unit_entries)
        if subcomponent_names is None:
            return
        
        create_autosar_structure(swc_name, len(subcomponent_names), len(unit_names[subcomponent_names[0]]), directory)
        messagebox.showinfo("Success", f"SWC '{swc_name}' created successfully!")

    tk.Button(root, text="Create SWC", command=create_swc).grid(row=8, column=0, columnspan=2, pady=10)
    root.mainloop()

launch_gui()
