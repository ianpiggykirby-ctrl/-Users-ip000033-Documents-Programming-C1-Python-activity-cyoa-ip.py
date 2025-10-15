# Notes - Loops
# 14 October
# Ian Poon

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
mike.stamp()
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


window.exitonclick()
