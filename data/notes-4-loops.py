# Notes - Loops
# 14 October
# Ian Poon

import random
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("cyan")

# TMNT - turtles
# create a turtle called mike
mike = turtle.Turtle()
mike.turtlesize(5)
mike.shape("turtle")
mike.color("orange")

# move mike around
mike.speed(2)
mike.width(4)
mike.penup()
mike.goto(100, 100)
mike.forward(50)
mike.left(50)
mike.right(50)
mike.forward(50)
mike.right(5)
mike.circle(200)
mike.penup()
mike.goto(10, 20)
mike.right(50)
mike.forward(30)
mike.left(40)
mike.forward(10)
mike.right(10)
mike.forward(50)
mike.goto(50, 50)
mike.left(20)
mike.forward(40)
mike.left(20)
mike.penup()
mike.goto(10, 10)
mike.left(40)
mike.right(22)
mike.right(45)
mike.forward(13)

mike.color("lightblue")
mike.begin_fill()
# Large circle
mike.circle(100)
mike.end_fill()
mike.penup()
mike.goto(0, 200)
mike.begin_fill()
# Medium Circle
mike.circle(80)
mike.end_fill()
mike.goto(0, 360)
mike.begin_fill()
# Smallest circle
mike.circle(50)
mike.end_fill()
mike.goto(-25, 420)
mike.shapesize(1)
mike.color("black")
mike.shape("circle")
# Face
mike.stamp()
mike.goto(25, 420)
mike.stamp()
mike.goto(0, 400)
mike.stamp()
# Buttons
mike.goto(0, 340)
mike.stamp()
mike.goto(0, 300)
mike.stamp()
mike.goto(0, 260)
mike.stamp()


def make_cookies(x: int, y: int):
    # Cookie Making
    # Set the colour of our choco chip cookie
    mike.color("brown")
    # Draw a circle to represent our cookie
    mike.shapesize(1)
    mike.pu()
    mike.setheading(0)  # mike points east
    mike.goto(-5 + x, -30 + y)
    mike.pd()
    mike.circle(30)
    # Put a chocolate chip at the top-right
    mike.pu()
    mike.goto(10 + x, 10 + y)
    mike.stamp()
    # Put a chocolate chip at the bottom-right
    mike.goto(10 + x, -10 + y)
    mike.stamp()
    # Put a choco chip at the bottom-left
    mike.goto(-10 + x, -10 + y)
    mike.stamp()
    # Choco chip at the top-left
    mike.goto(-10 + x, 10 + y)
    mike.stamp()
    # Chocolate chip in the middle
    mike.goto(0 + x, 0 + y)
    mike.stamp()


# make cookies randomly on the screen
# make 500 of them
for _ in range(500):
    x = random.randrange(-500, 500)
    y = random.randrange(-500, 500)
    mike.speed(0)
    make_cookies(x, y)

window.exitonclick()
