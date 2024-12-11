# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:23:43 2024

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


content = get_input(day)

stones_orig = [int(x) for x in content.split(' ')]

#%% part 1
with stimer:
    from tqdm import tqdm
    # stones = [125, 17]
    stones = stones_orig.copy()
    for _ in tqdm(range(25)):
        stones_new = []
        # print(stones)
        inserted = 0
        for i, stone in enumerate(stones):
            # If the stone is engraved with the number 0, it is replaced by a
            # stone engraved with the number 1.
            if stone==0:
                stones_new += [1]
            # If the stone is engraved with a number that has an even number of
            # digits, it is replaced by two stones. The left half of the digits
            # are engraved on the new left stone, and the right half of the digits
            # are engraved on the new right stone. (The new numbers don't keep extra
            # leading zeroes: 1000 would become stones 10 and 0.)
            elif (stone_len:=len(stone_str:=str(stone)))%2==0:
                stone1 = int(stone_str[:stone_len//2])
                stone2 =  int(stone_str[stone_len//2:])
                stones_new += [stone1, stone2]
            else:
                stones_new += [stone*2024]
        stones = stones_new
        # input()

    print(f'{len(stones)=}')

    #%% part 2
    from functools import cache

    # calculate each stone individually,
    # they are actually independent of their surrounding.
    # My idea: do a depth-first-search with caching. that way we reach the end
    # of the tree relatively quickly and have our first caching results.

    # update: nope, I'll do reverse search and see from the last node
    # and cache results. then i calculate the level above that and so on.

    stone_dict = {}

    # stones = [125, 17]

    transitions = {0 : (1,)}

    # first of all establish which transitions are possible
    # actually there are only a limited set of numbers appearing in all of the
    # transitions. This is not collatz after all!
    for stone_single in stones_orig.copy()[2:]:
        stones_subset = [stone_single]
        for i in range(75):
            stones_new = []

            # only calculate stones that we have not yet calculated
            stones_subset = [stone for stone in stones_subset if stone not in transitions]
            for i, stone in enumerate(stones_subset):
                # print(stone in calculated)
                # If the stone is engraved with the number 0, it is replaced by a
                # stone engraved with the number 1.
                if stone==0:
                    stones_new += [1]
                # If the stone is engraved with a number that has an even number of
                # digits, it is replaced by two stones. The left half of the digits
                # are engraved on the new left stone, and the right half of the digits
                # are engraved on the new right stone. (The new numbers don't keep extra
                # leading zeroes: 1000 would become stones 10 and 0.)
                elif (stone_len:=len(stone_str:=str(stone)))%2==0:
                    stone1 = int(stone_str[:stone_len//2])
                    stone2 =  int(stone_str[stone_len//2:])
                    stones_new += [stone1, stone2]
                    transitions[stone] = (stone1, stone2)
                else:
                    stones_new += [stone*2024]
                    transitions[stone] = (stone*2024,)
            stones_subset = stones_new


    maxlevel = 75

    @cache
    def blink(stone, level=0):
        if level==maxlevel:
            return 1
            # take the leftmost stone.
        if stone==0:
            return blink(1, level+1)
        # If the stone is engraved with a number that has an even number of
        # digits, it is replaced by two stones. The left half of the digits
        # are engraved on the new left stone, and the right half of the digits
        # are engraved on the new right stone. (The new numbers don't keep extra
        # leading zeroes: 1000 would become stones 10 and 0.)
        elif (stone_len:=len(stone_str:=str(stone)))%2==0:
            stone1 = int(stone_str[:stone_len//2])
            stone2 =  int(stone_str[stone_len//2:])
            return blink(stone1, level+1) + blink(stone2, level+1)
        else:
            return blink(stone*2024, level+1)
    # next, calculate from the lowest possibility upwards
    blink.cache_clear()

    for level in range(maxlevel, 0, -1):
        for stone in transitions:
            blink(stone, level)

    n_stones = sum([blink(stone)for stone in stones_orig])

    print(f'{n_stones=}')
