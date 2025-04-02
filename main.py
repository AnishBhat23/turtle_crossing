import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts
# at the bottom of the screen and listen
# for the "Up" keypress to move the turtle north.

screen.listen()

player = Player()
screen.onkeypress(fun=player.move,key="Up")

# Create cars that are 20px high by 40px wide
# that are randomly generated along the y-axis and
# move to the left edge of the screen.
# No cars should be generated in the top and bottom
# 50px of the screen (think of it as a safe zone for our little turtle).


car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_counter+=1
    if car_counter%6 == 0:
        new_car = CarManager()
        cars.append(new_car)
        car_counter = 0
    for car in cars:
        car.move_cars()
        if abs(player.ycor() - car.xcor()) < 5:
            # Detect when the turtle player collides with a car and stop the game if this happens
            game_is_on = False
            print("Game Over")







