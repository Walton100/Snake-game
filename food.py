from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('circle')
        self.color('tomato')
        self.respawn()


    def respawn(self):
        x = random.randint(-280,280)
        y = random.randint(-280, 280)
        self.goto(x,y)


