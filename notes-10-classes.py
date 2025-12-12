# Classes and Objects
# Author: Ian
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        """Constructor"""
        self.name = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        print("A pokemon is born!")
        # 1 in 4096
        if random.randint(0, 4096):
            self.is_shiny = False
        else:
            self.is_shiny = True
            print("This pokemon is shiny!✨✨✨")


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()
    # Access the pokemon's properties
    print("Pokemon name:", pokemon_one.name)
    # Change the pokemon's properties
    pokemon_one.name = "Mew"
    print("Pokemon name:", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    # Check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They're the same.")
    else:
        print("They're individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")

    for _ in range(100):
        Pokemon()
