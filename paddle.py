from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        x = self.xcor()
        y = self.ycor()
        if y < 260:
            self.goto(x, y+20)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()
        if y > -260:
            self.goto(x, y-20)
