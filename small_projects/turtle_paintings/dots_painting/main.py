# import colorgram
#
# rgb = []
# colors = colorgram.extract('20_001.jpg', 25)
# for current in colors:
#     r = current.rgb.r
#     g = current.rgb.g
#     b = current.rgb.b
#     new_color = (r, b, b)
#     rgb.append(new_color)
# print(rgb)
import random
import turtle
from turtle import Turtle

turtle.colormode(255)
color_list = [(199, 117, 117), (124, 24, 24), (168, 57, 57), (186, 53, 53), (6, 83, 83),
              (109, 85, 85), (113, 175, 175), (22, 174, 174), (64, 138, 138), (39, 36, 36), (76, 48, 48), (9, 47, 47),
              (90, 53, 53),
              (181, 79, 79), (132, 42, 42), (210, 151, 151), (141, 155, 155), (179, 186, 186), (172, 159, 159),
              (212, 177, 177),
              (176, 203, 203)]

timmy = Turtle()
timmy.speed('fastest')
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for dot_count in range(1, 101):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
turtle.mainloop()
