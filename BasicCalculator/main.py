from tkinter import *

root = Tk()
root.title("Calculator")
root.iconbitmap("./res/cal.ico")
root.attributes("-topmost", True)
screenWidth = 300
screenHeight = 510
root.config(bg="#BDBFC1")
entryInput = StringVar()
root.minsize(screenWidth, screenHeight)
root.resizable(False, False)

#defs

def buttonClick(num):
    current = entryInput.get()

    # Operatörlerin tanımlanması
    operators = set("+-*/%.")

    # Son karakterin operatör olup olmadığını kontrol et
    if current and current[-1] in operators and num in operators:
        current = current[:-1]

    entryInput.set(current + str(num))


def clearEntry():
    entryInput.set("")

def undo():
    current = entryInput.get()
    entryInput.set(current[:-1])

def calculate():
    try:
        result = eval(entryInput.get())
        entryInput.set(result)
    except:
        entryInput.set("Error")

def onKeyPress(event):
    if(event.keysym == "Return"):
        calculate()
    elif(event.keysym == "BackSpace"):
        undo()

def nega():
    current = entryInput.get()
    newCurrent = f"-{current}"
    entryInput.set(newCurrent)
#defsend




entryCal = Entry(root, textvariable=entryInput, font=('Arial', 25, ''), width=4, bd=3, justify="right", bg="#A5A5A5", fg="white", highlightthickness=0,insertontime=0)
entryCal.grid(padx=5, pady=(10, 0), row=0, column=0, columnspan=4, sticky="ew")
entryCal.focus_set()
entryCal.bind("<KeyPress>",onKeyPress)
# row1
labelResult = Label(root, font=('Arial', 15, 'bold'), width=20, bg="#BDBFC1", fg="white", text="", anchor="e")
labelResult.grid(padx=5, pady=5, row=1, column=0, columnspan=4, sticky="ew")

# row2
btnMod = Button(root, text="%", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick('%'))
btnMod.grid(row=2, column=0, padx=2, pady=2, sticky="ew")

btnCE = Button(root, text="CE", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=clearEntry)
btnCE.grid(row=2, column=1, padx=2, pady=2, sticky="ew")

btnC = Button(root, text="C", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=clearEntry)
btnC.grid(row=2, column=2, padx=2, pady=2, sticky="ew")

btnClear = Button(root, text="<-", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=undo)
btnClear.grid(row=2, column=3, padx=2, pady=2, sticky="ew")

# row3
btn7 = Button(root, text="7", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(7))
btn7.grid(row=3, column=0, padx=2, pady=2, sticky="ew")

btn8 = Button(root, text="8", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(8))
btn8.grid(row=3, column=1, padx=2, pady=2, sticky="ew")

btn9 = Button(root, text="9", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(9))
btn9.grid(row=3, column=2, padx=2, pady=2, sticky="ew")

btnMultiply = Button(root, text="x", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick('*'))
btnMultiply.grid(row=3, column=3, padx=2, pady=2, sticky="ew")

# row4
btn4 = Button(root, text="4", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(4))
btn4.grid(row=4, column=0, padx=2, pady=2, sticky="ew")

btn5 = Button(root, text="5", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(5))
btn5.grid(row=4, column=1, padx=2, pady=2, sticky="ew")

btn6 = Button(root, text="6", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(6))
btn6.grid(row=4, column=2, padx=2, pady=2, sticky="ew")

btnMinus = Button(root, text="-", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick('-'))
btnMinus.grid(row=4, column=3, padx=2, pady=2, sticky="ew")

# row5
btn1 = Button(root, text="1", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(1))
btn1.grid(row=5, column=0, padx=2, pady=2, sticky="ew")

btn2 = Button(root, text="2", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(2))
btn2.grid(row=5, column=1, padx=2, pady=2, sticky="ew")

btn3 = Button(root, text="3", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(3))
btn3.grid(row=5, column=2, padx=2, pady=2, sticky="ew")

btnPlus = Button(root, text="+", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick('+'))
btnPlus.grid(row=5, column=3, padx=2, pady=2, sticky="ew")

# row6
btn0 = Button(root, text="0", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick(0))
btn0.grid(row=6, column=0, padx=2, pady=2, sticky="ew")

btnDot = Button(root, text=".", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=lambda: buttonClick('.'))
btnDot.grid(row=6, column=1, padx=2, pady=2, sticky="ew")

btnNega = Button(root, text="±", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=nega)
btnNega.grid(row=6, column=2, padx=2, pady=2, sticky="ew")

btnEquals = Button(root, text="=", fg="white", bg="#7F8182", font=("Arial", 16, "bold"), activebackground='#555555', padx=20, pady=20, bd=1, command=calculate)
btnEquals.grid(row=6, column=3, padx=2, pady=2, sticky="ew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
