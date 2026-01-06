from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.levl = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.levl}", align="left", font=FONT)

    def increase(self):
        self.levl += 1
        self.update_scoreboard()

    def over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
