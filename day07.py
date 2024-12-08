# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:35:22 2024

@author: Simon
"""
import os
from aoc import get_input, get_lines, get_matrix
import stimer
import numpy as np
import itertools
from operator import add, mul
from tqdm import tqdm

day = os.path.basename(__file__)[-5:-3]

lines = get_lines(day)
x = get_input(day)

# lines = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20""".split('\n')

#%% part 1

valid_results = 0

for line in tqdm(lines):
    expected, nums = line.split(': ')
    nums = [int(num) for num in nums.split(' ')]
    expected = int(expected)

    n_ops = len(nums)-1
    for ops in itertools.product([mul] + [add], repeat=n_ops):
        res = nums[0]  # start with the first number
        eq = f'{expected} = {nums[0]}'

        for op, num in zip(ops, nums[1:], strict=True):
            if 'add' in str(op):
                eq += f' + {num}'
            else:
                eq += f' * {num}'
            res = op(res, num)

        if res==expected:
            # print(f'{eq}')
            valid_results += expected
            break


print(f'{valid_results=}')



#%% part 2

concat = lambda x, y: int(str(x) + str(y))

valid_results = 0

for line in tqdm(lines):
    expected, nums = line.split(': ')
    nums = [int(num) for num in nums.split(' ')]
    expected = int(expected)

    n_ops = len(nums)-1
    for ops in itertools.product([mul, add, concat], repeat=n_ops):
        res = nums[0]  # start with the first number
        # eq = f'{expected} = {nums[0]}'

        for op, num in zip(ops, nums[1:], strict=True):
            # if 'add' in str(op):
            #     eq += f' + {num}'
            # else:
            #     eq += f' * {num}'
            res = op(res, num)

        if res==expected:
            # print(f'{eq}')
            valid_results += expected
            break


print(f'{valid_results=}')
