import turtle
turtleScreen = turtle.Screen()
turtleScreen.bgcolor("black")
turtleScreen.title("Helix")

turtleInstance = turtle.Turtle()
turtleInstance.color("dark blue")
turtle.speed(0)
colorsList = ["red","purple","blue","green","orange","yellow"]
print(len(colorsList))

for x in range(100):
    turtleInstance.color(colorsList[x % 6])
    turtleInstance.circle(10 * x)
    turtleInstance.circle(-10 * x)
    turtleInstance.left(x)


turtle.mainloop()
#turtle.done()