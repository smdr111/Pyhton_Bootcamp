import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
board = Scoreboard()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    cars.move()

    # Collision with wall
    if player.ycor() > 280:
        time.sleep(1.5)
        board.point()
        player.restart()
        cars.add_speed()

    # Collision with car
    for car in cars.cars:
        if player.distance(car) < 22:
            game_is_on = False
            board.game_over()














screen.exitonclick()