# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:22:44 2024

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

matrix = get_matrix(day)

# lines = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".split('\n')
# matrix = np.array([list(line.strip()) for line in lines])

#%% part 1

with stimer:
    antennas = np.unique(matrix[matrix!='.'])

    antinodes = set()
    m = matrix.copy()

    for antenna in antennas:
        coords = np.array(list(zip(*np.where(matrix==antenna))))
        for a1, a2 in itertools.combinations(coords, 2):
            # for
            diff = a1 - a2
            anti1 = a1 + diff
            anti2 = a2 - diff

            # out of bounds?
            if all(anti1>=0) and all(anti1<matrix.shape):
                if m[*anti1] == '.':
                    m[*anti1] = '#'
                    antinodes.add(tuple(anti1))

            if all(anti2>=0) and all(anti2<matrix.shape):
                if m[*anti2] == '.':
                    m[*anti2] = '#'
                antinodes.add(tuple(anti2))
        # asdf
        # asd
    print(f'{len(antinodes)=}')

    # 338 too high


    #%% part 2

    antennas = np.unique(matrix[matrix!='.'])

    antinodes = set()

    m = matrix.copy()

    for antenna in antennas:
        coords = np.array(list(zip(*np.where(matrix==antenna))))
        for a1, a2 in itertools.combinations(coords, 2):
            # for
            antinodes.add(tuple(a1))
            antinodes.add(tuple(a2))
            diff = a1 - a2

            anti1 = a1 + diff
            anti2 = a2 - diff

            # loop until out of bounds
            while all(anti1>=0) and all(anti1<matrix.shape):
                antinodes.add(tuple(anti1))
                if m[*anti1] == '.':
                    m[*anti1] = '#'
                anti1 = anti1 + diff

            while all(anti2>=0) and all(anti2<matrix.shape):
                antinodes.add(tuple(anti2))
                if m[*anti2] == '.':
                    m[*anti2] = '#'
                anti2 = anti2 - diff

            pass

    print(f'{len(antinodes)=}')
