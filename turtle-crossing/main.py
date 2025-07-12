import turtle
from turtle import Screen
import time
from player import Player
from car_manager import CarManager


screen = Screen()
player = Player()
car_manager = CarManager()
screen.tracer(0)
screen.screensize(300,300)
car_manager.hideturtle()



screen.listen()
screen.onkeypress(player.move , key="Up")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False

    if player.distance(0,300) < 5:
        player.level_up()
        car_manager.speed_up()

















screen.exitonclick()