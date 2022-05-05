# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii
#
# keyPair = RSA.generate(3072)
#
# pubKey = keyPair.publickey()
# print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
# pubKeyPEM = pubKey.exportKey()
# print(pubKeyPEM.decode('ascii'))
#
# print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
# privKeyPEM = keyPair.exportKey()
# print(privKeyPEM.decode('ascii'))
#
# # encryption
# msg = 'A message for encryption'
# encryptor = PKCS1_OAEP.new(pubKey)
# encrypted = encryptor.encrypt(msg)
# print("Encrypted:", binascii.hexlify(encrypted))

from tkinter import *
import qrcode
import rsa
from tkinter import messagebox
import base64


def encrypt():
    message = text1.get(1.0, END)
    title = qr_name.get()



    # def file_open(file):
    #     key_file = open(file, 'rb')
    #     key_data = key_file.read()
    #     key_file.close()
    #     return key_data
    #
    # privkey = rsa.PrivateKey.load_pkcs1(file_open('privatekey.key'))
    # encrypted_message = rsa.sign(message,privkey, 'SHA-512')
    #
    # s = open('signature_file', 'wb')
    # s.write(encrypted_message)


    create_qr = qrcode.make(message)
    # print(encrypted_message)
    create_qr.save(str(title) + ".png")

    global Image

    Image = PhotoImage(file=str(title) + ".png")
    Image_view.config(image=Image)

    (pubkey, privkey) = rsa.newkeys(2048)

    with open('publickey.key', 'wb') as key_file:
        key_file.write(pubkey.save_pkcs1('PEM'))

    with open('privatekey.key', 'wb') as key_file:
        key_file.write(privkey.save_pkcs1('PEM'))

    public_key = open("publickey.key", "r")
    # private_key = open("privatekey.key", "r")

    show_key = Label(create_screen, text=public_key.read())
    show_key.pack(padx=10, pady=50, side=BOTTOM)


def create():
    global text1
    global qr_name
    global Image_view
    global create_screen

    create_screen = Toplevel(screen)
    create_screen.title("Qr Generator")
    create_screen.geometry("375x700")

    Image_view = Label(create_screen)
    Image_view.pack(padx=50, pady=10, side=BOTTOM)

    Label(create_screen, text="Enter text to encrypt", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text1 = Text(create_screen, font="calibri", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=40, width=355, height=100)

    Label(create_screen, text="Name of the QR", fg="black", font=("calibri", 13)).place(x=10, y=140)
    qr_name = Entry(create_screen, font="calibri")
    qr_name.place(x=10, y=170, width=355, height=30)

    Button(create_screen, text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(
        x=100, y=250)


def scan():
    scan_screen = Toplevel(screen)
    scan_screen.title("Qr Scanner")
    scan_screen.geometry("375x700")

    Image_view = Label(scan_screen)
    Image_view.pack(padx=50, pady=10, side=BOTTOM)

    Label(scan_screen, text="Enter the key to decrypt", fg="black", font=("calibri", 13)).place(x=10, y=10)
    text2 = Text(scan_screen, font="calibri", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text2.place(x=10, y=40, width=355, height=100)

    Button(scan_screen, text="DECRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0).place(
        x=100, y=250)


def main_screen():
    global screen

    screen = Tk()
    screen.title("QR Generator using RSA Encryptor")
    screen.geometry("500x500")
    screen.resizable(False, False)

    Label(screen, text="QR Generator using RSA Encryption", fg="black", font=20).place(x=115, y=10)

    Button(text="Generate QR", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=create).place(x=60, y=200)
    Button(text="Scan QR", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=scan).place(x=260, y=200)

    screen.mainloop()


main_screen()
