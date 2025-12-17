# Classes and Objects
# Author: Ian
# 11 December 2025

import random


class Pokemon:
    def __init__(self):
        """Constructor"""
        self.name = ""
        self.species = ""
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

    def talk(self):
        """Hear what the pokemon has to say
        The pokemon says its species name"""
        print(f'{self.name} says, "{self.species}".')

    def stats(self):
        """Display the states of the pokemon"""
        print(f"----({self.species})-----------")
        print(f"    Name: {self.name}")
        print(f"    Type:  {self.type}")
        print(f"    Age:   {self.age}")
        print(f"    Level: {self.level}")
        print("--------------------------------")


if __name__ == "__main__":
    # Create a pokemon object
    pokemon_one = Pokemon()
    # Access the pokemon's properties
    print("Pokemon name:", pokemon_one.name)
    # Change the pokemon's properties
    pokemon_one.name = "Mew"
    pokemon_one.species = "Pikachu"
    print("Pokemon name:", pokemon_one.name)
    # Create another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    pokemon_two.species = "Pikachu"
    # Check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They're the same.")
    else:
        print("They're individual pokemon.")

    if type(pokemon_one) is Pokemon:
        print(f"{pokemon_one.name} is a Pokemon.")

        for _ in range(100):
            Pokemon()

        # Tell our pokemon to talk
        pokemon_one.talk()
        pokemon_two.talk()
        # Display stats of pokemon_one
        pokemon_one.stats()
        pokemon_two.stats()
