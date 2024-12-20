# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:52:23 2024

@author: Simon
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:46:54 2024

@author: Simon
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 17:16:37 2024

@author: Simon
"""
import os
from aoc import get_input, get_lines, get_matrix, print_matrix
import aoc
import stimer
import numpy as np
import itertools
from operator import add, mul
from tqdm import tqdm
import matplotlib.pyplot as plt

day = os.path.basename(__file__)[-5:-3]
lines, instructions = get_input(day).split('\n\n')

# ### test input
# lines, instructions  = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# lines, instructions = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".split('\n\n')

# <^^>>>vv<v>>v<<""".split('\n\n')

matrix = aoc.lines2matrix(lines.split('\n'))

instructions = instructions.replace('\n', '')

#%% part 1

start = np.where(matrix=='@')

wall = '#'
box = 'O'
free = '.'
bot = '@'

pos = np.array(list(zip(*start)))[0]
for m in instructions:
    # print(f'{m=}')
    # print_matrix(matrix)
    # input()

    delta = aoc.directions[m]
    next_pos = pos + delta

    next_item = matrix[*next_pos]
    # if next item is free, walk there
    if next_item == free:
        matrix[*pos] = free
        matrix[*next_pos] = bot
        pos = next_pos
        print('free, go!')
        continue

    # if step would reach a wall, ignore this move
    if next_item == wall:
        print('wall, stop')
        continue

    # seems like it is a box, so check if we can shift it
    # we actually move the first box to the first free position,
    # and dont shift the entire row
    box_pos = next_pos.copy()
    while True:
        next_pos = next_pos+delta
        next_item = matrix[*next_pos]

        # another box, keep shifting
        if next_item == box:
            continue
        # that means there was no space to move the box!
        if next_item == wall:
            # pos remains the same
            print('no space for box shift')
            break
        if next_item == free:
            matrix[*box_pos] = free
            matrix[*next_pos] = box
            matrix[*pos] = free
            matrix[*pos+delta] = bot
            pos = pos+delta
            print(f'shift box from {box_pos} to {next_pos}')
            break
    # asd

boxes = np.array(list(zip(*np.where(matrix=='O'))))

print('sum is', np.sum(boxes[:, 0]*100 + boxes[:, 1]))


#%% part 2

# ohhhh this is not difficult, but tedious. might do later.
