# Turtle Artist
# Author: Ian Poon
# 28 October

import turtle

# A one-of-a-kind drawing
wn = turtle.Screen()
wn.bgcolor("black")
a = turtle.Turtle()
a.speed(10)


# Your code here
# Draw a star
def draw_star(size, color):
    """Draw a 5-pointed star of a given size."""
    a.color(color)
    a.pensize(5)
    a.begin_fill()
    for _ in range(5):
        a.forward(size)
        a.right(144)
    a.end_fill()


# Move turtle to a nice position (optional)
a.penup()
a.goto(-250, 150)
a.pendown()
draw_star(200, "yellow")  # <-- adjust size here to make it bigger or smaller

a.penup()
a.goto(200, 100)  # move to the right side
a.pendown()
draw_star(200, "red")

# --- Third star (Blue) ---
a.penup()
a.goto(-220, 350)
a.pendown()
draw_star(200, "blue")


# Draw a moon
def draw_moon(x, y, radius, color1="lightyellow", color2="black"):
    """Draw a crescent moon using two overlapping circles."""
    a.penup()
    a.goto(x, y)
    a.pendown()
    a.color(color1)
    a.begin_fill()
    a.circle(radius)
    a.end_fill()

    # Overlapping circle to create the crescent shape
    a.penup()
    a.goto(x + radius / 3, y)
    a.pendown()
    a.color(color2)
    a.begin_fill()
    a.circle(radius)
    a.end_fill()


# Move turtle to draw moon
draw_moon(200, 200, 80)  # position (x, y), radius


def factorial(num: int) -> int:
    """Calculate the factorial of the given num recursively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


def draw_house(x, y, size=100):
    """Draw a colorful house with roof, door, and window."""
    a.penup()
    a.goto(x, y)
    a.pendown()

    # Draw the square base
    a.color("orange")
    a.begin_fill()
    for _ in range(4):
        a.forward(size)
        a.left(90)
        a.end_fill()

    # Draw the roof
    a.color("red")
    a.begin_fill()
    a.goto(x, y + size)
    a.goto(x + size / 2, y + size * 1.5)
    a.goto(x + size, y + size)
    a.goto(x, y + size)
    a.end_fill()
    # Draw a door
    a.penup()
    a.goto(0, -100)
    a.pendown()
    a.begin_fill()
    a.color("brown")
    for _ in range(2):
        a.forward(20)
        a.left(90)
        a.forward(40)
        a.left(90)
    a.end_fill()

    # --- Chimney ---
    a.penup()
    a.goto(x + size * 0.7, y + size * 1.2)
    a.pendown()
    a.color("maroon")
    a.begin_fill()
    for _ in range(2):
        a.forward(size * 0.15)
        a.left(90)
        a.forward(size * 0.4)
        a.left(90)
    a.end_fill()

    # --- Left Window ---
    a.penup()
    a.goto(x + size * 0.15, y + size * 0.4)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()

    # --- Right Window ---
    a.penup()
    a.goto(x + size * 0.65, y + size * 0.4)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()

    # top left window
    a.penup()
    a.goto(x + size * 0.15, y + size * 0.7)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()

    # top right window
    a.penup()
    a.goto(x + size * 0.65, y + size * 0.7)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()

    # bottom left window
    a.penup()
    a.goto(x + size * 0.15, y + size * 0.1)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()

    # bottom right window
    a.penup()
    a.goto(x + size * 0.65, y + size * 0.1)
    a.pendown()
    a.color("skyblue")
    a.begin_fill()
    for _ in range(4):
        a.forward(size * 0.2)
        a.left(90)
    a.end_fill()


# Ground
a.penup()
a.goto(-400, -100)
a.pendown()
a.color("darkgreen")
a.begin_fill()
for _ in range(2):
    a.forward(800)
    a.right(90)
    a.forward(100)
    a.right(90)
a.end_fill()

draw_house(-50, -100, 120)

a.hideturtle()

print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(4))  # 24
print(factorial(12))  # 479001600
print(factorial(20))  # 2432902008176640000


wn.exitonclick()
