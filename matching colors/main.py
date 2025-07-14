from turtle import Turtle, Screen
from colors import colors_css

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
START_POS = (-((SCREEN_WIDTH/2) - 100), (SCREEN_HEIGHT/2) - 100)

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

screen_bgcolor = "white"
screen.bgcolor(screen_bgcolor)

screen.title("Matching Colors")

pen = Turtle()
pen.hideturtle()
pen.up()
pen.goto(START_POS)


pen_corx = START_POS[0]
pen_cory = START_POS[1]

colors_per_line = 0
print(pen.position())

for color in colors_css[:20]:
    if colors_per_line <= 5:
        pen.color(color)
        pen.write(f"{color}", align="center", font=("Arial", 15, "bold"))
        pen.forward(150)
        colors_per_line += 1
        print(pen.position())
    else:
        pen_cory -= 20
        pen.goto(pen_corx , pen_cory)
        print(pen.position())
        colors_per_line = 0

screen.exitonclick()