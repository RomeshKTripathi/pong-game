from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 8
        self.y_move = 8
        self.sleep_time = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1
        self.sleep_time *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reposition(self):
        self.goto(0, 0)
        self.x_move *= -1
