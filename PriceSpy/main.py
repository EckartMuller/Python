import tkinter as tk
import os
import tkinter.messagebox
from PIL import Image, ImageTk
import requests
from rembg import remove
from bs4 import BeautifulSoup
from io import BytesIO
#from win10toast import ToastNotifier

root = tk.Tk()
root.title("Price Spy")
root.resizable(False, False)
root.iconbitmap("./res/price_tag.ico")
root.minsize(500, 600)

bgColor = "#145A57"
fgColor = "#E2E2E2"
labelFont = ('Arial', 14, 'bold')
entryFont = ('Arial', 12, 'bold')
labelDataFont = ('Arial', 10, 'bold')
root.configure(bg=bgColor)
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
#notification = ToastNotifier()
# URL
urlLabel = tk.Label(
    root,
    text="Amazon Product Adress",
    bg=bgColor,
    fg=fgColor,
    font=labelFont,
    pady=10
)
urlLabel.pack()

entryUrl = tk.Entry(
    root,
    width=30,
    font=entryFont,
    bg="#CBCBCB",
    bd=2,
    relief="solid"
)
entryUrl.pack()

# NAME CONTENT
nameSituation = tk.Checkbutton(
    root,
    text="Product Name:",
    bg=bgColor,
    fg=fgColor,
    activebackground=bgColor,
    font=labelFont,
    selectcolor="#929292",
    variable=var1
)

nameSituationLabel = tk.Label(
    root,
    text="... ",
    bg=bgColor,
    fg=fgColor,
    font=labelDataFont,
    pady=10
)
nameSituation.pack(pady=(20, 0))
nameSituationLabel.pack()

# PRICE CONTENT
priceSituation = tk.Checkbutton(
    root,
    text="Price:",
    bg=bgColor,
    fg=fgColor,
    activebackground=bgColor,
    font=labelFont,
    selectcolor="#929292",
    variable=var2
)

priceSituationLabel = tk.Label(
    root,
    text="...",
    bg=bgColor,
    fg=fgColor,
    font=labelDataFont,
    pady=10
)
priceSituation.pack()
priceSituationLabel.pack()

# STOCK CONTENT
stockSituation = tk.Checkbutton(
    root,
    text="In Stock:",
    bg=bgColor,
    fg=fgColor,
    activebackground=bgColor,
    font=labelFont,
    selectcolor="#929292",
    variable=var3
)
stockSituationLabel = tk.Label(
    root,
    text="...",
    bg=bgColor,
    fg=fgColor,
    font=labelDataFont,
    pady=10
)
stockSituation.pack()
stockSituationLabel.pack()

# IMAGE CONTENT
imageSituation = tk.Checkbutton(
    root,
    text="Image: ",
    bg=bgColor,
    fg=fgColor,
    activebackground=bgColor,
    font=labelFont,
    selectcolor="#929292",
    variable=var4
)
imageSituationLabel = tk.Label(
    root,
    text="...",
    bg=bgColor,
    fg=fgColor,
    font=labelDataFont,
    pady=10
)
imageSituation.pack()
imageSituationLabel.pack()

# DEFS
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}


def getContentData():
    try:
        urlStr = str(entryUrl.get())
        nameBool = var1.get()
        priceBool = var2.get()
        stockBool = var3.get()
        imageBool = var4.get()

        # GET DATA
        page = requests.get(urlStr, headers=headers)
        content = BeautifulSoup(page.content, 'html.parser')

        if nameBool:
            productName = content.find(id='productTitle').getText().strip()
            nameSituationLabel.configure(text=f"{productName[0:40]} ...")

        if priceBool:
            productPrice = content.find(class_='a-price-whole').getText().strip()
            priceSituationLabel.configure(text=f"{productPrice[0:6]} TL")

        if stockBool:
            productInStock = content.find(class_='a-size-medium a-color-success').getText().strip()
            stockSituationLabel.configure(text=f"{productInStock}")

        if imageBool:
            img_tag = content.find('img', {'id': 'landingImage'})
            img_url = img_tag['src'] if img_tag else None
            if img_url:
                img_response = requests.get(img_url)
                img_data = BytesIO(img_response.content)
                img = Image.open(img_data)

                # Remove background
                img_no_bg = remove(img)

                img_no_bg = img_no_bg.resize((200, 200), Image.Resampling.LANCZOS)
                tk_img = ImageTk.PhotoImage(img_no_bg)
                imageSituationLabel.configure(image=tk_img)
                imageSituationLabel.image = tk_img

    except Exception as e:
        tkinter.messagebox.showerror(title="Hata", message=f"Bir şeyler yanlış gitti: {e}")

def cagir():
    getContentData()
    root.after(60 * 60 * 1000, cagir)

    """notification.show_toast("Price Spy", "Hey, Price changed !", duration=20, icon_path="./res/icon.ico")"""
    #olmadı
# BUTTON
button_border = tk.Frame(root, highlightbackground="black", highlightthickness=2, bd=0)
buttonForward = tk.Button(
    button_border,
    text='Fiyat Değişince Bildir',
    fg='black',
    padx=5,
    pady=5,
    bg="#CBCBCB",
    font=(("Arial"), 12, 'bold'),
    command=cagir
)

buttonForward.pack()
button_border.pack()

root.mainloop()
