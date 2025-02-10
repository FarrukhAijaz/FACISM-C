import tkinter as tk
from GUI.confirmation import ConfirmationPage

class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Configuration Settings").pack(pady=10)

        self.solver_var = tk.StringVar()
        tk.Label(self, text="Solver:").pack()
        tk.Entry(self, textvariable=self.solver_var).pack()

        self.time_step_var = tk.StringVar()
        tk.Label(self, text="Time Step:").pack()
        tk.Entry(self, textvariable=self.time_step_var).pack()

        self.coder_format_var = tk.StringVar()
        tk.Label(self, text="Coder Format:").pack()
        tk.Entry(self, textvariable=self.coder_format_var).pack()

        tk.Button(self, text="Next", command=lambda: controller.show_frame(ConfirmationPage)).pack(pady=10)
