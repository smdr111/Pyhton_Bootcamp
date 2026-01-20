import turtle
from turtle import Turtle, Screen
import random as ran

c_list = [(196, 174, 114), (151, 92, 61), (113, 43, 30), (23, 56, 81), (222, 222, 225), (198, 212, 201), (140, 144, 80), (90, 149, 126), (39, 36, 36), (122, 159, 173), (57, 120, 171), (71, 41, 48), (97, 73, 92), (29, 67, 49), (174, 104, 86), (99, 137, 68), (205, 198, 132), (135, 166, 159), (89, 49, 54), (170, 163, 166), (38, 75, 58), (182, 198, 186), (32, 72, 91), (203, 187, 183), (77, 134, 180), (195, 189, 191), (106, 136, 145), (133, 124, 128)]


tim = Turtle()
tim.shape('triangle')
tim.color('black')
tim.speed(0)
tim.pensize(12)
turtle.colormode(255)


def position_turtle():
    tim.up()
    tim.bk(300)
    tim.right(90)
    tim.fd(300)
    tim.left(90)


def first_line():
    for _ in range(10):
        tim.pencolor(ran.choice(c_list))
        tim.dot()
        tim.fd(60)
    tim.left(90)
    tim.fd(60)
    tim.left(90)
    tim.fd(60)

def second_line():
    for _ in range(10):
        tim.pencolor(ran.choice(c_list))
        tim.dot()
        tim.fd(60)
    tim.right(90)
    tim.fd(60)
    tim.right(90)
    tim.fd(60)

position_turtle()

for _ in range(5):
    first_line()
    second_line()









screen = Screen()
screen.exitonclick()