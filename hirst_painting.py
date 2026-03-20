import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

mikey = Turtle()
mikey.shape("turtle")
mikey.penup()
mikey.hideturtle()
mikey.goto(-250, -250)
x = -250
y = -250
for row in range(10):

    for item in range(10):
        random_color = random.choice(color_list)
        mikey.dot(20, random_color)
        mikey.penup()
        mikey.forward(50)

    y += 50
    mikey.goto(x, y)


screen = Screen()
screen.setup(1000,1000)
screen.screensize(1000, 1000)
screen.bgcolor("gray")
screen.exitonclick()
