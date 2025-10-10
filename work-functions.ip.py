# Exercise - Functions
# 10 October
# Ian Poon


def create_mood_message():
    def create_mood_message(name, mood="neutral"):
        if mood == "happy":
            return f"Hey {name}, great to see you smiling!"
        elif mood == "sad":
            return f"I hope your day gets better, {name}."
        elif mood == "neutral":
            return f"Sometimes you have average days, {name}."
        else:
            return f"Hi {name}, hope you're having a good day. "


...


def average(num_one, num_two, num_three):
    """
    Calculate the average of at least three numbers.
    Additional numbers can be passed as optional arguments.

    Parameters:
        num_one (float or int): First number.
        num_two (float or int): Second number.
        num_three (float or int): Third number.
        *args (float or int): Optional additional numbers.

    Returns:
        float: The average of all the numbers.
    """

    return (num_one + num_two + num_three) / 3


result = average(10, 20, 30)
print(result)  # Output: 20.0
print(result)  # Output 30.0
