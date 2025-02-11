import tkinter as tk
from tkinter import Canvas, Entry, Label, OptionMenu, StringVar
from PIL import Image, ImageTk
from GUI.helper import blur_image
from GUI.helper import create_rounded_rectangle

class SWCSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(width=800, height=600)
        def InitaliseFrame():
            self.bg_image = Image.open("/home/saijaz/Desktop/GAMA/GAMA/assets/images/bg.png")
            self.bg_image = self.bg_image.resize((800, 600), Image.ANTIALIAS)
            self.bg_photo = ImageTk.PhotoImage(blur_image(self.bg_image, 1))

            self.canvas = Canvas(self, width=800, height=600, bg="white", bd=0, highlightthickness=0)
            self.canvas.place(x=0, y=0)

            self.canvas.create_image(400, 0, image=self.bg_photo, anchor="nw")

            label_text = "Welcome to Generation of Software Components"
            label_font = ("Times New Roman", 14, "bold italic")
            self.canvas.create_text(198, 20, text=label_text, font=label_font, fill="#000FFF", anchor="center")

            label_text = "This tool works with all supported Matlab versions"
            label_font = ("Times New Roman", 10, "italic")
            self.canvas.create_text(150, 40, text=label_text, font=label_font, fill="#0036FF")

            label_text = "Please fill in the following:"
            label_font = ("Times New Roman", 12, "bold italic")
            self.canvas.create_text(100, 80, text=label_text, font=label_font, fill="#17202A")

        self.var = tk.IntVar(value=0)
        # Button 1 Starts
        def InitialiseRadioButtonSet1():
            Yes_BASE_X = 258
            YN_OFFSET = 100
            y_line = 508
            x1 = 220
            y1 = 500
            YN_OFFSET_Button = 100
            
            label_text = "Yes"
            label_font = ("Times New Roman", 14, "bold")
            self.canvas.create_text(Yes_BASE_X, y_line, text=label_text, font=label_font, fill="#17202A")


            self.circle1 = self.canvas.create_oval(x1, y1, x1 + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle1, "<Button-1>", lambda event: toggle_radio_button(1))

            self.inner_circle1 = self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner1")

            label_text = "No"
            label_font = ("Times New Roman", 14, "bold")
            self.canvas.create_text(Yes_BASE_X + YN_OFFSET, y_line, text=label_text, font=label_font, fill="#17202A")


            self.circle3 = self.canvas.create_oval(x1 + YN_OFFSET_Button, y1, x1 + YN_OFFSET_Button + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle3, "<Button-1>", lambda event: toggle_radio_button(3))

            self.inner_circle3 = self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner3")
        # Button 2 Starts
        def InitialiseRadioButtonSet2():
            Yes_BASE_X = 258
            YN_OFFSET = 100
            y_line = 558
            x1 = 220
            y1 = 550
            YN_OFFSET_Button = 100
            label_text = "Yes"
            label_font = ("Times New Roman", 14, "bold")
            self.canvas.create_text(Yes_BASE_X, y_line, text=label_text, font=label_font, fill="#17202A")

            self.circle2 = self.canvas.create_oval(x1, y1, x1 + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle2, "<Button-1>", lambda event: toggle_radio_button(2))

            self.inner_circle2 = self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner2")

            label_text = "No"
            label_font = ("Times New Roman", 14, "bold")
            self.canvas.create_text(Yes_BASE_X + YN_OFFSET, y_line, text=label_text, font=label_font, fill="#17202A")

            self.circle4 = self.canvas.create_oval(x1 + YN_OFFSET_Button, y1, x1 + YN_OFFSET_Button + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle4, "<Button-1>", lambda event: toggle_radio_button(4))

            self.inner_circle4 = self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner4")


        def toggle_radio_button(selected_value):
            self.var.set(selected_value)

            self.canvas.itemconfig(self.inner_circle1, state="normal" if self.var.get() == 1 else "hidden")
            self.canvas.itemconfig(self.inner_circle2, state="normal" if self.var.get() == 2 else "hidden")
            self.canvas.itemconfig(self.inner_circle3, state="normal" if self.var.get() == 3 else "hidden")
            self.canvas.itemconfig(self.inner_circle4, state="normal" if self.var.get() == 4 else "hidden")

            if self.var.get() == 1:
                print("1")
            elif self.var.get() == 2:
                print("2")
            elif self.var.get() == 3:
                print("3")
            elif self.var.get() == 4:
                print("4")
        
        def create_swc_name_input():
            self.canvas.create_text(100, 120, text="Enter Software Component Name:", font=("Times New Roman", 12, "bold"), fill="#17202A", anchor="w")
            create_rounded_rectangle(self.canvas, 200, 110, 400, 140, radius=10, fill="white", outline="black")

            self.swc_name_entry = Entry(self, font=("Times New Roman", 12), bd=0, bg="white")
            self.canvas.create_window(300, 125, window=self.swc_name_entry, width=180, height=20)
            return self.swc_name_entry

        def create_subcomponents_question():
            self.canvas.create_text(100, 160, text="Does the SWC have subcomponents?", font=("Times New Roman", 12, "bold"), fill="#17202A", anchor="w")

            self.subcomponent_var = StringVar(value="Select")
            options = ["No", "Yes"]
            create_rounded_rectangle(self.canvas, 350, 150, 430, 180, radius=10, fill="white", outline="black")

            self.subcomponent_dropdown = OptionMenu(self, self.subcomponent_var, *options, command=self.toggle_subcomponent_dropdown)
            self.subcomponent_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.canvas.create_window(390, 165, window=self.subcomponent_dropdown, width=70, height=20)

            # Subcomponent Count Dropdown
            self.subcomponent_count_var = StringVar(value="0")
            create_rounded_rectangle(self.canvas, 450, 150, 510, 180, radius=10, fill="white", outline="black")
            self.subcomponent_count_dropdown = OptionMenu(self, self.subcomponent_count_var, *[str(i) for i in range(1, 11)])
            self.subcomponent_count_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.subcomponent_count_dropdown_id = self.canvas.create_window(480, 165, window=self.subcomponent_count_dropdown, width=50, height=20)
            self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="hidden")  # Hide initially
        
        def create_units_question():
            self.canvas.create_text(100, 200, text="Does the SWC have units?", font=("Times New Roman", 12, "bold"), fill="#17202A", anchor="w")

            self.units_var = StringVar(value="No")
            options = ["No", "Yes"]
            create_rounded_rectangle(self.canvas, 350, 190, 430, 220, radius=10, fill="white", outline="black")

            self.units_dropdown = OptionMenu(self, self.units_var, *options, command=self.toggle_units_dropdown)
            self.units_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.canvas.create_window(390, 205, window=self.units_dropdown, width=70, height=20)

            # Units Count Dropdown
            self.units_count_var = StringVar(value="1")
            create_rounded_rectangle(self.canvas, 450, 190, 510, 220, radius=10, fill="white", outline="black")
            self.units_count_dropdown = OptionMenu(self, self.units_count_var, *[str(i) for i in range(1, 11)])
            self.units_count_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.units_count_dropdown_id = self.canvas.create_window(480, 205, window=self.units_count_dropdown, width=50, height=20)
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="hidden")  # Hide initially



        # Execute the functions

        InitaliseFrame()
        InitialiseRadioButtonSet1()
        InitialiseRadioButtonSet2()
        create_swc_name_input()
        create_subcomponents_question()
        create_units_question()

    def toggle_subcomponent_dropdown(self, value):
            if value == "Yes":
                self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="normal")  # Show
            else:
                self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="hidden")  # Hide
    
    def toggle_units_dropdown(self, value):
        if value == "Yes":
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="normal")  # Show
        else:
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="hidden")  # Hide
