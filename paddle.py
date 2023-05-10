from turtle import Turtle

COLOR = "red"


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.paddle_creating(position)

    def paddle_creating(self, position):
        self.color(COLOR)
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
