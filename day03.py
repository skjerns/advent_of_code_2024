# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:24:36 2024

@author: Simon
"""
import re
import os
from aoc import get_input, get_lines
import stimer
import numpy as np

day = os.path.basename(__file__)[-5:-3]
content = get_input(day)

#%% part 1

# Regular expression to match mul(X,Y) where X and Y are integers
pattern = r"mul\(\d+,\d+\)"

# Example usage
test_string = "mul(5,10) mul( -3 , 4 ) mul(0,-7) mul(12,abc) mul( -15 , -20 )"

# Find all matches
matches = re.findall(pattern, content)

s = 0
for m in matches:
    m = m.replace('mul(', '')
    m = m[:-1]
    s += np.prod([int(x) for x in m.split(',')])
print(s)

# print("Matches:", matches)

#%% part2
# Regular expression to match mul(X,Y) where X and Y are integers
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

# Example usage
test_string = "mul(5,10) mul( -3 , 4 ) mul(0,-7) mul(12,abc) mul( -15 , -20 ) do()"


# Find all matches
matches = re.findall(pattern, content)
# print(matches)

s = 0
run = True
dos = 0
donts = 0
enabled =0
for m in matches:
    if m=='do()':
        dos += 1
        run = True
        continue
    elif m=='don\'t()':
        donts+=1
        run = False
        continue
    if not run:
        continue
    enabled += 1
    m = m.replace('mul(', '')
    m = m[:-1]
    s += np.prod([int(x) for x in m.split(',')])


print(s)
