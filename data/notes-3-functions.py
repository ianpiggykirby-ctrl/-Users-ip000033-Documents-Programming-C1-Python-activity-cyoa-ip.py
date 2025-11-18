# Notes - Function
# 8 October
# Ian Poon

# function to print "hello" to the console
def say_hello():
    print("hello")


# function to print a personalized hello
def say_hello_personal(name: str):
    print(f"hello {name}!")


say_hello_personal("Oscar")
say_hello_personal("Peashooter")


def normalized_input():
    """Clean up the user's input"""
    output = input()
    output = output.strip(",.?! ").lower()
    return output


# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
    print("You should bring your unbralla.")


def some_fun():
    print("hello!")


def some_fun_return() -> str:
    print("hello!")
    return "gummy worm"


return_val = some_fun()

print(return_val)

return_val = some_fun_return()

print(return_val)


# our example from notes-3-functions.py
# default name -> "Tiger"
def say_hello_personal(name="Tiger"):
    print(f"hello {name}")


say_hello_personal("Peashooter")
say_hello_personal()
