from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.left_score = 0
        self.right_score = 0
        self.write(f'{self.score}', align='center', font=('Courier', 50, 'normal'))

    def left_score_rise(self):
        self.clear()
        self.left_score += 1
        self.write(f'{self.left_score}', align='center', font=('Courier', 50, 'normal'))

    def right_score_rise(self):
        self.clear()
        self.right_score += 1
        self.write(f'{self.right_score}', align='center', font=('Courier', 50, 'normal'))
