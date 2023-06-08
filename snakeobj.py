import time
from turtle import Turtle
DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for n in range(0, 3):
            tim = Turtle(shape="square")
            tim.penup()
            tim.color("white")
            current_cor = tim.xcor()
            tim.setx(current_cor - 20 * n)
            self.segments.append(tim)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[index - 1].xcor()
            y_cor = self.segments[index - 1].ycor()
            self.segments[index].goto(x_cor, y_cor)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.segments[0].heading() == 270:
            return
        self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() == 90:
            return
        self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() == 180:
            return
        self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() == 0:
            return
        self.segments[0].setheading(180)

    def still_on_game(self):
        for i in range(1, len(self.segments) - 1):
            if self.segments[0].xcor() == self.segments[i]:
                return False

        return True

    def add_segment(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.speed("fastest")
        tim.color("white")
        tim.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(tim)

    def position_turtles(self, alien):
        x = alien.xcor()
        y = alien.ycor()
        return (x, y)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def is_game_over(self):
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.reset()
        for segment in self.segments[1:]:
            if self.segments[0].distance(segment) < 15:
                self.reset()




