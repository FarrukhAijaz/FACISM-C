import tkinter as tk
from tkinter import filedialog
from GUI.dynamic_input import DynamicInputPage


class SWCSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="SWC Name:").grid(row=0, column=0, padx=10, pady=5)
        self.entry_swc_name = tk.Entry(self)
        self.entry_swc_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Directory:").grid(row=1, column=0, padx=10, pady=5)
        self.entry_directory = tk.Entry(self)
        self.entry_directory.grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self, text="Browse", command=self.browse_directory).grid(row=1, column=2)

        tk.Button(self, text="Next", command=lambda: controller.show_frame(DynamicInputPage)).grid(row=2, column=0, columnspan=2, pady=10)

    def browse_directory(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
            self.entry_directory.delete(0, tk.END)
            self.entry_directory.insert(0, selected_directory)
