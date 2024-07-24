import turtle
import random

screen = turtle.Screen()
screen.setup(800,600)
screen.title("Catch The Turtle")
screen.bgpic("./image/bg.gif")
FONT = ('Arial', 30, 'bold')
score = 0
game_over = False
degree = 1
x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]
#turtllist
turtle_list = []
#score turtle
score_turtle = turtle.Turtle()
#countdownturtle
countdown_turtle = turtle.Turtle()
def setup_score_turtle():
    global score_turtle
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.speed(0)
    score_turtle.color("dark blue")
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0,y)
    if game_over != True:
        score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)



def game_setting():
    try:
        global zorluk
        zorluk = str(input("Kolay,Orta,Zor:(K,O,Z) "))
        if zorluk == "K":
            degree = 0
        elif zorluk == "O":
            degree = 1
        elif zorluk == "Z":
            degree = 2
        else:
            degree = 1
    except:
        print("Hata")
        screen.exitonclick()

grid_size = 10

def make_turtle(x,y):
    t = turtle.Turtle()
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    screen.addshape("./image/mole.gif")
    t.shape("./image/mole.gif")
    t.fillcolor('green')
    t.shapesize(3, 3)
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)
def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive fonk
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        if zorluk == "K":
            screen.ontimer(show_turtles_randomly, 1000)
        elif zorluk =="O":
            screen.ontimer(show_turtles_randomly, 500)
        elif zorluk == "Z":
            screen.ontimer(show_turtles_randomly, 100)
        else:
            screen.done()



def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.speed(0)
    countdown_turtle.color("red")
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setpos(0, y-50)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        countdown_turtle.write(arg="GAME OVER", move=False, align="center", font=FONT)
        hide_turtles()




def start_game_up():
    game_setting()
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)




start_game_up()
turtle.done()