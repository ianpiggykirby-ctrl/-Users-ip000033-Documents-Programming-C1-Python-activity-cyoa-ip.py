# Choose Your Own Adventure – Mini Story
# 24 September
# Ian Poon

# Variables: storing and updating information
# Conditionals: using if, elif, and else to branch the story

# Introduction
greeting = "Hello, who are you?"

print(greeting)

print("My name is Herbert.")
print("I am finding a partner for this adventure.")

user_name = input("What's your name?")
print(f"Nice to meet you, {user_name}!")

user_name = input("Do you want to join our adventure? (Yes/No): ").strip().lower()

# Adventure Summary
if user_name == "yes":
    print("\nYou: Yes, I join!")
    print("Herbert: Great! Follow me, I’m going to show you our base first.\n")
    print(
        "The base is a cozy wooden cabin surrounded by tall pine trees, with the smell of fresh pine and campfire in the air."
    )
    print(
        "Herbert: We have two missions today. One is to explore the mysterious cave nearby, the other is to scout the forest for resources."
    )

    inventory = []

    mission = (
        input("\nWhich mission do you want to take? (cave/forest): ").strip().lower()
    )
    if mission == "cave":
        print("\nHerbert: The cave is dark and full of unknown dangers. Stay close!")
        print("You enter the cave, hearing dripping water and distant echoes.")

        print(
            "Suddenly, you spot a glowing crystal deep inside. Will you take it or leave it?"
        )
        print("I will also provide the gummy flash light for you as well.")
        inventory.append("Gummy Flashlight")  # Add flashlight to inventory

        choice = input("Take the crystal or leave it? (take/leave): ").strip().lower()
        if choice == "take":
            print("\nYou carefully grab the crystal. It pulses with energy!")
            inventory.append("Glowing Crystal")  # Add crystal
            print("Herbert: Wow! This might be useful later on. Let's head back.")
        else:
            print("\nYou decide not to risk it and leave the crystal alone.")
            print("Herbert: Smart choice. Some treasures are traps.")
            print("Herbert: Let's go back.")

    elif mission == "forest":
        print(
            "\nHerbert: The forest is dense and full of wildlife. Keep your eyes open!"
        )
        print("You start scouting and find berries, herbs, and signs of a nearby deer.")

        choice = (
            input(
                "Do you want to try hunting the deer or just gather herbs? (hunt/gather): "
            )
            .strip()
            .lower()
        )

        if choice == "hunt":
            print("\nYou prepare your bow and quietly approach the deer.")
            inventory.append("Venison Meat")
            print("Herbert: Good luck! A successful hunt will feed us for days.")
        else:
            print("\nYou gather herbs and berries carefully.")
            print("Herbert: These will help us heal if anyone gets hurt. Wise choice.")
    else:
        print(
            "\nHerbert: That’s not a mission we have today, but feel free to rest here."
        )

        inventory = [
            "Glowing Crystal",
            "Venison Meat",
            "Healing Herbs",
            "Gummy Flashlight",
        ]

        # Ending

    if inventory:
        print("You returned with:")
        for item in inventory:
            print(f"-{item}")

    else:
        print("You returned with nothing, but the experience itself is valuable!")

    if "Glowing Crystal" in inventory:
        print("Herbert: That glowing crystal may hold secrets for future adventures.")
    if "Venison Meat" in inventory:
        print("Herbert: Great hunt! This will keep us well fed.")
    if "Healing Herbs" in inventory:
        print("Herbert: Those herbs will surely help if we get injured.")
    if "Gummy Flashlight" in inventory:
        print("Herbert: The gummy flashlight is a handy tool for dark places.")

    print(
        "\nHerbert: Thanks for joining me today, brave adventurer. Rest well and prepare for the challenges ahead!"
    )

else:
    print("\nYou: No, I’m not ready for this adventure.")
    print(
        "Herbert: I understand. Sometimes the greatest adventure is knowing when to wait."
    )
    print("Maybe next time, friend.")
