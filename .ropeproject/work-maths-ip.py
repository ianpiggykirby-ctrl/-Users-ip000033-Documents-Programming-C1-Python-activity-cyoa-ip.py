# Work - Math
# 13 November
# Ian Poon

print("Here's your food")
print("\n It looks so good!")
print("Yeah, so just try out to see if you like it or not.")
input("It the food good? (Yes/No): ").strip().lower()
print("Show your commend about the food!")


# Ask the user what their fave
def fish_and_chips_rating():
    """Rating the taste, quailty and the freshness of the fish and chips."""


questions = [
    """How the taste of the fish and chips out of 10? 1 is tasteless and nasty, 10 is super tasty and soft.""",
    """How is the quailty out of 10? 1 is messy, 10 is nice and neat.""",
    """How is the freshness out of 10? 1 is not fresh, 10 is super fresh.""",
]

# Rating Total
total = 0

print("Have a small bite of the meat of the fish.")
print("Eat it mindfully.")
print("Give your rating.")

for question in questions:
    print(question)

    rating = int(input("Your rating: ").strip(",.?!"))

    total += rating

    average = total / len(questions)

    print(f"the average rating for the fish and chips is: {average}.")
    print("Thanks for rate.")


def main():
    fish_and_chips_rating()


if __name__ == "__main__":
    main()
