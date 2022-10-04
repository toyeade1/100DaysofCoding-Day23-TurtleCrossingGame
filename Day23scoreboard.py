from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.pu()
        self.hideturtle()
        self.score = 1
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.score} ', align='left', font=FONT)

    def add_level(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write('  GAME OVER\nCLICK TO EXIT', align='center', font=FONT)



