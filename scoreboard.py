from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"SCORE = {self.score}", align = ALIGNMENT,font = FONT)

    def update_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)