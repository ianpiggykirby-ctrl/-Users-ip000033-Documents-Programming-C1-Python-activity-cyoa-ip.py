# Work - dataanalysis
# Ian Poon
# 21 November

# Analyse the data provided in class


def main():
    # do your work in here
    path = "/Users/teacher/Documents/fave_food.csv"
    file = open(path)
    # print the first line of the file
    header_row = file.readline()

    # Get information about the fave fried chicken restaurant
    churchs_texas_chicken = 0
    shawns_chicken = 0
    chicko_chicken = 0
    # Fave pizza shop
    pizza_hut = 0
    uncle_fatihs = 0
    little_caesars = 0

    for line in file:
        # fave pizza is in column 5 (4th ind)
        # a line is a string
        # convert the string to a list
        # split the line wherever a , is
        info = line.split(",")
        fave_fried_chicken_restaurant = info[3]
        fave_pizza_shop = info[3]

        if fave_fried_chicken_restaurant == "churchs_texas_chicken":
            churchs_texas_chicken += 1
        elif fave_fried_chicken_restaurant == "shawns_chicken":
            shawns_chicken += 1
        elif fave_fried_chicken_restaurant == "chicko_chicken":
            chicko_chicken += 1

        if fave_pizza_shop == "pizza_hut":
            pizza_hut += 1
        elif fave_pizza_shop == "uncle_fatihs":
            uncle_fatihs += 1
        elif fave_pizza_shop == "little_caesars":
            little_caesars += 1

    # Display Results
    print(f"churchs texas chicken votes: {churchs_texas_chicken}")
    print(f"shawns chicken votes: {shawns_chicken}")
    print(f"chicko chicken votes: {chicko_chicken}")

    # Display the most popular pizza shop
    print(f"pizza hut votes: {pizza_hut}")
    print(f"uncle fatihs votes: {uncle_fatihs}")
    print(f"little caesars votes: {little_caesars}")

    # or create a new function and call it in here
    file.close()


if __name__ == "__main__":
    main()
