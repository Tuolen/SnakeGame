from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.food_generator()

    def food_generator(self):
        x_cor = random.choice(range(-280, 280, 20))
        y_cor = random.choice(range(-280, 280, 20))
        self.goto(x_cor, y_cor)

