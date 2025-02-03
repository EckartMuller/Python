from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def save_and_encrypt_notes():
    title = title_entry.get()
    message = input_text.get("1.0",END)
    master_secret = master_secret_input.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showerror(title="Hata",message="Butun bilgileri giriniz")
    else:
        message_encryped = encode(master_secret, message)        

        try:
            with open("mysecret.txt","a") as data_file:
                data_file.write(f"\n{title}\n{message_encryped}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message}")
        finally:
            title_entry.delete(0,END)
            master_secret_input.delete(0, END)
            input_text.delete("1.0",END)

def decrypt_notes():
    message_encrypted = input_text.get("1.0",END)
    master_secret = master_secret_input.get()
    if len(message_encrypted) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Hata", message="Bilgileri giriniz.!")
    else:
        try:
            decrypted_message = decode(master_secret, message_encrypted)
            input_text.delete("1.0",END)
            input_text.insert("1.0", decrypted_message)
        except:
            messagebox.showinfo(title="Hata",message="Şifrelenmeyen bir mesajı çözmeye calısmayın")


#UI
FONT = ('Verdana',14,'normal')
window = Tk()
window.title("Secret Notes")
window.config(padx=30,pady=30)
window.resizable(False,False)

original_image = Image.open("res/secret.png")
resized_image = original_image.resize((80, 80))
photo = ImageTk.PhotoImage(resized_image)
photo_label = Label(image=photo)
photo_label.pack()

title_info_label = Label(text="Enter Your Title: ", font=FONT)
title_info_label.pack()

title_entry = Entry(width=54)
title_entry.pack()

input_info_label = Label(text="Enter Your Note: ", font=FONT)
input_info_label.pack()

input_text = Text(width=40,height=20,padx=5,pady=5)
input_text.pack()

master_secret_label = Label(text="Enter manster key", font=FONT)
master_secret_label.pack()

master_secret_input = Entry(width=54)
master_secret_input.pack()

save_button = Button(text="Save & Encrypt",command=save_and_encrypt_notes, padx=5,pady=5,bd=4)
save_button.pack()

decrypt_button = Button(text="Decrypt",bd=4,command=decrypt_notes)
decrypt_button.pack(padx=5,pady=10)

window.mainloop()