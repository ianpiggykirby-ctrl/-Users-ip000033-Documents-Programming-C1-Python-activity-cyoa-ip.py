# Variables, Data, Input and Output 
16 September, 2025


## Designing Algorithms

> A step-by-step procedure for solving a problem or accomplishing some end.
> Merriam-Webster

An algorithm is like a recipe. If you follow the step, you should be able to solve the problem.

## Variables

We use variables to "store" values.
Variables have 2 parts: A **name** and a **value**.

Example:
```Ptyhon

Python

greeding = "Hello, I am a chatbot."


```



### Getting the Type

We can use the `type()` function to get the type of a variable.

`type()` is a function, just like `print()` is a *function*.

*Values*, in Python can be grouped based on their type, also known as a **data type**.

We'll look at **data types** more specifically in the next section.

### Variables names

When naming our variables, we need to follow Python's rules.

You can get the data type of any object by using the type() function:

Example
Print the data type of the variable x:
````
x = 5
print(type(x))

````


## Data

So far, we've used two **types of data**.

`"Mr. Ubial"` is an example of a **String**.

`32` is an example of a **Integer**.

`32.2` is a number, but more specifically it's an example of a **Float**.


### F-String 
This exists only in Python. The F in F-String stands for **format**. To create an f-string. you put an `F` in front of the opening quotation.

```python

name = f"Ian Poon"

```

```python
friends_name = "Mo Kam Cart (Oscar)"
print(f"Hey {friends_name}!")
```

You can use `{}` inside of an f-string to evaluate an expression.


## Input and Output 


Whenever we want to get information from the user, we can use the `input()` function. 

```python
# prompt the user for their name
# store their name in a variable
print("What is your name?")
user_name = input
```