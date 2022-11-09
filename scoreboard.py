from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.l_score} {self.r_score}", align="center", font=("Courier", 60, "bold"))

    def left_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.update_scoreboard()