from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Main_body(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.turtle_speed = MOVE_DISTANCE

    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def move_up(self):
        self.forward(self.turtle_speed)

    def level_up(self):
        self.turtle_speed += 10