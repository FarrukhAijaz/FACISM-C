import tkinter as tk
from tkinter import Frame, Canvas, filedialog
from PIL import Image, ImageTk
from GUI.swc_setup import SWCSetupPage
from GUI.swc_setup import DynamicInputPage
from GUI.helper import blur_image
from GUI.helper import create_rounded_rectangle


class IntroPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=600)

        self.bg_image = Image.open("/home/saijaz/Desktop/GAMA/GAMA/assets/images/bg.png")
        self.bg_image = self.bg_image.resize((800, 600), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(blur_image(self.bg_image, 10))

        self.canvas = Canvas(self, width=800, height=600, bg="white", bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        label_text = "Welcome to SMG-F1 (Simulink Model Generator - Ford v1.0)"
        label_font = ("Times New Roman", 14, "bold italic")
        self.canvas.create_text(240, 20, text=label_text, font=label_font, fill="#000FFF", anchor="center")

        label_text = "This application is an automation tool for creating Simulink Models for Software Components, feel free to use it and share any comments!"
        label_font = ("Times New Roman", 10, "italic")
        self.canvas.create_text(385, 40, text=label_text, font=label_font, fill="#0036FF")

        label_text = "Please Select one of the following:"
        label_font = ("Times New Roman", 12, "bold italic")
        self.canvas.create_text(150, 100, text=label_text, font=label_font, fill="#17202A")

        self.var = tk.IntVar()

        self.var = tk.IntVar(value=0)

        label_text = "I want to generate the software component in Simulink using an ARXML import."
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(345, 157, text=label_text, font=label_font, fill="#17202A")

        self.circle1 = self.canvas.create_oval(45, 150, 60, 165, fill="#CCD1D1", outline="#0036FF", width=2)
        self.canvas.tag_bind(self.circle1, "<Button-1>", lambda event: toggle_radio_button(1))

        self.inner_circle1 = self.canvas.create_oval(48, 153, 57, 162, fill="#28B463", outline="", state="hidden")

        self.canvas.create_oval(48, 153, 57, 162, fill="green", outline="", state="hidden", tags="inner1")

        label_text = "I want to generate the software component in Simulink by manually defining software components/units."
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(422, 207, text=label_text, font=label_font, fill="#17202A")

        self.circle2 = self.canvas.create_oval(45, 200, 60, 215, fill="#CCD1D1", outline="#0036FF", width=2)
        self.canvas.tag_bind(self.circle2, "<Button-1>", lambda event: toggle_radio_button(2))

        self.inner_circle2 = self.canvas.create_oval(48, 203, 57, 212, fill="#28B463", outline="", state="hidden")

        self.canvas.create_oval(48, 203, 57, 212, fill="green", outline="", state="hidden", tags="inner2")

        def toggle_radio_button(selected_value):
            self.var.set(selected_value)

            self.canvas.itemconfig(self.inner_circle1, state="normal" if self.var.get() == 1 else "hidden")
            self.canvas.itemconfig(self.inner_circle2, state="normal" if self.var.get() == 2 else "hidden")

            y_offset = 50 if self.var.get() == 1 else 0

            if self.var.get() == 1:
                show_file_dialogs()
            else:
                hide_file_dialogs()

        self.file_dialog_label1 = self.canvas.create_text(400, 250, text="Select File 1", font=("Arial", 10), fill="blue", state="hidden")
        self.file_dialog_label2 = self.canvas.create_text(400, 280, text="Select File 2", font=("Arial", 10), fill="blue", state="hidden")

        self.file1_path = None
        self.file2_path = None

        def show_file_dialogs():
            self.canvas.itemconfig(self.file_dialog_label1, state="normal")
            self.canvas.itemconfig(self.file_dialog_label2, state="normal")

            self.file1_path = filedialog.askopenfilename(title="Select File 1")
            self.file2_path = filedialog.askopenfilename(title="Select File 2")

            if self.file1_path and self.file2_path:
                print(f"File 1 selected: {self.file1_path}")
                print(f"File 2 selected: {self.file2_path}")

        def hide_file_dialogs():
            self.canvas.itemconfig(self.file_dialog_label1, state="hidden")
            self.canvas.itemconfig(self.file_dialog_label2, state="hidden")
            self.file1_path = None
            self.file2_path = None

        def navigate_next(event=None):
            try:
                if self.var.get() == 0:
                    raise ValueError("Please select an option before proceeding.")
                
                if self.var.get() == 1 and (not self.file1_path or not self.file2_path):
                    raise ValueError("Please select both files before proceeding.")
                
                if self.var.get() == 1:
                    self.controller.show_frame(SWCSetupPage, self.file1_path, self.file2_path)
                elif self.var.get() == 2:
                    self.controller.show_frame(DynamicInputPage)

            except ValueError as e:
                error_message = str(e)
                
                if hasattr(self, 'error_text_id'):
                    self.canvas.delete(self.error_text_id)
                
                self.error_text_id = self.canvas.create_text(400, 550, text=error_message, font=("Arial", 12, "bold"), fill="red", anchor="center")
            
            if self.var.get() != 0:
                if hasattr(self, 'error_text_id'):
                    self.canvas.delete(self.error_text_id)

        def on_hover(event):
            self.canvas.itemconfig(self.start_button, fill="#A3E4D7")

        def on_leave(event):
            self.canvas.itemconfig(self.start_button, fill="#F0B27A")

        self.start_button = create_rounded_rectangle(self.canvas, 650, 550, 730, 580, radius=15, fill="#F0B27A", outline="", width=2)

        self.start_button_text = self.canvas.create_text(685, 565, text="Next", font=("Times New Roman", 14, "bold italic"), fill="#17202A")

        self.canvas.tag_bind(self.start_button, "<Button-1>", navigate_next)
        self.canvas.tag_bind(self.start_button_text, "<Button-1>", navigate_next)
        self.canvas.tag_bind(self.start_button, "<Enter>", on_hover)
        self.canvas.tag_bind(self.start_button_text, "<Enter>", on_hover)
        self.canvas.tag_bind(self.start_button, "<Leave>", on_leave)
        self.canvas.tag_bind(self.start_button_text, "<Leave>", on_leave)
