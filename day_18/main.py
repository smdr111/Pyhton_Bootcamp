import turtle
from turtle import Turtle, Screen
import random as ran

tim = Turtle()
tim.shape('triangle')
tim.color('black')
turtle.colormode(255)



def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    tup = (r,g,b)
    return tup


#tim.pensize(10)
tim.speed(0)
angle = [0,90,180,270]
colors = ['brown','blue','red','black','black','grey','green','yellow','orange']
def draw_circle(size_gap):
    for _ in range(int(360/size_gap)):
        tim.pencolor(random_color())
        tim.circle(150)
        tim.setheading(tim.heading()+size_gap)













screen = Screen()
screen.exitonclick()