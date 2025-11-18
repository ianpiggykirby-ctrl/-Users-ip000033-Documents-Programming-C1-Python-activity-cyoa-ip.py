# Notes - Introduction
# 16 September
# Ian Poon

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#          MeGPT

# 1. Greet the user with apredetermined statment
greeting = "Hello! I am a chatbot."

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT.")
print("I'm not like the other guy.")
print("I am completely deterministic")

# 3. Wow the user with some maths
print("I bet you don't figure it out what is 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8*8}.")

print("What is pi squared?")
print("I am smart, I can do it too.")
print(f"It is {3.14159265359 ** 2}.")

# 4. Make the bot crash out a little bit.
print("The quick brawn fox jump over the lazy dog." * 10)

# 5. Get the name of the user, store it, and use it
user_name = input("What's your name? ")
print(f"It's a nice to meet you, {user_name}! ")

# ...

# 8. See IF the user is someone specific
# 8a. If they're someone specific, tell them a secret

if user_name == "Ian Poon":
 print("I know you hate Super Monkey Ball.")
 print("But I won't tell anyone about that.")


user_name = "Ian Poon"
if user_name == "Ian Poon":
    print("Access granted.")
    print("You can see all the secret information.")
elif user_name == "Peashooter":
    print("Grows in Crazy Dave' lawn.")
    print("I will kill all those zombies!")
