# 🔒 Image Steganography in Python  

Hide and extract secret text inside images using Python.  
This project is built **from scratch** for learning, with simple scripts (`hide.py` and `Extract.py`).  

---

## 📌 Features
- Convert text ↔ binary (ASCII & UTF-8).
- Add payloads with **headers** for message length.
- Hide and extract data from images (PNG).
- Learn concepts: **LSB (Least Significant Bit), binary, ASCII, bytes**.

---

## 🛠️ Requirements
- Python 3.x  
- Pillow (`pip install pillow`)  

---

## 📂 Project Structure
📦 Image-Steganography
┣ 📜 hide.py # Main interactive program
┣ 📜 Extract.py # Conversion helpers (text/bytes ↔ bits)
┣ 📂 assets # Original and encoded images
┗ 📜 README.md # Documentation


---

## 🚀 Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/image-steganography.git
cd image-steganography


📖 Key Terms

ASCII: Standard encoding for characters (A = 65).

Binary: Data in 0 and 1. Example: "H" → 01001000.

Byte: 8 bits.

Payload: Your message + 4-byte header storing length.

LSB (Least Significant Bit): Smallest bit in binary, used to hide data in pixel values.

⚡ Code Snippets
Convert Text → Binary
def text_to_bits(message: str) -> str:
    return " ".join(format(ord(c), "08b") for c in message)

Binary → Text

def bits_to_text(bits: str) -> str:
    return "".join(chr(int(c, 2)) for c in bits.split(" "))

🖼️ How It Works

Each pixel has 3 values (R, G, B).

We change the last bit (LSB) of each value to hide message bits.

Human eyes can’t detect this small change.

✅ TODO (Future Upgrades)

Add GUI with Tkinter.

Support hiding files.

Encrypt data before hiding.

Benchmark with img.load() vs getpixel() vs putpixel().

🤝 Contributing

Pull requests welcome!

📜 License

MIT License. Free to use and modify.
