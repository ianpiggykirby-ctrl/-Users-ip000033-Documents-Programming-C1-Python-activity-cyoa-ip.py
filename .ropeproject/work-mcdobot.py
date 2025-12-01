# McDoBot
# Author: Ian
# 6 October 2025

# Write a McDonald's bot that asks if you want fries with your meal.
# Call it  work-mcdobot.py.

# It should accept  Yes/yes  or  No/no  as inputs, and reply
# appropriately depending on the answer.

# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

print("Hello")
print("I am mcdobot")

choice = input("Would you like fries with your meal? (Yes/No) ").strip().lower()

if choice == "YES":
    print("Here's your meal with fries!")

if choice == "yes":
    print("Here's your meal with fries!")

elif choice == "no":
    print("Here's your meal without fries!")

else:
    print(f"Sorry. I don't understand asdfsdf?'.")
