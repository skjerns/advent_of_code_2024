# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:11:10 2024

@author: Simon
"""
import re
import os
from aoc import get_input, get_lines, get_matrix
import stimer
import numpy as np

day = os.path.basename(__file__)[-5:-3]

matrix = get_matrix(day)

# with open('C:/Users/Simon/Desktop/day6inputchris.txt', 'r') as f:
#     lines = f.readlines()

# lines = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...'''.split('\n')
# matrix = np.array([list(line.strip()) for line in lines])

# convert matrix to int
matrix[matrix=='.'] = 0
matrix[matrix=='#'] = 9
matrix[matrix=='^'] = 1
matrix = matrix.astype(int)
matrix[matrix==9]=-1

lookup = {1: np.array([-1, +0]),
          2: np.array([+0, +1]),
          3: np.array([+1, +0]),
          4: np.array([+0, -1]),
          }

turns = {1: 2,
         2: 3,
         3: 4,
         4: 1,
         }

#%% part 1

start = np.array(list(zip(*np.where(matrix==1))))[0]

m = matrix.copy()
pos = start.copy()
curr_dir = 1
x=1
while True:
    step = lookup[curr_dir]
    next_pos = (pos+step)
    if any(next_pos<0) or any(next_pos>=m.shape):
        # we escaped! so no loop
        break
    # in python we don't check, we do and ask for forgiveness if it fails
    try:
        in_front = m[*(pos+step)]
        # either turn or walk
        if in_front==-1:
            curr_dir = turns[curr_dir] # turn right
            continue
        else:  # no turn? walk
            pos += step
    except IndexError:
        m[*pos] = x  # last state must also be marked
        break
    m[*pos] = x  # mark state as visited


print((m>0).sum())

# 5318 christophs result
# asd
#%%
from tqdm import tqdm
def isloop(m2):
    pos = start.copy()
    curr_dir = 1
    visited = set()

    while True:



        state = (pos[0], pos[1], curr_dir)
        if state in visited:
            # We've been here before with the same facing direction; it's a loop
            return True
        visited.add(state)

        # if we have been here 4 times or more, it means we have a loop
        # if m2[*pos] > 4:
        #     return True

        # first check where we need to go
        step = lookup[curr_dir]
        next_pos = (pos+step)

        # no negative indexing allowed. I'm not sure why this does not happen
        # in the base case, but here it seems to happen.
        if any(next_pos<0) or any(next_pos>=m.shape):
            # we escaped! so no loop
            return False
        # in python we don't check, we just do and
        # ask for forgiveness if it fails
        try:
            # see what is in front of us, if obstacle, turn right
            if m2[*next_pos]==-1:
                curr_dir = turns[curr_dir] # turn right
                continue  # check everything again
            else:
                # we didn't turn, so lets walk a step!
                pos += step
        except IndexError:
            # We escaped, out of bounds!! no loop
            # never have I been so happy to have an Error
            return False



n_loops = 0
m[m>1] = 1
m[*start] = 0  # mark the starting location as non "obstacleable"

# run through all positions at which the guard walks past and put an obstacle
for i, walked in enumerate(tqdm(list(zip(*np.where(m==1))))):
    m2 = matrix.copy()

    # place obstacle at that position
    m2[*walked] = -1
    # check if he is getting into a loop
    loop =  isloop(m2)

    n_loops += loop

print('\n n loops', n_loops)

# 1947 too high
# 1518 not right
# 1516 is correct, but why?! I will not cheat, need to find mistake first
