import math
import turtle
import time

from turtle import *

POINTS = 1000

pen = turtle.Turtle()
pen.speed(0)
pen.color("#c01502")
pen.pensize(2)
pen.hideturtle()

screen = turtle.Screen()
screen.bgcolor("black")

screen.title("Rose Curve")
screen.setup(width=900, height=900)

screen.tracer(0, 0)
#to trace the drawing process

k = 20  # number of petals if k is odd, 2k if k is even
# Scale to fill most of the window without clipping.
scale = min(screen.window_width(), screen.window_height()) * 0.42

for i in range(POINTS+1):
    t = (2 * math.pi * i) / POINTS  # parameter t from 0 to 2π
    r = math.cos(k * t)

    #cartesian coordinates of the rose curve
    x = scale * r * math.cos(t)
    y = scale * r * math.sin(t)

    if i == 0:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
    else:
        pen.goto(x, y)

    if i % 10 == 0:
        screen.update()
        time.sleep(0.2)
    
turtle.done()
