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
        self.bg_photo = ImageTk.PhotoImage(blur_image(self.bg_image, 1))

        self.canvas = Canvas(self, width=800, height=600, bg="white", bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        self.canvas.create_image(400, 0, image=self.bg_photo, anchor="nw")

        label_text = "Welcome to SMG-F1"
        label_font = ("Times New Roman", 14, "bold italic")
        self.canvas.create_text(90, 20, text=label_text, font=label_font, fill="#000FFF", anchor="center")
        
        label_text = "(Simulink Model Generator - Ford v1.0)"
        label_font = ("Times New Roman", 14, "bold italic")
        self.canvas.create_text(160, 40, text=label_text, font=label_font, fill="#000FFF", anchor="center")

        label_text = "This application is an automation tool for creating Simulink Models"
        label_font = ("Times New Roman", 10, "italic")
        self.canvas.create_text(200, 60, text=label_text, font=label_font, fill="#0036FF")

        label_text = "for Software Components, feel free to use it and share any comments!"
        label_font = ("Times New Roman", 10, "italic")
        self.canvas.create_text(200, 75, text=label_text, font=label_font, fill="#0036FF")

        label_text = "Please Select one of the following:"
        label_font = ("Times New Roman", 12, "bold italic")
        self.canvas.create_text(125, 125, text=label_text, font=label_font, fill="#17202A")

        self.var = tk.IntVar(value=0)
        
        # Button 1 Starts
        label_text = "Generate Software Component in Simulink"
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(190, 167, text=label_text, font=label_font, fill="#17202A")

        label_text = "using an ARXML import."
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(133, 187, text=label_text, font=label_font, fill="#17202A")

        self.circle1 = self.canvas.create_oval(20, 160, 35, 175, fill="#CCD1D1", outline="#0036FF", width=2)
        self.canvas.tag_bind(self.circle1, "<Button-1>", lambda event: toggle_radio_button(1))

        self.inner_circle1 = self.canvas.create_oval(23, 163, 32, 172, fill="#28B463", outline="", state="hidden")

        self.canvas.create_oval(23, 163, 32, 172, fill="green", outline="", state="hidden", tags="inner1")

        # Button 2 Starts
        label_text = "Generate Software Component in Simulink by"
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(200, 227, text=label_text, font=label_font, fill="#17202A")

        label_text = "manually defining software components/units."
        label_font = ("Times New Roman", 12, "bold")
        self.canvas.create_text(200, 247, text=label_text, font=label_font, fill="#17202A")

        self.circle2 = self.canvas.create_oval(20, 220, 35, 235, fill="#CCD1D1", outline="#0036FF", width=2)
        self.canvas.tag_bind(self.circle2, "<Button-1>", lambda event: toggle_radio_button(2))

        self.inner_circle2 = self.canvas.create_oval(23, 223, 32, 232, fill="#28B463", outline="", state="hidden")

        self.canvas.create_oval(23, 223, 32, 232, fill="green", outline="", state="hidden", tags="inner2")

        def toggle_radio_button(selected_value):
            self.var.set(selected_value)

            self.canvas.itemconfig(self.inner_circle1, state="normal" if self.var.get() == 1 else "hidden")
            self.canvas.itemconfig(self.inner_circle2, state="normal" if self.var.get() == 2 else "hidden")

            if self.var.get() == 1:
                print("I'm here")
                DisplayRadioButton1();

            elif self.var.get() == 2:
                print("I'm there")
                DisplayRadioButton2();


        def DisplayRadioButton1():
            # Labels for text boxes
            print("I'm now here")
            label_font = ("Times New Roman", 12, "bold")
            canvas_id1 = self.canvas.create_text(200, 270, text="Select Save Location:", font=label_font, fill="#17202A")
            canvas_id2 = self.canvas.create_text(200, 340, text="Select ARXML File:", font=label_font, fill="#17202A")

            # Rectangular boxes
            rect1 = create_rounded_rectangle(self.canvas, 350, 255, 600, 285, radius=5, fill="white", outline="black")
            rect2 = create_rounded_rectangle(self.canvas, 350, 325, 600, 355, radius=5, fill="white", outline="black")

            # Text inside boxes
            text1_id = self.canvas.create_text(475, 270, text="Click to select folder", font=("Arial", 10), fill="grey")
            text2_id = self.canvas.create_text(475, 340, text="Click to select ARXML file", font=("Arial", 10), fill="grey")

            # Function to open directory dialog and update text
            def select_directory(event, text_id):
                folder_selected = filedialog.askdirectory(title="Select Folder")
                if folder_selected:
                    self.canvas.itemconfig(text_id, text=folder_selected, fill="black")

            # Bind clicks to open dialogs
            self.canvas.tag_bind(rect1, "<Button-1>", lambda event: select_directory(event, text1_id))
            self.canvas.tag_bind(text1_id, "<Button-1>", lambda event: select_directory(event, text1_id))

            self.canvas.tag_bind(rect2, "<Button-1>", lambda event: select_directory(event, text2_id))
            self.canvas.tag_bind(text2_id, "<Button-1>", lambda event: select_directory(event, text2_id))


        def DisplayRadioButton2():
            return 1

        # Navigation functionality
        def navigate_next(event=None):
            try:
                if self.var.get() == 0:
                    raise ValueError("Please select an option before proceeding.")
                
                if self.var.get() == 1:
                    self.controller.show_frame(SWCSetupPage)
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

        # Hover effects for the 'Next' button
        def on_hover(event):
            self.canvas.itemconfig(self.start_button, fill="#A3E4D7")

        def on_leave(event):
            self.canvas.itemconfig(self.start_button, fill="#F0B27A")

        # Next button
        self.start_button = create_rounded_rectangle(self.canvas, 300, 550, 380, 580, radius=15, fill="#F0B27A", outline="", width=2)
        self.start_button_text = self.canvas.create_text(335, 565, text="Next", font=("Times New Roman", 14, "bold italic"), fill="#17202A")

        self.canvas.tag_bind(self.start_button, "<Button-1>", navigate_next)
        self.canvas.tag_bind(self.start_button_text, "<Button-1>", navigate_next)
        self.canvas.tag_bind(self.start_button, "<Enter>", on_hover)
        self.canvas.tag_bind(self.start_button_text, "<Enter>", on_hover)
        self.canvas.tag_bind(self.start_button, "<Leave>", on_leave)
        self.canvas.tag_bind(self.start_button_text, "<Leave>", on_leave)
