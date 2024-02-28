from PIL import Image
from os.path import (
    join
)

def convert_to_icon(path_image, name_file, size=(256,256)):
    
    pathFile = path_image
    nameFile = name_file
    
    if (nameFile.endswith(".png")):
        path_out = join(pathFile, name_file.replace("png", "ico"))
        convertPNG(join(pathFile, nameFile), path_out)
    elif (nameFile.endswith(".jpg")):
        path_out = join(pathFile, name_file.replace("jpg", "ico"))
        convertJPG(join(pathFile, nameFile), path_out, size)
    elif (nameFile.endswith("jpeg")):
        path_out = join(pathFile, name_file.replace("jpeg", "ico"))
        convertJPG(join(pathFile, nameFile), path_out, size)
    else:
        print("Formato no soportado")

def getValueEnviron():
    ...
        
def convertPNG(path, path_out, size=(90,90)):
    img = Image.open(path)
    img.save(path_out, sizes=[size])

def convertJPG(path, path_out, size):
    img = Image.open(path)
    icon = img.convert("RGBA")
    icon.save(path_out, sizes=[size])