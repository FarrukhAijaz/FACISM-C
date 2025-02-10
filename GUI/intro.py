import tkinter as tk
from tkinter import Frame, Canvas
from PIL import Image, ImageTk  # Import for handling images
from GUI.swc_setup import SWCSetupPage  # Import next page
from GUI.helper import blur_image

class IntroPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=600)

        # Load and display the background image
        self.bg_image = Image.open("/home/saijaz/Desktop/GAMA/GAMA/assets/images/bg.png")  # Replace with your image path
        self.bg_image = self.bg_image.resize((800, 600), Image.ANTIALIAS)  # Resize to fit the frame
        self.bg_photo = ImageTk.PhotoImage(blur_image(self.bg_image, 3))

        # Canvas for drawing image and text
        self.canvas = Canvas(self, width=800, height=600, bg="white", bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)

        # Add background image to canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Title with transparent background
        label_text = "Welcome to SMG-F1 (Simulink Model Generator - Ford v1.0)"
        label_font = ("Times New Roman", 10, "bold italic")  # Use Times New Roman, with size 20 and bold
        self.canvas.create_text(400, 100, text=label_text, font=label_font, fill="black")  # Position intro text at the top center

        # Subtitle with transparent background
        label_text = "This application is an automation tool for creating Simulink Models for Software Components, feel free to use it and share any comments!"
        label_font = ("Times New Roman", 8, "italic")  # Use Times New Roman, with size 12
        self.canvas.create_text(400, 300, text=label_text, font=label_font, fill="black")  # Position intro text at the top center


        # Start Button
        start_button = tk.Button(self, text="Next", font=("Roboto", 10), command=lambda: controller.show_frame(SWCSetupPage))
        start_button.place(x=650, y=550, width=80, height=30)

