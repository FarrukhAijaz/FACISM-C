import tkinter as tk
from tkinter import messagebox
from SWC.swc_creator import create_autosar_structure


class ConfirmationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Review Your Inputs").pack(pady=10)
        self.review_label = tk.Label(self, text="", wraplength=400)
        self.review_label.pack()

        tk.Button(self, text="Create SWC", command=self.create_swc).pack(pady=10)

    def update_review(self, swc_name, directory):
        self.review_label.config(text=f"SWC Name: {swc_name}\nDirectory: {directory}")

    def create_swc(self):
        try:
            create_autosar_structure("SampleSWC", 2, 3, "/tmp")
            messagebox.showinfo("Success", "SWC Created Successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create SWC: {str(e)}")
