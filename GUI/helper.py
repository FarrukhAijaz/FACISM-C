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

