# Make Cookies
# Ian Poon


import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

# Set up turtle
mike = turtle.Turtle()
mike.color("saddlebrown")  # Use a realistic brown color
mike.shape("circle")
mike.shapesize(0.5)  # Make the chips smaller
mike.penup()

# Draw cookie (larger circle for the cookie base)
cookie = turtle.Turtle()
cookie.color("peru")  # Cookie dough color
cookie.pensize(3)
cookie.penup()
cookie.goto(0, -50)  # Center the cookie
cookie.pendown()
cookie.begin_fill()
cookie.circle(60)  # Cookie radius
cookie.end_fill()

# Chocolate chip positions (relative to cookie center)
chip_positions = [
    (20, 30),  # top-right
    (25, -20),  # bottom-right
    (-25, -20),  # bottom-left
    (-20, 30),  # top-left
    (0, 0),  # center
]

# Stamp chocolate chips
for x, y in chip_positions:
    mike.goto(x, y)
    mike.stamp()

# Hide turtles
mike.hideturtle()
cookie.hideturtle()

# Keep window open
turtle.done()
