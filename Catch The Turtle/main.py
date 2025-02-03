import turtle
import time#sayaca göre mole hareket edecek
import random#x ve y konumları rastgele

bgImage = "./image/bg.gif"
moleImage = "./image/mole.gif"
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Catch The Mole")
screen.setup(700,600)
pen = turtle.Turtle()

#skor
pen.hideturtle()
pen.penup()
pen.goto(0, screen.window_height() // 2 - 60)
pen.pencolor("white")
pen.write("Skor: ", align="center", font=("Verdana", 30, "normal", "bold"))

#rsmi ekledim
screen.addshape(bgImage)
screen.bgpic(bgImage)

#mole eklendi
mole = turtle.Turtle()
screen.addshape(moleImage)
mole.shape(moleImage)
mole.penup()
mole.goto(0,80)

#zamana göre mole gaccak
turtle.tracer(0)
def timer(duration):
    print("basladi")
    time.sleep(duration)


score = 0
blokla = False
skorWrite = turtle.Turtle()
finalPuan = 5
def updateScore():
    global score
    score +=1
    skorWrite.penup()
    skorWrite.hideturtle()
    skorWrite.goto(80, 240)
    skorWrite.pencolor("white")
    skorWrite.clear()
    skorWrite.write(score, align="center", font=("Verdana", 30, "normal","bold"))

def moveMole():
    current_x, current_y = mole.position()
    delta_x = random.randint(-250, 250)  #
    delta_y = random.randint(-250, 250)

    new_x = current_x + delta_x
    new_y = current_y + delta_y

    # Ekran sınırları kontrolü
    if new_x < -290 or new_x > 290:
        new_x = current_x
    if new_y < -290 or new_y > 290:
        new_y = current_y

    mole.goto(new_x, new_y)
def moleClicked(x, y):
    global score
    if score < finalPuan:
        if mole.distance(x, y) < 40:
            updateScore()
            moveMole()
    if score >= finalPuan:
        skorWrite.clear()
        pen.clear()
        skorWrite.goto(0, 0)
        skorWrite.write("END", align="center", font=("Verdana", 50, "bold"))


screen.onscreenclick(moleClicked)


def gameLoop():
    if score < finalPuan:
        moveMole()
        screen.ontimer(gameLoop, 100)


gameLoop()
turtle.tracer(1)
screen.mainloop()
