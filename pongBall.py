from turtle import Turtle
import sys
from pongbar import BAR_LENGTH

initial_co = (0, 0)
NORTH_EAST = 45
NORTH_WEST = 135
SOUTH_WEST = 225
SOUTH_EAST = 315
MOVE_DIST = 20


class pongball:
    def __init__(self):
        self.ball = Turtle('circle')
        self.ball.setheading(NORTH_EAST)
        self.ball.penup()
        self.ball.color('red')
        self.ball.goto(initial_co)
        # self.ball.speed(1)

    def ball_movement(self):
        print(self.ball.ycor())
        print(self.ball.heading())
        self.ball.forward(MOVE_DIST)
        self.collide_with_top_wall()

    def collide_with_top_wall(self):
        if self.ball.ycor() >= 270 and self.ball.heading() == NORTH_EAST:
            self.ball.setheading(SOUTH_EAST)
        elif self.ball.ycor() >= 270 and self.ball.heading() == NORTH_WEST:
            self.ball.setheading(SOUTH_WEST)
        if self.ball.ycor() <= -290 and self.ball.heading() == SOUTH_WEST:
            self.ball.setheading(NORTH_WEST)
        elif self.ball.ycor() <= -290 and self.ball.heading() == SOUTH_EAST:
            self.ball.setheading(NORTH_EAST)

    def collide_with_bar(self, bars):
        for b in bars:
            for i in range(BAR_LENGTH):
                xco, yco = b.bar[i].xcor(), b.bar[i].ycor()
                if xco - 30 <= self.ball.xcor() <= xco + 30 and \
                        yco - 30 <= self.ball.ycor() <= yco + 30:
                    if self.ball.heading() == NORTH_EAST:
                        self.ball.setheading(NORTH_WEST)
                        return
                    elif self.ball.heading() == NORTH_WEST:
                        self.ball.setheading(NORTH_EAST)
                        return
                    elif self.ball.heading() == SOUTH_EAST:
                        self.ball.setheading(SOUTH_WEST)
                        return
                    elif self.ball.heading() == SOUTH_WEST:
                        self.ball.setheading(SOUTH_EAST)
                        return
        self.collide_with_side_wall()

    def collide_with_side_wall(self):
        if self.ball.xcor() >= 300 or self.ball.xcor() <= -300:
            sys.exit()
