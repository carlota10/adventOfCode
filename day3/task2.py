"""The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""

import functools
from collections import defaultdict


def check_surroundings(mat, indexes, number, asterisks_dict):
    for num_row, num_col in indexes:
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = num_row + i
                col = num_col + j

                if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                    char = mat[row][col]

                    if char != '.' and not (char.isdigit() or char.isalpha()) and char != '\n':
                        if char == "*":
                            asterisks_dict[f'{row, col}'].add(int(number))
                        return asterisks_dict

    return asterisks_dict


def check_part_numbers(mat):
    numbers = []
    asterisks_positions = defaultdict(set)
    for idx, row in enumerate(mat):
        j = 0

        while j < len(row):
            char = mat[idx][j]
            if char == '.' or not char.isdigit():
                j += 1
                continue

            indexes = []
            number = ''
            i = j

            while i < len(mat[0]):
                num = mat[idx][i]

                if num == '.' or not num.isdigit():
                    break
                indexes.append((idx, i))
                number += num
                i += 1

            asterisks_positions = check_surroundings(mat, indexes, number, asterisks_positions)

            j = i + 1

    return asterisks_positions


def multiply_sets(dictionary):
    result_dict = {}

    for key, value_set in dictionary.items():
        result_dict[key] = 0 if len(value_set) <= 1 else functools.reduce(lambda x, y: x * y, value_set)

    # for key, value_set in dictionary.items():
    # Check if the set is not empty
    # if len(value_set) > 1:
    #    result = 1
    #    for num in value_set:
    #        result *= num
    #    result_dict[key] = result
    # else:
    #    result_dict[key] = 0  # Set is empty, result is None

    return sum(result_dict.values())


def main(filename):
    with open(filename) as f:
        mat = [list(line) for line in f]

        positions = check_part_numbers(mat)

        print(multiply_sets(positions))  # task2


main('engine.txt')
