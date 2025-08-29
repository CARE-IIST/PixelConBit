from PIL import Image

def capacity(img_path):
    img = Image.open(img_path).convert("RGB")
    w, h = img.size
    return w * h * 3   

if __name__ == "__main__":
    bits = capacity("asset/rose.png")
    print("Capacity (bits):", bits)
    print("Capacity (bytes):", bits // 8)



