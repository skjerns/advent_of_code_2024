# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:24:04 2024

@author: Simon
"""

import os
from aoc import get_input, get_lines, get_matrix, print_matrix
import stimer
import numpy as np
import itertools
from operator import add, mul
from tqdm import tqdm

day = os.path.basename(__file__)[-5:-3]

lines = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".split('\n')

landscape = get_matrix(day, dtype=int)


# landscape = np.array([[int(c) for c in line] for line in lines])

#%% day1
with stimer:
    starts = np.array(list(zip(*np.where(landscape==0))))
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

    def is_ending(pos):

        if (curr_height:=landscape[*pos]) == 9:  # := walrus operator , love it!
            return {tuple(pos)}
        score = set()
        for d in directions:
            step = pos+d
            if any(step<0) or any(step>=landscape.shape):
                continue
            next_height = landscape[*step]
            if next_height == curr_height+1:
                score |= is_ending(step)
        return score

    score = 0
    for start in starts:
        # print(is_ending(start))
        score += len(is_ending(start))

    print(score)



    #%% day2

    starts = np.array(list(zip(*np.where(landscape==0))))
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

    def is_ending(pos):

        if (curr_height:=landscape[*pos]) == 9:  # := walrus operator , love it!
            return True
        score = 0
        for d in directions:
            step = pos+d
            if any(step<0) or any(step>=landscape.shape):
                continue
            next_height = landscape[*step]
            if next_height == curr_height+1:
                score += is_ending(step)
        return score

    score = 0
    for start in starts:
        # print(is_ending(start))
        score += is_ending(start)

    print(score)
