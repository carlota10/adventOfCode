"""To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?"""

import re

thresholds = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def read_game(game):
    game_id = int(re.findall(r'\d+', game.split(':')[0])[0])
    rounds = game.split(':')[1].split(';')

    for ronda in rounds:
        colors = ronda.strip().split(',')

        for color in colors:
            cube = color.split()

            if int(cube[0]) > thresholds[cube[1]]:
                return 0

    return game_id


def main(filename):
    game_ids = []
    with open(filename) as f:
        for game in f:
            game_ids.append(read_game(game))
    print(sum(game_ids))


main('cubes.txt')
