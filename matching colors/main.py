from turtle import Turtle, Screen
from colors import colors_css
import math

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
START_POS = (-((SCREEN_WIDTH/2) - 100), (SCREEN_HEIGHT/2) - 100)
COLORS_PER_LINE = 6
NUM_OF_LINES = math.ceil(len(colors_css) / COLORS_PER_LINE)

# set the wanted background color for the screen
screen_bgcolor = "darkslategray"

# screen settings
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(screen_bgcolor)
screen.title("Matching Colors")

# pen settings
pen = Turtle()
pen.hideturtle()
pen.up()
pen.speed("fastest")
pen.goto(START_POS)

pen_corx = START_POS[0]
pen_cory = START_POS[1]

# initial writing position
start_index = 0
end_index = COLORS_PER_LINE

for _ in range(NUM_OF_LINES):
    for color in colors_css[start_index:end_index]:
        pen.color(color)
        pen.write(f"{color}", align="center", font=("Arial", 15, "bold"))
        pen.forward(200)

    # set writing position for the next line
    pen_cory -= 20
    pen.goto(pen_corx, pen_cory)

    # set indices for the next color list slice
    start_index += COLORS_PER_LINE
    end_index += COLORS_PER_LINE


screen.exitonclick()