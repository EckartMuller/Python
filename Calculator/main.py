from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("./res/cal.ico")
screenWidth = 300
screenHeight = 510
root.config(bg="#BDBFC1")

root.minsize(screenWidth, screenHeight)
root.resizable(False, False)

entryCal = Entry(root, font=('Arial', 25, 'bold'), width=4, insertwidth=2, bd=3, justify="right", bg="#A5A5A5", fg="white", highlightthickness=0)
entryCal.grid(padx=5, pady=(10, 0), row=0, column=0, columnspan=4, sticky="ew")

# row1
labelResult = Label(root, font=('Arial', 15, 'bold'), width=20, bg="#BDBFC1", fg="white", text="434646532", anchor="e")
labelResult.grid(padx=5, pady=5, row=1, column=0, columnspan=4, sticky="ew")

# row2
btnMod = Button(root, text="%", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnMod.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

btnCE = Button(root, text="CE", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnCE.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

btnC = Button(root, text="C", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnC.grid(row=2, column=2, padx=2, pady=2, sticky="ew")

btnClear = Button(root, text="<-", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnClear.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

# row3
btn7 = Button(root, text="7", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn7.grid(row=3, column=0, padx=2, pady=2, sticky="ew")

btn8 = Button(root, text="8", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn8.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

btn9 = Button(root, text="9", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn9.grid(row=3, column=2, padx=2, pady=2, sticky="ew")

btnMultiply = Button(root, text="x", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnMultiply.grid(row=3, column=3, padx=2, pady=2, sticky="ew")

# row4
btn4 = Button(root, text="4", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn4.grid(row=4, column=0, padx=2, pady=2, sticky="ew")

btn5 = Button(root, text="5", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn5.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

btn6 = Button(root, text="6", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn6.grid(row=4, column=2, padx=2, pady=2, sticky="ew")

btnMinus = Button(root, text="-", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnMinus.grid(row=4, column=3, padx=2, pady=2, sticky="ew")

# row5
btn1 = Button(root, text="1", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn1.grid(row=5, column=0, padx=2, pady=2, sticky="ew")

btn2 = Button(root, text="2", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn2.grid(row=5, column=1, padx=2, pady=2, sticky="ew")

btn3 = Button(root, text="3", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn3.grid(row=5, column=2, padx=2, pady=2, sticky="ew")

btnPlus = Button(root, text="+", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnPlus.grid(row=5, column=3, padx=2, pady=2, sticky="ew")

# row6
btn0 = Button(root, text="0", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn0.grid(row=6, column=0, padx=2, pady=2, sticky="ew")

btn2 = Button(root, text="2", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn2.grid(row=6, column=1, padx=2, pady=2, sticky="ew")

btn3 = Button(root, text="3", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btn3.grid(row=6, column=2, padx=2, pady=2, sticky="ew")

btnResult = Button(root, text="=", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1)
btnResult.grid(row=6, column=3, padx=2, pady=2, sticky="ew")

# Kolon genişliklerini ayarla
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
