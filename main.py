# Project for Encryption And Decryption of Basic Text

# It consist of 2 Input Fields one is for Taking the text Data and another is for taking the Password (key) for Encryption and Decryption
# Along with that it consist of 2 Buttons one is for Encryption and another is for Decryption and one extra for reseting the fields

from tkinter import *
from tkinter import messagebox
import base64
import os

def encrypt():
    password = code.get()

    if password == "doit":
        screen1 = Toplevel(screen)
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        Label(screen1, text= "ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40, width=380, height=150)

        text2.insert(END,encrypt)

    elif password =="":
        messagebox.showerror("encryption", "Input right Password")

    elif password != "doit":
        messagebox.showerror("encryption", "Invalid Password")

def decrypt():
    password = code.get()

    if password == "doit":
        screen2 = Toplevel(screen)
        screen2.title("decrypt")
        screen2.geometry("400x200")
        screen2.configure(bg="blue")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text= "ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10,y=0)
        text2=Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40, width=380, height=150)

        text2.insert(END,decrypt)

    elif password =="":
        messagebox.showerror("decryption", "Input right Password")

    elif password != "doit":
        messagebox.showerror("decryption", "Invalid Password")

def main_scree():
    global screen
    global code
    global text1

    screen =Tk()
    screen.geometry("400x500")

    #icons
    image_icon = PhotoImage(file="Encryption-Decryption\keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Encryption App")

    def reset():
        code.set("")
        text1.delete(1.0, END) #

    Label(text="Enter text for encryption and decryption", font="arial 20 bold", fg="black").place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", highlightbackground="lightgray", highlightcolor="lightgray", relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10, y=50, width=400, height=60)

    Label(text="Enter The Key to Encry or Decrypt", fg="black", font="arial 15 bold").place(x=10, y=120)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font="arial 15" ,show="*").place(x=10, y=150)

    # Buttons
    Button(text="Encryption", width=8, height=2, bd=0, bg="red", fg="white", font="arial 15 bold", command=encrypt).place(x=10, y=180)
    Button(text="Decryption", width=8, height=2, bd=0, bg="yellow", fg="white", font="arial 15 bold", command=decrypt).place(x=200, y=180)
    Button(text="Reset", width=8, height=2, bd=0, bg="gray", fg="white", font="arial 15 bold" , command=reset).place(x=10, y=280)

    screen.mainloop()


main_scree()