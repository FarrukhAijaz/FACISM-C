import tkinter as tk
from tkinter import filedialog, messagebox

def browse_directory(entry_widget):
    """Open a file explorer to select a directory and update the entry field."""
    selected_directory = filedialog.askdirectory(initialdir="~/Downloads", title="Select Directory")
    if selected_directory:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, selected_directory)

def toggle_manual_inputs(predefined_settings_var, widgets):
    """Show or hide manual input fields based on the checkbox state."""
    if predefined_settings_var.get():
        for widget in widgets:
            widget.grid_remove()
    else:
        for i, widget in enumerate(widgets):
            widget.grid(row=5 + i, column=0 if i % 2 == 0 else 1, padx=10, pady=5)

def update_dynamic_fields(combo_subcomponents, combo_units, dynamic_frame):
    """Dynamically add entry fields based on the number of subcomponents and units selected."""
    for widget in dynamic_frame.winfo_children():
        widget.destroy()

    num_subcomponents = int(combo_subcomponents.get())
    num_units = int(combo_units.get())

    subcomponent_entries = []
    unit_entries = {}

    for i in range(num_subcomponents):
        sub_label = tk.Label(dynamic_frame, text=f"Subcomponent {i + 1} Name:")
        sub_label.grid(row=i, column=0, padx=10, pady=5)

        sub_entry = tk.Entry(dynamic_frame)
        sub_entry.insert(0, f"Subcomponent_{i+1}")  # Default name
        sub_entry.grid(row=i, column=1, padx=10, pady=5)
        subcomponent_entries.append(sub_entry)

        unit_entries[i] = []
        for j in range(num_units):
            unit_label = tk.Label(dynamic_frame, text=f"Unit {i+1}-{j+1} Name:")
            unit_label.grid(row=i, column=2 + j * 2, padx=10, pady=5)

            unit_entry = tk.Entry(dynamic_frame)
            unit_entry.insert(0, f"Unit_{i+1}_{j+1}")  # Default name
            unit_entry.grid(row=i, column=3 + j * 2, padx=10, pady=5)
            unit_entries[i].append(unit_entry)

    return subcomponent_entries, unit_entries

def validate_inputs(swc_name, directory, subcomponent_entries, unit_entries):
    """Validate user inputs before creating an SWC."""
    if not swc_name:
        messagebox.showerror("Validation Error", "SWC name cannot be empty.")
        return None, None
    if not directory:
        messagebox.showerror("Validation Error", "Please select a valid directory.")
        return None, None

    subcomponent_names = [entry.get().strip() for entry in subcomponent_entries]
    if any(not name for name in subcomponent_names):
        messagebox.showerror("Validation Error", "Subcomponent names cannot be empty.")
        return None, None

    unit_names = {subcomponent_names[i]: [entry.get().strip() for entry in unit_list] for i, unit_list in unit_entries.items()}
    if any(any(not name for name in unit_list) for unit_list in unit_names.values()):
        messagebox.showerror("Validation Error", "Unit names cannot be empty.")
        return None, None

    return subcomponent_names, unit_names
