from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color('black')
        self.level = 0
        self.write(f'Level: {self.level}', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=('Arial', 20, 'normal'))
