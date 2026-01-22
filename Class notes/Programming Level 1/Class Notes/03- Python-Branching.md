# Branching 

23 September


## `if`

Branching is a concept in computer science that allows us to write code that has "two or more different outcomes".

This is the "grammar" of the `if` expression 
```python
if <statement>:
    <code block - line 1>
	<...>
	<code block - line n>
```

Example:
```python
user_name = "Ian Poon"
if user_name == "Ian Poon":
    print("Access granted.")
	print("You can see all the secret information.")
```

## `elif and else`

```python
user_name = "Ian Poon"
if user_name == "Ian Poon":
    print("Access granted.")
	print("You can see all the secret information.")
elif user_name == "Peashooter"
    print("Grows in Crazy Dave' lawn. ")
	
```

## Booleans

> Asking my Computer Science nerd friends.
> "Do you want pizza or fries?"
> All of them replied.
> "Yes!"

**Booleans** are a type of data in Python, binary and are either `True` or `False`

```python
is_sunny = True

if is_sunny! 
  print("You should probably wear sunscreen.")
else:
    print("Maybe you should bring suncreen!")
	
```

## `or`

`or`can be used to join two or more statements together.
`or`is true if  and only if at least one statement is **True**.

```python
food_to_eat_one = "Pizza"
food_to_eat_one = "Fries"

if food_to_eat_one == "Pizza" or
food_to_eat_two == "Fries":
	print("We're going to eat pizza or fries.")
else:
	print("We're going to eat pizza and fries.")
	
```


## `And`
`and`is true if and only if **both**  statements are True

```python
x = "cats"

y = "dogs"

if x == "cats" and y == "dogs":
	print("IT is raining cats and dogs.")
else:
	print("We have either a cat or a dog or neither.")
	
```

```python
want_cookies = True
want_chips = True

if want_cookies and want_chips:
    print("You get both!")    
else:
    print("You get none.")
```

