import time
from turtle import Screen
from the_turtle import Main_body
from cars import Cars
from turtle_crossing.scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

main_turtle = Main_body()
car_generator = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(main_turtle.move_up, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_generator.create_car()
    car_generator.move_cars()

    # Detect collision with a car
    for car in car_generator.all_cars:

        if car.distance(main_turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect if player has reached top side of the screen

    if main_turtle.ycor() == 300:
        main_turtle.go_to_start()
        scoreboard.update_score()
        main_turtle.level_up()
        car_generator.move_faster_car()

screen.exitonclick()
