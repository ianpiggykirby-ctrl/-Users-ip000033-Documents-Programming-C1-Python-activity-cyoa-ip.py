# Numbers and Operations

15 October 2025

## Data Types So Far

| Data Type     |  Name | Example | 
|  ---                  |  ---       |  ---       | 
| String            |   `str`|    `"Ian"` |
| boolean        | `bool` | `True` `False` |   
| **Interger**| `int`| `1` `2` `-100` |
| **Float** | `float` | `1.0` `-2.3` | 
| Dictionary | `dict` | `{"key": "val",}` |   

## Operators that work on numbers 
```Python
# Addition
print(5 + 3) # Output: 8

# Subtraction
print(10 - 4) # Output: 6

# Multiplication
print(2 * 6) # Output: 12

# Division (returns a float)
print(15 / 3) # Output: 5.0

# Floor Division (returns an integer, discarding the fractional part)
print(17 // 5) # Output: 3

# Modulus (returns the remainder of a division)
print(17 % 5) # Output: 2

# Exponentiation (raises the first number to the power of the second)
print(2 ** 4) # Output: 16

### Addition and Subtraction
```python
sum = 1 +1 # 2
diff = 10 -8 # 2
another_sum = 1 + 1.0 # 2.0
```

### Multiplication and Division
```python
product = 8 * 8  # 64
answer = 10 / 2  # 5
```

### Order of Operations
```python
# BEDMAS - Bracket, Exponents, Div/Mult, Add/Sub
answer = (2 + 3) * 4 +2 / 3 
```

### Cool Other Operations
```python
# Exponents
ans = 3 ** 2   # 9 
# Floor Division
ans = 10 // 3  # 3
# Modulo
ans = 2 / 2 # r0 
ans = 3 / 2 # r1
ans = 4 / 2 # r0
ans = 5 / 2 # r1 
# Increment, Decrement, Mult-rement, Divide-rememt
# Update the value of a variable
egg_count = 1
egg_count += 1      # raises the value of egg-count
egg_count -= 1      # decrease the value of egg-count
egg_count *= 1      # multiplies the value of egg-count 
egg_count /= 1      # divide the value of egg_count
```

## Loops Again
Recall:

```python
# Repeat something 10 times
for _ in range(10):
	print("This will be printed 10 times."
```

Iteraate over a "sequence" . 
```python
grocery_list = [
	"cucumbers",
	"eggs",
	"hot wheels",
	"moper"
]

# print out a pretty version of the list
for item in grocery_list:
	# Create a bulleted list and print it out
	bulleted_item = "* " + item
	separator = " ------ "
	print(bulleted_item)
	print(separator)
```
Output
```
* cucumbers
 ---------

* eggs
 ---------

* hot wheels
 ---------

* moper
 ---------
```
