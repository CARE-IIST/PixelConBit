from PIL import Image
from stegano.utils import bin_to_text

def decode(img_path, password_input):
    img = Image.open(img_path).convert("RGB")
    pixels = img.load()

    width, height = img.size
    bits = ""

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)

    end_marker = "1111111111111110"
    end_index = bits.find(end_marker)
    if end_index == -1:
        return "No hidden message found"

    hidden_bits = bits[:end_index]
    hidden_text = bin_to_text(hidden_bits)

  
    if "::" not in hidden_text:
        return "No password found in data"

    stored_pass, message = hidden_text.split("::", 1)

    if stored_pass == password_input:
        return message
    else:
        return "Wrong password!"
