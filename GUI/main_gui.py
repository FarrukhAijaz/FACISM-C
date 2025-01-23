# gui/main_gui.py
import tkinter as tk
from tkinter import messagebox
from swc.swc_creator import create_new_swc
from gui.validation import validate_inputs

def generate_swc():
    swc_name = entry_swc_name.get()
    directory = entry_directory.get()

    if validate_inputs(swc_name, directory):
        try:
            create_new_swc(swc_name, directory)
            messagebox.showinfo("Success", f"SWC '{swc_name}' created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create SWC: {e}")

def launch_gui():
    global entry_swc_name, entry_directory
    root = tk.Tk()
    root.title("SWC Generator")

    tk.Label(root, text="SWC Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_swc_name = tk.Entry(root)
    entry_swc_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Directory:").grid(row=1, column=0, padx=10, pady=5)
    entry_directory = tk.Entry(root)
    entry_directory.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(root, text="Generate SWC", command=generate_swc).grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()