"""The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one.
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers
and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58
(middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
schematic?"""

import functools
from collections import defaultdict


def check_surroundings(mat, indexes):
    for num_row, num_col in indexes:
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = num_row + i
                col = num_col + j

                if 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                    char = mat[row][col]

                    if char != '.' and not (char.isdigit() or char.isalpha()) and char != '\n':

                        return True

    return False


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

            is_part_num = check_surroundings(mat, indexes)

            if is_part_num:
                numbers.append(int(number))

            j = i + 1

    return numbers


def main(filename):
    with open(filename) as f:
        mat = [list(line) for line in f]

        part_numbers = check_part_numbers(mat)

        print(sum(part_numbers))  # task1


main('engine.txt')
