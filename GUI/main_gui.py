import tkinter as tk
from GUI.intro import IntroPage
from GUI.swc_setup import SWCSetupPage
from GUI.dynamic_input import DynamicInputPage
from GUI.config_swc import ConfigPage
from GUI.confirmation import ConfirmationPage

class AppController:
    def __init__(self, root):
        self.root = root
        self.root.title("SWC Generator")
        self.frames = {}

        container = tk.Frame(root)
        container.pack(fill="both", expand=True)

        for F in (IntroPage, SWCSetupPage, DynamicInputPage, ConfigPage, ConfirmationPage):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IntroPage)

    def show_frame(self, page_class):
        """Switch to the given frame by class reference."""
        if page_class not in self.frames:
            print(f"Error: {page_class} not found in self.frames")  # Debugging
        else:
            frame = self.frames[page_class]
            frame.tkraise()
