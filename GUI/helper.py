from PIL import Image, ImageFilter

def blur_image(image: Image.Image, blur_radius: int) -> Image.Image:
    
    return image.filter(ImageFilter.GaussianBlur(blur_radius))
