from turtle import Turtle

initial_co = ((-280, 10), (280, 10))
NORTH = 90
SOUTH = 270
MOVE_DIST = 40
BAR_LENGTH = 5


class pongbar:
    def __init__(self, i):
        self.bar = []
        xco, yco = initial_co[i]
        for k in range(BAR_LENGTH):
            new_block = Turtle("square")
            new_block.penup()
            new_block.setheading(NORTH)
            new_block.color("white")
            new_block.goto(xco, yco)
            yco += 20
            self.bar.append(new_block)

    def pongbar_movement(self):
        for i in range(BAR_LENGTH):
            self.bar[i].forward(MOVE_DIST)

    def pongbar_top(self):
        print(self.bar[0].ycor())
        if self.bar[0].ycor() <= 230:
            for i in range(BAR_LENGTH):
                self.bar[i].setheading(NORTH)
            self.pongbar_movement()
        else:
            for i in range(BAR_LENGTH):
                self.bar[i].setheading(SOUTH)
            return

    def pongbar_down(self):
        print(self.bar[0].ycor())
        if self.bar[-1].ycor() >= -230:
            for i in range(BAR_LENGTH):
                self.bar[i].setheading(SOUTH)
            self.pongbar_movement()
        else:
            for i in range(BAR_LENGTH):
                self.bar[i].setheading(NORTH)
            return
