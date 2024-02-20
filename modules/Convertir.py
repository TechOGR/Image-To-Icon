from PIL import Image

def convert_to_icon(path_image, path_out, size=(256,256)):
    img = Image.open(path_image)
    icon = img.convert("RGBA")
    icon.save(path_out, sizes=[size]) 