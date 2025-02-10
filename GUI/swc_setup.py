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

    # def navigate_next():
    #         if self.var.get() == 1:
    #             self.controller.show_frame(SWCSetupPage)
    #         elif self.var.get() == 2:
    #             self.controller.show_frame(DynamicInputPage)  # Assuming this is the correct class name

    # # Function to go back to the previous page (e.g., WelcomePage)
    # def navigate_previous():
    #     self.controller.show_frame(WelcomePage)  # Replace with the actual previous page class

    # # Start Button (Next)
    # start_button = tk.Button(self, text="Next", font=("Roboto", 10), command=navigate_next)
    # start_button.place(x=650, y=550, width=80, height=30)

    # # Previous Button
    # prev_button = tk.Button(self, text="Previous", font=("Roboto", 10), command=navigate_previous)
    # prev_button.place(x=550, y=550, width=80, height=30)  # Placed to the left of the Next button

