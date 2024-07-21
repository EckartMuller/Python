import turtle
import tkinter as tk

# Pencere kurulum
screen = turtle.Screen()
screen.title("Python Turtle Paint")
screen.setup(width=800, height=600)

# Kalem kurulum
pen = turtle.Turtle()
pen.speed("fastest")  # Maksimum hız
pen.width(2)

# Kalemi hareket ettir
def move_pen(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Çizim işlevi
def draw(x, y):
    pen.ondrag(None)  # İkili çağrıların önüne geçmek için kaldır
    pen.setheading(pen.towards(x, y))
    pen.goto(x, y)
    pen.ondrag(draw)  # Yeniden etkinleştir

# Fare olayları
screen.onscreenclick(move_pen)  # İlk tıklamada kalemi hareket ettir
pen.ondrag(draw)

# Renk değiştirme işlevi
def change_color(color):
    pen.color(color)

# Kalınlık değiştirme işlevi
def change_pen_size(size):
    pen.width(size)




# Renk değiştirmek için tuş bağlama
screen.listen()
screen.onkey(lambda: change_color("red"), "r")
screen.onkey(lambda: change_color("green"), "g")
screen.onkey(lambda: change_color("blue"), "b")
screen.onkey(lambda: change_color("black"), "k")

# Kalınlık değiştirme için tuş bağlama
screen.onkey(lambda: change_pen_size(1), "1")
screen.onkey(lambda: change_pen_size(2), "2")
screen.onkey(lambda: change_pen_size(3), "3")
screen.onkey(lambda: change_pen_size(4), "4")
screen.onkey(lambda: change_pen_size(5), key="5")
screen.onkey(lambda: change_pen_size(6), key="6")
screen.onkey(lambda: change_pen_size(7), key="7")
screen.onkey(lambda: change_pen_size(8), key="8")
screen.onkey(lambda: change_pen_size(9), key="9")

# Temizleme işlevi
def clear_screen():
    pen.clear()

# Temizleme için tuş bağlama
screen.onkey(clear_screen, "c")

# Ana döngü
try:
    screen.mainloop()
except Exception as e:
    print(f"Hata: {e}")
