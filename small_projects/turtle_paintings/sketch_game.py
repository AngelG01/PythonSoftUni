import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed('fastest')
screen = turtle.Screen()
turtle.title("Sketch and fun")


def move_forward():
    timmy.forward(10)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


def move_backwards():
    timmy.backward(10)


def delete_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='a', fun=move_left)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=move_right)
screen.onkeypress(key='c', fun=delete_drawing)

screen.exitonclick()
