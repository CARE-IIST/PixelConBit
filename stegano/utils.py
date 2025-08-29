

def text_to_bin(message: str) -> str:
    """Convert text into a binary string."""
    return ''.join(format(ord(c), "08b") for c in message)

def bin_to_text(binary: str) -> str:
    """Convert a binary string back into text (8 bits = 1 char)."""
    chars = []
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)
