# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 17:36:47 2024

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
matrix = get_matrix(day)

# matrix = aoc.lines2matrix("""#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################""".split('\n'))

#%% part 1

# we are going to do something dijkstra-like. At each point, we push
# the next possible moves to the global stack together with the current pos.
# then we sort the stack by the lowest resulting path.

start = list(zip(*np.where(matrix=='S')))[0]
ori = '>'


walk = 'w'
wall = '#'
end = 'E'

queue = [(start, ori, 0)]

explored = set()

add = lambda x, y: (x[0]+y[0], x[1]+y[1])

best_scores = []

while True:
    # whats the cheapest move we can make, besides a bad pickup line
    queue = sorted(queue, key=lambda x: x[2])

    cheapest_move = queue.pop(0)

    pos, ori, score = cheapest_move
    # print(f'cheapest move ({score}) {pos}: {ori=}')

    if (pos, ori) in explored:
        # some node has already reached this position with fewer steps
        continue

    # add that we have been here with the cheapest move possible
    explored.add((pos, ori))

    if matrix[*pos] == wall:
        # dead end, stop here
        continue

    if matrix[*pos] == end:
        # we have reached the end, wohoo
        print(f'final {score=}')
        break

    # add the options that are possible
    # A) keep orientation and walk
    queue.append((add(pos, aoc.step[ori]), ori, score + 1))
    # B) turn left
    queue.append((pos, aoc.turn_counter[ori], score + 1000))
    # C) turn right
    queue.append((pos, aoc.turn_clock[ori], score + 1000))
