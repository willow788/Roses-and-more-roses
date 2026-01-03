import time
import math
import turtle
from turtle import *

Screen = turtle.Screen()
Screen.bgcolor("black")
Screen.title("Maurer Rose")

# Set up the drawing pen
pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.color("#a20b4a")
pen.pensize(2)

Screen.tracer(0, 0)
# to trace the drawing process

n = 361  # number of lines
step_angle = 71 # step angle in degrees
k = 15
scale = 250  # scale to fit the window

coords = []
for i in range(n):
    theta = math.radians(i * step_angle)
    r = math.cos(k * theta)

    # Cartesian coordinates of the Maurer Rose
    x = scale * r * math.cos(theta)
    y = scale * r * math.sin(theta)
    coords.append((x, y))

  
    pen.goto(coords[0])
    

    #the explanation of the 1st loop is to compute the points of the Maurer Rose and store them in coords list
    #why are we storing the points? because we need to draw lines between these points in a specific order
    #how are we going to draw the lines? by iterating through the coords list and using pen.goto() to move the pen to each point


# Draw the Maurer Rose
#enumerate function adds a counter to an iterable and returns it as an enumerate object
for i , (x, y) in enumerate(coords):
    pen.goto(x, y)


#if i is divisible by 8, update the screen and pause briefly
    if i % 8 == 0:
        Screen.update()
        time.sleep(0.1)


Screen.update()
turtle.done()



#oh jesus, i'm finnally getting the hang of this
