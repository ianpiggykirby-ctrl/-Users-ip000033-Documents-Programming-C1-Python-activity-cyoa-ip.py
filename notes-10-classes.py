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

    def dance(self):
        """Make your pokemon dance"""
        print(f"{self.name} is dancing")

    def find_something(self, how_many_things=1) -> str:
        """Send pokemon to find something

        Returns:
            a list of str representing what it found"""
        things = [
            "pinap berry",
            "razz berry",
            "nanab berry",
            "golden razz berry",
            "leftovers",
            "moon stone",
        ]
        found_things = []

        for _ in range(how_many_things):
            found_things.append(random.choice(things))

        return found_things


class Squirtle(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"
        self.level = 1
        self.has_sunglasses = True

    def water_gun(self):
        """Squirtle shoots water out of its mouth"""
        print(f"{self.name} used water gun!")

    def bubble_beam(self):
        """Squirtle shoots bubble beam out of its mouth"""
        print(f"{self.name} used bubble beam!")


class Mewtwo(Pokemon):
    def __init__(self):
        # call the constructor of the parent class
        super().__init__()
        self.name = "Mewtwo"
        self.type = "Psychic"
        self.species = "Mewtwo"
        self.level = 1
        self.age = 0


class Snorlax(Pokemon):
    def __init__(self):
        super().__init__()
        self.name = "Snorlax"
        self.species = "Snorlax"
        self.type = "normal"
        self.level = 5

    def gluttony(self):
        """Snorlax's hidden ability which allows it to eat held berries at half health"""
        print(f"{self.name} used gluttony!")
        print(f"{self.name} from half health heal into full health!")

    def stats(self):
        """Display the states of the pokemon"""
        print("--------------------------------")
        print(f"    Name: {self.name}")
        print(f"    Type:  {self.type}")
        print(f"    Level: {self.level}")
        print(f"    Age:    {self.age}")
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

        print(f"{pokemon_one.name} found these things: {pokemon_one.find_something()}")

        # Tell our pokemon to talk
        pokemon_one.talk()
        pokemon_two.talk()
        # Display stats of pokemon_one
        pokemon_one.stats()
        pokemon_two.stats()
        # Make your pokemon dance
        pokemon_one.dance()
        pokemon_two.dance()

        squirtle_one = Squirtle()
        # display stats of Squirtle()
        squirtle_one.stats()
        # use .water_gun()
        squirtle_one.water_gun()
        # use bubble_beam()
        squirtle_one.bubble_beam()
        # use .talk()
        squirtle_one.talk()

        snorlax_one = Snorlax()
        snorlax_one.stats()
        # use .gluttony()
        snorlax_one.gluttony()
        # use .talk()
        snorlax_one.talk()

        # Create a Mewtwwo object
        pokemon_three = Mewtwo()
        pokemon_three.stats()
        pokemon_three.talk()
