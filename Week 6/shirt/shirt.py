import sys
import PIL
from PIL import Image,ImageOps
import os

input_path = os.path.splitext(sys.argv[1])
output_path  = os.path.splitext(sys.argv[2])
allowed_extensions = [".jpg", ".jpeg", ".png"]

shirt = Image.open("shirt.png")
size = shirt.size

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif input_path[1].lower() not in allowed_extensions and output_path[1].lower() not in allowed_extensions:
    sys.exit("Invalid output")
elif input_path[1].lower() != output_path[1].lower():
    sys.exit("Input and output have different extensions")

try:

    image_input = Image.open(sys.argv[1])
    new_image = ImageOps.fit(image_input,size)
    new_image.paste(shirt, mask = shirt)
    new_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
