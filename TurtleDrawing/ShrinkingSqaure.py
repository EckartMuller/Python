import turtle

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("light green")
turtleScreen.title("Turtle Python")

turtleInstance = turtle.Turtle()
turtleInstance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtleInstance.forward(size)
        turtleInstance.left(90)
        size-= 5

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(100)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(10)

turtle.done()