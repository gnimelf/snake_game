from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 30, "normal")
POSITION = (0, 265)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(POSITION)
        self.update_score()

    def update_score(self):
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
