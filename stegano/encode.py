from PIL import Image
from stegano.utils import text_to_bin

img=Image.rotate(fillcolor="black")
# Encode message + password
def encode(img_path, message, password, out_path):
   
    full_text = password + "::" + message
    binary = text_to_bin(full_text) + "1111111111111110"  

    img = Image.open(img_path).convert("RGB")
    pixels = img.load()

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx < len(binary):
                r, g, b = pixels[x, y]
                r = (r & ~1) | int(binary[idx]); idx += 1
                if idx < len(binary):
                    g = (g & ~1) | int(binary[idx]); idx += 1
                if idx < len(binary):
                    b = (b & ~1) | int(binary[idx]); idx += 1
                pixels[x, y] = (r, g, b)

    img.save(out_path)
    return True
