from turtle import Turtle

MOVE_DISTANCE = 20

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.goto(0,-300)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.goto(0,-300)
