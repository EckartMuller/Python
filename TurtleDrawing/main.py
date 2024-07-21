import turtle

drawingBoard = turtle.Screen()
drawingBoard.bgcolor("#D6D6D6")
drawingBoard.title("Python Turtle")

turtleInstance = turtle.Turtle()

"""
kare = turtle.Turtle()
for x in range(8):
    turtle.forward(100)
    turtle.left(45)

for x in range(4):
    turtle.forward(100)
    turtle.left(90)

yildiz = turtle.Turtle()
yildiz.left(70)
yildiz.forward(200)
yildiz.right(140)
yildiz.forward(200)
yildiz.right(140)
yildiz.forward(210)
yildiz.right(150)
yildiz.forward(230)
yildiz.right(150)
yildiz.forward(220)

yildiz.pencolor("red")
yildiz.begin_fill()
for i in range(5):
    yildiz.right(144)
    yildiz.forward(200)
yildiz.end_fill()
"""
#poligon

num_sides = 5
angle = 360.0 / num_sides
side_length = 100

for x in range(num_sides):
    turtleInstance.right(angle)
    turtleInstance.forward(side_length)


turtle.done()