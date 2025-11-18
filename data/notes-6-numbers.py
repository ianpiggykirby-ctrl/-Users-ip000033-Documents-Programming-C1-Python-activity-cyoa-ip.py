# Notes - Number
# 6 November
# Ian Poon


def vote_listed_choices():
    """Display all voting choices Users vote for their choice Results with be printed"""

    CHOICES = ["A. CoCo", "B. Chatime", "C. BUBBLE WAFFEL", "D. CHAYAN"]
    NUM_VOTERS = 5
    # Initialize vote counters
    coco = 0
    chatime = 0
    bubble_waffel = 0
    chayan = 0

    for _ in range(NUM_VOTERS):
        # Show all the bbt choices
        print("Vote for your favourite from the list.")
        print("Give the letter of your choice.")
        for choice in CHOICES:
            print(choice)

        # Ask the user for their choice.
        vote = input("Your vote: ").lower().strip(",.?!")

        if vote == "a":
            coco += 1
        elif vote == "b":
            chatime += 1
        elif vote == "c":
            bubble_waffel += 1
        elif vote == "d":
            chayan += 1

        total_votes = coco + chatime + bubble_waffel + chayan

        print("No votes recorded.")

    # Give some raw scores
    # Show the scores of coco, ..., etc.
    print(f"CoCo votes: {coco}")
    print(f"Chatime votes: {chatime}")
    print(f"BUBBLE WAFFEL votes: {bubble_waffel}")
    print(f"chayan votes: {chayan}")
    # Give score as a percentage
    coco_percentage = coco / (coco + chatime + bubble_waffel + chayan)
    print(f"CoCo Percentage: {coco_percentage * 100}%")
    chatime_percentage = chatime / (coco + chatime + bubble_waffel + chayan)
    print(f"Chatime Percentage: {chatime_percentage * 100}%")
    bubble_waffel_percentage = bubble_waffel / (coco + chatime + bubble_waffel + chayan)
    print(f"Bubble Waffel Percentage: {bubble_waffel_percentage * 100}%")
    chayan_percentage = chayan / (coco + chatime + bubble_waffel + chayan)
    print(f"chayan Percentage: {chayan_percentage * 100}%")


# Version 2


# Ask the user what their fave
def chip_rater():
    """Help gather data about chip crispness and quality."""
    # Create a list of questions
    questions = [
        "How crispy is the chip out of 5? 1 is mushy, 5 is super crispy.",
        "How would you rate the taste out of 5? 1 is this is the worst thing that you ever taste, 5 is this is the best thing that you ever taste.",
        "How fresh would you rate the chips out of 5? 1 is not fresh, 5 is super fresh.",
    ]

    # Rating total
    total = 0

    # Give user instructions
    print("Take one chip from the bag.")
    print("Eat it mindfully.")
    print("Give your rating.")
    # Ask the user questions
    for question in questions:
        print(question)
        # For each question, get their rating
        # out of five
        rating = int(input("Your rating: ").strip(",.?!"))
        # Update total
        total += rating
    # Print the average rating out of five
    average = total / len(questions)

    print(f"the average rating for this chip is: {average}.")


def main():
    # vote_listed_choices()
    chip_rater()


if __name__ == "__main__":
    main()
