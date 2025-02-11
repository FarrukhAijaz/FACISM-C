import tkinter as tk
from tkinter import Canvas, Entry, OptionMenu, StringVar, messagebox
from PIL import Image, ImageTk
from GUI.helper import blur_image
from GUI.helper import create_rounded_rectangle
from GUI.dynamic_input import DynamicInputPage

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

        self.var1 = tk.IntVar(value=0)
        self.var2 = tk.IntVar(value=0)
        # Button 1 Starts

        def InitialiseRadioButtonSet1():
            Yes_BASE_X = 258
            YN_OFFSET = 100
            y_line = 390
            x1 = 220
            y1 = 382
            YN_OFFSET_Button = 100
            
            label_text = "Yes"
            label_font = ("Times New Roman", 14)
            self.canvas.create_text(Yes_BASE_X, y_line, text=label_text, font=label_font, fill="#17202A")


            self.circle1 = self.canvas.create_oval(x1, y1, x1 + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle1, "<Button-1>", lambda event: toggle_radio_button(1))

            self.inner_circle1 = self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner1")

            label_text = "No"
            label_font = ("Times New Roman", 14)
            self.canvas.create_text(Yes_BASE_X + YN_OFFSET, y_line, text=label_text, font=label_font, fill="#17202A")


            self.circle2 = self.canvas.create_oval(x1 + YN_OFFSET_Button, y1, x1 + YN_OFFSET_Button + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle2, "<Button-1>", lambda event: toggle_radio_button(2))

            self.inner_circle2 = self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner3")
        
        # Button 2 Starts

        def InitialiseRadioButtonSet2():
            Yes_BASE_X = 258
            YN_OFFSET = 100
            y_line = 450
            x1 = 220
            y1 = y_line - 8
            YN_OFFSET_Button = 100
            label_text = "Yes"
            label_font = ("Times New Roman", 14)
            self.canvas.create_text(Yes_BASE_X, y_line, text=label_text, font=label_font, fill="#17202A")

            self.circle3 = self.canvas.create_oval(x1, y1, x1 + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle3, "<Button-1>", lambda event: toggle_radio_button(3))

            self.inner_circle3 = self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + 3, y1 + 3, x1 + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner2")

            label_text = "No"
            label_font = ("Times New Roman", 14)
            self.canvas.create_text(Yes_BASE_X + YN_OFFSET, y_line, text=label_text, font=label_font, fill="#17202A")

            self.circle4 = self.canvas.create_oval(x1 + YN_OFFSET_Button, y1, x1 + YN_OFFSET_Button + 15, y1 + 15, fill="#CCD1D1", outline="#0036FF", width=2)
            self.canvas.tag_bind(self.circle4, "<Button-1>", lambda event: toggle_radio_button(4))

            self.inner_circle4 = self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="#28B463", outline="", state="hidden")

            self.canvas.create_oval(x1 + YN_OFFSET_Button + 3, y1 + 3, x1 + YN_OFFSET_Button + 12, y1 + 12, fill="green", outline="", state="hidden", tags="inner4")


        def toggle_radio_button(selected_value):
            if selected_value <= 2 :
                self.var1.set(selected_value)

            else: self.var2.set(selected_value)

            self.canvas.itemconfig(self.inner_circle1, state="normal" if self.var1.get() == 1 else "hidden")
            self.canvas.itemconfig(self.inner_circle2, state="normal" if self.var1.get() == 2 else "hidden")
            self.canvas.itemconfig(self.inner_circle3, state="normal" if self.var2.get() == 3 else "hidden")
            self.canvas.itemconfig(self.inner_circle4, state="normal" if self.var2.get() == 4 else "hidden")

            if self.var1.get() == 1:
                print("1")
            elif self.var1.get() == 2:
                print("2")
            if self.var2.get() == 3:
                print("3")
            elif self.var2.get() == 4:
                print("4")
        
        def create_swc_name_input():
            self.canvas.create_text(20, 120, text="Name of Software Component:", font=("Times New Roman", 12), fill="#17202A", anchor="w")
            create_rounded_rectangle(self.canvas, 90, 140, 390, 170, radius=10, fill="white", outline="black")

            self.swc_name_entry = Entry(self, font=("Times New Roman", 12), bd=0, bg="white")
            self.canvas.create_window(240, 155, window=self.swc_name_entry, width=302, height=32)

        def create_subcomponents_question():
            self.canvas.create_text(20, 185, text="Does the Software Component have subcomponents?", font=("Times New Roman", 12), fill="#17202A", anchor="w")

            self.subcomponent_var = StringVar(value="Select")
            options = ["No", "Yes"]
            create_rounded_rectangle(self.canvas, 20, 210, 100, 240, radius=10, fill="white", outline="black")

            self.subcomponent_dropdown = OptionMenu(self, self.subcomponent_var, *options, command=self.toggle_subcomponent_dropdown)
            self.subcomponent_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.canvas.create_window(60, 225, window=self.subcomponent_dropdown, width=70, height=20)

            # Subcomponent Count Dropdown
            self.rect1 = create_rounded_rectangle(self.canvas, 120, 210, 280, 240, radius=10, fill="white", outline="black", state = "hidden")
            self.subcomponent_count_var = StringVar(value="Select a number")
            self.subcomponent_count_dropdown = OptionMenu(self, self.subcomponent_count_var, *[str(i) for i in range(0, 6)])
            self.subcomponent_count_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.subcomponent_count_dropdown_id = self.canvas.create_window(200, 225, window=self.subcomponent_count_dropdown, width=150, height=20)
            self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="hidden")  # Hide initially
        
        def create_units_question():
            self.canvas.create_text(20, 265, text="Does the Software Component have units?", font=("Times New Roman", 12), fill="#17202A", anchor="w")

            self.units_var = StringVar(value="Select")
            options = ["No", "Yes"]
            create_rounded_rectangle(self.canvas, 20, 290, 100, 320, radius=10, fill="white", outline="black")

            self.units_dropdown = OptionMenu(self, self.units_var, *options, command=self.toggle_units_dropdown)
            self.units_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.canvas.create_window(60, 305, window=self.units_dropdown, width=70, height=20)

            # Units Count Dropdown
            self.units_count_var = StringVar(value="Select a number")
            self.rect2 = create_rounded_rectangle(self.canvas, 120, 290, 280, 320, radius=10, fill="white", outline="black", state = "hidden")
            self.units_count_dropdown = OptionMenu(self, self.units_count_var, *[str(i) for i in range(0, 6)])
            self.units_count_dropdown.config(bg="white", bd=0, highlightthickness=0)
            self.units_count_dropdown_id = self.canvas.create_window(200, 305, window=self.units_count_dropdown, width=150, height=20)
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="hidden")  # Hide initially



        def Question1():
            label_text = "Do you want to include I/O ports for subcomponents"
            label_font = ("Times New Roman", 12)
            self.canvas.create_text(187, 350, text=label_text, font=label_font, fill="#17202A", anchor="center")
            
            label_text = "or units ?"
            label_font = ("Times New Roman", 12)
            self.canvas.create_text(50, 370, text=label_text, font=label_font, fill="#17202A", anchor="center")
        
        
        def Question2():
            label_text = "Do you want to name those I/O ports ?"
            label_font = ("Times New Roman", 12)
            self.canvas.create_text(145, 420, text=label_text, font=label_font, fill="#17202A", anchor="center")
    
        def navigate_next(event=None):
            try:
                selected_option1 = self.var1.get()
                selected_option2 = self.var2.get()

                swc_name = self.swc_name_entry.get().strip()
                if not swc_name:
                    raise ValueError ("Please enter a valid name for the Software Component")
                
                if self.subcomponent_var.get() == "Select" or self.units_var.get() == "Select":
                    raise ValueError("Please Enter a Valid answer in the Select Box")
                
                if self.subcomponent_var.get() == "Yes" and self.subcomponent_count_var.get() == "Select a number":
                    raise ValueError("Please select a valid number of subcomponents before proceeding.")
                
                if self.units_var.get() == "Yes" and self.units_count_var.get() == "Select a number":
                    raise ValueError("Please select a valid number of units before proceeding.")
                
                if selected_option1 not in [1, 2] and selected_option2 not in [3, 4]:
                    raise ValueError("Please select both Yes/No options before proceeding.")
                
                # Proceed to the respective page
                self.controller.show_frame(DynamicInputPage)

            except ValueError as e:
                messagebox.showerror("Input Error", str(e))  # Show error pop-up

        # Hover effects for the 'Next' button
        def on_hover(event):
            self.canvas.itemconfig(self.start_button, fill="#A3E4D7")

        def on_leave(event):
            self.canvas.itemconfig(self.start_button, fill="#F0B27A")

        # Next button definition
        def NextButton():
            self.start_button = create_rounded_rectangle(self.canvas, 300, 550, 380, 580, radius=15, fill="#F0B27A", outline="", width=2)
            self.start_button_text = self.canvas.create_text(335, 565, text="Next", font=("Times New Roman", 14, "bold italic"), fill="#17202A")

            self.canvas.tag_bind(self.start_button, "<Button-1>", navigate_next)
            self.canvas.tag_bind(self.start_button_text, "<Button-1>", navigate_next)
            self.canvas.tag_bind(self.start_button, "<Enter>", on_hover)
            self.canvas.tag_bind(self.start_button_text, "<Enter>", on_hover)
            self.canvas.tag_bind(self.start_button, "<Leave>", on_leave)
            self.canvas.tag_bind(self.start_button_text, "<Leave>", on_leave)
        # Execute the functions

        InitaliseFrame()
        InitialiseRadioButtonSet1()
        InitialiseRadioButtonSet2()
        create_swc_name_input()
        create_subcomponents_question()
        create_units_question()
        Question1()
        Question2()
        NextButton()

    def toggle_subcomponent_dropdown(self, value):
            
            if value == "Yes":
                self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="normal")  # Show
                self.canvas.itemconfigure(self.rect1, state = "normal")
            else:
                self.canvas.itemconfigure(self.subcomponent_count_dropdown_id, state="hidden")  # Hide
                self.canvas.itemconfigure(self.rect1, state = "hidden")
    
    def toggle_units_dropdown(self, value):
        if value == "Yes":
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="normal")  # Show
            self.canvas.itemconfigure(self.rect2, state = "normal")
        else:
            self.canvas.itemconfigure(self.units_count_dropdown_id, state="hidden")  # Hide
            self.canvas.itemconfigure(self.rect2, state = "hidden")

    
