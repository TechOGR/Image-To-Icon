from PIL import Image
from os.path import (
    basename
)

def convert_to_icon(path_image, path_out, size=(256,256)):
    
    nameFile = basename(path_image)
    
    if (nameFile.endswith(".png")):
        convertPNG(path_image, path_out)
    elif (nameFile.endswith(".jpg") or nameFile.endswith(".jpeg")):
        convertJPG(path_image, path_out, size)
    
def convertPNG(path, path_out, size=(90,90)):
    img = Image.open(path)
    img.save(path_out, sizes=[size])

def convertJPG(path, path_out, size):
    img = Image.open(path)
    icon = img.convert("RGBA")
    icon.save(path_out, sizes=[size])