from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.spd = 0

    def make_car(self):
        chance = r.randint(1,10)
        if chance == 1:
            new_car = Turtle('square')
            new_car.color(r.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(290, r.randint(-240, 240))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.spd)


    def add_speed(self):
        self.spd += 3














