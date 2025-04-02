import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.sety(random.randint(-250,250))
        self.setx(250)

    def move_cars(self):
        new_x = self.xcor() - MOVE_INCREMENT
        self.goto(new_x,self.ycor())



