from PIL import Image, ImageFilter
from tkinter import Canvas

def blur_image(image: Image.Image, blur_radius: int) -> Image.Image:
    
    return image.filter(ImageFilter.GaussianBlur(blur_radius))


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    """Draws a rounded rectangle on the canvas."""
    points = [
        (x1 + radius, y1), (x2 - radius, y1),  # Top line
        (x2, y1), (x2, y1 + radius),  # Top-right corner
        (x2, y2 - radius), (x2, y2),  # Right line
        (x2 - radius, y2), (x1 + radius, y2),  # Bottom line
        (x1, y2), (x1, y2 - radius),  # Bottom-left corner
        (x1, y1 + radius), (x1, y1)  # Left line
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

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