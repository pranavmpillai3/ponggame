from turtle import Screen
import time
from pongbar import pongbar
from pongBall import pongball

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
game_on = True

Pong1 = pongbar(0)
Pong2 = pongbar(1)
PongBall = pongball()

screen.listen()
screen.onkey(Pong1.pongbar_top, "w")
screen.onkey(Pong1.pongbar_down, "s")
screen.onkey(Pong2.pongbar_top, "Up")
screen.onkey(Pong2.pongbar_down, "Down")
bars = (Pong1, Pong2)
# screen.tracer(1)
while game_on:
    screen.update()
    time.sleep(0.1)
    PongBall.ball_movement()
    PongBall.collide_with_bar(bars)

screen.exitonclick()
