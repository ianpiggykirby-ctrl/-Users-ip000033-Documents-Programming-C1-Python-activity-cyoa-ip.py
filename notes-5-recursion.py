# Notes - Recursion
# 20 October
# Ian Poon

# Create a function that draws tree recursively

import turtle
import random

# set up the enviroment
wn = turtle.Screen()
t = turtle.Turtle()
t.left(90)  # point the turtle up
t.penup()
t.goto(0, -200)
t.color("brown")
t.width(10)
t.shape("arrow")  # leaf shape
t.speed("fastest")

# Create a directionary of leaf colours
LEAF_COLOURS = {
    "spring": "#efc3e6",
    "summer": "#1ff03f",
    "fall": "#d62828",
    "winter": "#a9d2d5",
}


def draw_tree(level: int, branch_length: float):
    """Draw a tree recursively at a given level
    level - the levels of branches
    branch_length - length of branch in pixels
    """
    t.pendown()

    # If the level is greater than zero
    if level > 0:
        # 1. Move forward branch_length
        t.forward(branch_length)
        # 2. Turn left and draw a "smaller tree"
        t.left(47)
        draw_tree(level - 1, branch_length * 0.8)
        # 3. Turn right and draw a "smaller tree"
        t.right(94)
        draw_tree(level - 1, branch_length * 0.8)
        # 4. Return to the beginning
        t.left(47)
        t.backward(branch_length)

        t.forward(branch_length)

        # Save current position and heading to return after each branch
        position = t.position()
        heading = t.heading()

        # Random angle and length multiplier for variation
        angle = random.randint(20, 45)
        shrink = random.uniform(0.7, 0.85)
        new_length = branch_length * shrink

        # Left branch
        t.left(angle)
        draw_tree(level - 1, new_length)

        # Reset position and heading before right branch
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()

        # Right branch
        t.right(angle)
        draw_tree(level - 1, new_length)

        # Return to base of this branch
        t.penup()
        t.setposition(position)
        t.setheading(heading)
        t.pendown()
        t.backward(branch_length)
    else:
        # create a leaf
        t.color(LEAF_COLOURS["summer"])
        t.stamp()
        t.color("brown")
        return


def factorial(num: int) -> int:
    """Calculate the factorial of the given num recursively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


def fibonacci(num: int) -> int:
    """Returns the nth fibonacci number calculated recursively"""
    if num <= 2:
        return (num - 1) + fibonacci(num - 2)
    else:
        return 1


t.speed(0)
draw_tree(4, 250)

print(factorial(1))  # 1
print(factorial(4))  # 24
print(factorial(101))  # SOME BIG NUM

print("\nFibonacci tests:")
print(fibonacci(6))  # 8
print(fibonacci(10))  # 55

wn.exitonclick()
