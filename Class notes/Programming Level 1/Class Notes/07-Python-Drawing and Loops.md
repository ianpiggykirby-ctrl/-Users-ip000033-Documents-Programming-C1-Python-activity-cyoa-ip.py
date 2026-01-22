# Drawing and Loops
14 October 2025

## Turtles!

>Turtle is a library that helps us visually interact with Python code.
>To draw on the screen, we create turtles. Turtles will be a new **type** of data.

## Turtle Boilerplate

> **Boilerplate** is a code that is frequently copied and pasted.

 ```python
import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles


window.exitonclick()
```


## Turtle Methods

```python
mikey = turtle.Turtle()  # creates a turtle object

# change attributes
mikey.size()
mikey.color()
mikey.width()
mikey.penup()    # mikey.pu()
mikey.pendown()  # mikey.pd()
mikey.shape()

# actions
mikey.forward()  # mikey.backward()
mikey.left()     # mikey.right()
mikey.circle()
mikey.goto()
```

- ______.circle(radius: int)
- ______.goto(x: int, y:int) 

## Loops / Iteration

**Iteration** is a word that means repitition.

If we ever want to repeat code, we can use a couple of methods.

When we **know how many times** we want to repeat something, we use a `for` loop.

```python
# Print "Hello" 10 times
for _ in range(10):
	print("Hello")

# A for loop that uses a 'counter'
for counter in range(100):
	print(counter) # 0, 1, 2, ...., 99
```


## Functions and Turtles