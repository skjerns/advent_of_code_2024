# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:16:37 2024

@author: Simon
"""
import os
from aoc import get_input, get_lines, get_matrix, print_matrix
import stimer
import numpy as np
import itertools
from operator import add, mul
from tqdm import tqdm
import matplotlib.pyplot as plt

day = os.path.basename(__file__)[-5:-3]


matrix = get_matrix(day)

# lines = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE""".split('\n')

# lines = """AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA""".split('\n')

# matrix = np.array([[x for x in line] for line in lines])

matrix = np.vectorize(lambda x: ord(x) - ord('A') + 1)(matrix)

directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

#%% part 1
with stimer:
    from scipy.ndimage import label, binary_erosion
    # gardens =

    psum = 0

    for markers in np.unique(matrix):
        plots, n_labels = label(matrix==markers)
        for p in range(1, n_labels+1):
            plot = plots==p

            plot_coords = set(zip(*np.where(plot)))
            fences = 0
            for coord in plot_coords:
                for d in directions:
                    if not tuple(coord+d) in plot_coords:
                        fences += 1

            psum += fences * plot.sum()
            # print(psum)
            # perimeter(labels==l)
            # plt.imshow(plot)
            # plt.pause(0.1)
            # plt.waitforbuttonpress()
            # perimeter(plot)

    print(f'{psum=}')

    #%% part 2

    from scipy.ndimage import label, binary_erosion
    # gardens =

    psum = 0

    for markers in np.unique(matrix):
        plots, n_labels = label(matrix==markers)
        for p in range(1, n_labels+1):
            plot = plots==p

            plot_coords = set(zip(*np.where(plot)))
            fences = []
            for coord in plot_coords:
                for d in directions:
                    if not (fence:=tuple(coord+d)) in plot_coords:
                        fences += [tuple(coord+d*0.25)]

            # next we check which fences belong to the same segment
            # that means that they share either the X or Y coordinate
            fences_arr = np.array(list(fences))
            sides = 0
            # first look at all vertical edges
            fences_vert = fences_arr[((fences_arr[:,0]/0.5)%2).astype(bool)]
            for x in np.unique(fences_vert[:,0]):
                same_x = fences_vert[fences_vert[:, 0]==x]
                same_x.sort(axis=0)
                # how many discontinuations are there?
                diff = np.diff(same_x[:, 1])
                sides_add = (diff>1).sum() + 1
                sides += (diff>1).sum() + 1
                # print(f'{x=} {same_x=} {diff=} {sides_add=}')
                # input()

            fences_horiz = fences_arr[((fences_arr[:,1]/0.5)%2).astype(bool)]
            for y in np.unique(fences_horiz[:,1]):
                same_y = fences_horiz[fences_horiz[:, 1]==y]
                same_y.sort(axis=0)
                # how many discontinuations are there?
                diff = np.diff(same_y[:, 0])
                sides_add = (diff>1).sum() + 1
                sides += (diff>1).sum() + 1
                # print(f'{y=} {same_y=} {diff=} {sides_add=}')
                # input()
            # stop
            psum += sides * plot.sum()

    print(f'{psum=}')

    # 845490 too low
