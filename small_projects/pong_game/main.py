import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
draw_mid_line = Turtle()
draw_mid_line.penup()
draw_mid_line.hideturtle()
draw_mid_line.goto(0,300)
draw_mid_line.setheading(270)
draw_mid_line.color('white')

for i in range(10):
    draw_mid_line.pendown()
    draw_mid_line.forward(30)
    draw_mid_line.penup()
    draw_mid_line.forward(30)

#
left_scoreboard = Scoreboard((-50, 220))
right_scoreboard = Scoreboard((50, 220))
# Paddles and ball
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
# Screen listener

screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect if a goal is scored
    if ball.xcor() > 380:
        ball.reset_position()
        left_scoreboard.left_score_rise()
        ball.move_speed = 0.1

    if ball.xcor() < - 380:
        ball.reset_position()
        right_scoreboard.right_score_rise()
        ball.move_speed = 0.1


screen.exitonclick()
