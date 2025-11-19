import time
import os
import sys


# Choose your Own Adventure
# Ethan Lu
# September 24, 2025
# Choose your own adventure solely focusing on
# using variables and branching/conditionals
def restart_program():
    """Restarts the current program."""
    python = sys.executable
    os.execv(python, ["python"] + sys.argv)


def game():
    clarity = 0  # represents mental stabiity and self awareness


# trust tracks relationships and cooperation
trustEcho = 0
trustMarris = 0
trustMirror = 0
trustRyne = 0
fracture = 0  # represents instability, paradox risk, memory corruption
# Introduction
time.sleep(0.5)
print("You wake up in a sterile white room with no windows.")
time.sleep(0.5)
print("A headache attacks you while a synthetic voice crackles to life.")
time.sleep(0.5)
print('"Subject 12. Consciousness upload successful. Welcome to Fracture Point."')
time.sleep(0.5)
print(
    'You see two doors infront of you: on the left, a door labeled "MEMORY CORE", and on the right, "EXTRACTION BAY".'
)
time.sleep(0.5)
print('"Time is breaking. Choose wisely."')

# Problem
choiceOne = input(
    'Type 1 to open the left door marked "MEMORY CORE".\nType 2 to open the right door marked "EXTRACTION BAY".'
)
while choiceOne != "1" and choiceOne != "2":
    print("Please type 1 or 2.")
    choiceOne = input(
        'Type 1 to open the left door marked "MEMORY CORE".\nType 2 to open the right door marked "EXTRACTION BAY".'
    )
# Rising Action

if choiceOne == "1":
    print(
        "You enter a room filled with floating orbs. Each one shows glimpses of your possible paths—a soldier, a scientist, a fugitive. One orb pulses stronger than the rest."
    )
    choiceOneBranch = input(
        "Do you: \n1. Touch the pulsing orb \n2. Break the orb \n3. Ignore all orbs and leave"
    )
    if choiceOneBranch == "1":
        print(
            "You touch the orb and you suddenly get teleported to a lab. You become a well-respected scientist there and become the head scientist of the lab experimenting with multiple timelines. "
        )
        print('You have unlocked the ending: "The Renegade Scientist"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    elif choiceOneBranch == "2":
        print(
            "You erased your past identity and you walk onto a path even you don't know where it leads. "
        )
        print('You have unlocked the ending: "My Own Path"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    elif choiceOneBranch == "3":
        print("You ignored all the orbs and left, remaining a black state ")
        print('You have unlocked the ending: "My Own Path"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    else:
        print('Invalid input. Please enter "YES" or "NO".')
        invalid = input("Type anything to restart")
        restart_program()

elif choiceOne == "2":
    print(
        "You're greeted by a woman in a lab coat who calls you \"Commander Vale\"—but you're not sure if she’s lying."
    )
    choiceTwoBranch = input(
        "Do you: \n1. Pretend to be Commander Vale \n2. Admit you don't remember \n3. Attack her first"
    )
    if choiceTwoBranch == "1":
        print(
            "You gain her trust, and you unlock base access, leading to you becoming a scientist working there"
        )
        print('You have unlocked the ending: "The Scientist"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    elif choiceTwoBranch == "2":
        print(
            "She quickly runs and activates a failsafe, and you are arrested in seconds, and then placed into a jail for who knows how long."
        )
        print('You have unlocked the ending: "Prisoner of Time"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    elif choiceTwoBranch == "3":
        print(
            "You attack her and become violent, becoming an nounstable person who walks a dangerous path where you are hunted."
        )
        print('You have unlocked the ending: "Fractured Mind"')
        restart = input("Press r to restart game.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    else:
        print('Invalid input. Please enter "YES" or "NO".')
        invalid = input("Type anything to restart")
        restart_program()
else:
    print('Invalid input. Please enter "YES" or "NO".')
    invalid = input("Type anything to restart")
    restart_program()

while True:
    start = input("Start Game? Type YES/NO ").lower()
    if start == "yes":
        game()
    elif start == "no":
        restart = input("Game not started. Press r to restart.")
        if restart == "r":
            print("Restarting program...")
            restart_program()
    else:
        print('Invalid input. Please enter "YES" or "NO".')
        invalid = input("Press r to restart.")
        if invalid == "r":
            print("Restarting program...")
            restart_program()


# Climax

# Resolution
