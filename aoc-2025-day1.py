# AOC DAY 1
# Author: Ian
# 1 December


def part_one():
    cur_location = 50
    zeroes = 0

    # read every line in the instructions
    with open("data/aoc-2025-day1.txt") as f:
        for line in f:
            # instruction example "R10" -> right 10
            direction = line[0]
            distance = int(line[1:])
            print(direction, distance)

            # if we go RIGHT -> add
            if direction == "R":
                cur_location += distance
            # if we go LEFT -> subtract
            else:
                cur_location -= distance
            # if we land on zero keep track of it
            # print(cur_location)

            if cur_location % 100 == 0:
                zeroes += 1
            # print how many times we landed on zero
            #
        print(zeroes)


if __name__ == "__main__":
    part_one()
