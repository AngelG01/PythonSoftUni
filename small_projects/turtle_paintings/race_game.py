from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink']
speeds = [10, 20, 30]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []
if user_bet:
    is_race_on = True

for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f'You won. The wining turtle is the {winning_turtle} one!')
            else:
                print(f'You lost. The wining turtle is the {winning_turtle} one!')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
