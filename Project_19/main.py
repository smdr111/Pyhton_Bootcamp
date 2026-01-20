from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle win the race.\nEnter a color:')
colors =['red','orange','yellow','blue','green','purple']
positions = [-100,-60,-20,20,60,100]
random_num = random.randint(0,10)
all_turtles = []


for t_index in range(6):
    tim = Turtle(shape='turtle')
    tim.color(colors[t_index])
    tim.penup()
    tim.goto(x=-240,y=positions[t_index])
    all_turtles.append(tim)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")
        random_dist = random.randint(0,10)
        turtle.fd(random_dist)

screen.exitonclick()
