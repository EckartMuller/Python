import tkinter as tk
import serial


port = serial.Serial('COM3', 9600)

def on_scale_change(value):
    try:
        value_to_send = int(value)
        if 0 <= value_to_send <= 180:
            port.write(f"{value_to_send}\n".encode())
            print(f"{value_to_send}")
    except ValueError:
        print("hata")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("scale")
scale = tk.Scale(root, from_=0, to=180, orient=tk.HORIZONTAL, command=on_scale_change)
scale.pack()


root.mainloop()

port.close()
