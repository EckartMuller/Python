from tkinter import *


root = Tk()
root.title("BMI Calculator")
root.iconbitmap("./res/bmi.ico")
root.resizable(False,False)
root.minsize(300,400)
root.attributes("-topmost",True)
root.configure(bg="white")
var1 = StringVar(root)
var1.set("160")
var2 = StringVar(root)
var2.set(60)

def calculate():
    try:
        height = float(spinboxHeight.get())
        weight = float(spinboxWeight.get())
        # BMI hesaplama
        bmi = weight / ((height / 100) ** 2)
        labelResult.config(text=f"BMI: {bmi:.2f}")
        if bmi <= 18.5:
            labelWarn.config(text="Zayıf")
        elif bmi > 18.5 and bmi < 24:
            labelWarn.config(text="Normal")
        elif bmi > 25 and bmi < 30:
            labelWarn.config(text="Kilolu")
        elif bmi >= 30:
            labelWarn.config(text="Obez")

    except ValueError:
        labelResult.config(text="Error")



labelName = Label(root,text="BMI CALCULATOR", font=('Arial',18,'bold'),padx=20,pady=10,fg="black",bg="white")
labelName.configure(justify='center')
labelName.pack()

labelHeight = Label(root,text="Height: ", font=('Arial',18,'bold'),padx=20,pady=10,fg="black",bg="white")
labelHeight.pack()
spinboxHeight = Spinbox(root,from_=100,to=250,font=('Arial',16,'bold'),width=10,textvariable=var1,repeatdelay=200,repeatinterval=30)
spinboxHeight.pack()
spinboxHeight.focus()

labelWeight = Label(root,text="Weight: ", font=('Arial',18,'bold'),padx=20,pady=10,fg="black",bg="white")
labelWeight.pack()
spinboxWeight = Spinbox(root,from_=35,to=300,font=('Arial',16,'bold'),width=10,textvariable=var2,repeatdelay=200,repeatinterval=30)
spinboxWeight.pack()

btnCal = Button(root,text="Calculate",activebackground="lightgray",width=10,height=3,cursor='hand2',font=('Arial',14,'bold'),command=calculate,bg="white")
btnCal.pack(pady=20)

labelResult = Label(root,text="Result", font=('Arial',18,'bold'),padx=20,pady=10,fg="black",bg="white")
labelResult.pack()

labelWarn = Label(root,text="", font=('Arial',18,'bold'),padx=20,pady=10,fg="black",bg="white")
labelWarn.pack()



root.mainloop()