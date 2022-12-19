import turtle
from turtle import Turtle
import random

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]

sashko = Turtle()
sashko.pensize(10)
sashko.speed('fastest')
for _ in range(500):
    sashko.color(random_color())
    sashko.forward(30)
    sashko.setheading(random.choice(directions))
    sashko.color(random_color())

turtle.mainloop()
