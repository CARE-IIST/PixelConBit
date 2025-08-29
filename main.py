import os
os.system("clear")
from stegano.encode import encode
from stegano.decode import decode
from stegano.capacity import capacity

if __name__ == "__main__":
    choice = input("Do you want to (e)ncode or (d)ecode? ")

    if choice.lower() == "e":
        msg = input("Enter secret message : ")
        pwd = input("Set a password : ")
        encode("asset/rose.png", msg, pwd, "asset/rose_encoded.png")
        print("Message hidden successfully!")

    elif choice.lower() == "d":
        pwd = input("Enter password to decode : ")
        secret = decode("asset/rose_encoded.png", pwd)
        print("Decoded : ", secret)

    else:
        print("Invalid choice")

    # show capacity
    bits = capacity("asset/rose.png")
    print("Image can hold up to", bits//8, "bytes.")
