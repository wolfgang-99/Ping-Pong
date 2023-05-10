from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with up and down wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bonce_x()

    # detect collision when R_paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    # detect collision when l_paddle misses
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()
