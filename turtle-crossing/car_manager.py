from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "purple", "yellow", "magenta","orange"]
MOVE_DISTANCE = 20
MOVE_INCREMENT = 10
class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = 20

    def create_cars(self):
        random_chance = random.randint(0,6)
        if random_chance == 0:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1,2)
            random_y = random.randint(-280,280)
            new_car.goto(400,random_y)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT


