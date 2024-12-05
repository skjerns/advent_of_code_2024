# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:43:47 2024

@author: Simon
"""

import re
import os
from aoc import get_input, get_lines, get_matrix
import stimer
import numpy as np

day = os.path.basename(__file__)[-5:-3]

c = get_input(day)

# c = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

rules, updates = [x.split('\n') for x in c.split('\n\n')]
updates = [list(map(int, update.split(','))) for update in updates]
rules = [list(map(int,rule.split('|'))) for rule in rules]
#%% part 1

#%% part 1
with stimer:
valids = []
invalids = []
updates_to_fix = []
middle_pages = []

for update in updates:
    validnums = []
    invalidnums = []
    rules_that_apply = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    for num in update:
        # check if any rule is violated
        for X, Y in rules_that_apply:
            if X!=num:  # rule does not apply
                continue

            if Y in validnums:
                # print(f'cant add {X=}, {Y=} already part of {validnums}!')
                invalidnums += [num]
                break
            # it passed, add
        validnums += [num]

    valids.append(validnums)
    invalids.append(invalidnums)
    if len(invalidnums)==0:
        middle_pages += [validnums[len(validnums)//2]]
    else:
        updates_to_fix.append(update)
print('middle_pages sum part 1', sum(middle_pages))

#%% part 2
from collections import defaultdict
new_updates = []



middle_pages = []

for update in updates_to_fix:
    rules_that_apply = [rule for rule in rules if (rule[0] in update and rule[1] in update)]
    # for num in update:
    # pass
    new_update = []
    for num in update:
        skip = False
        # check if any rule is violated
        for X, Ys in rules_dict.items():
            if X!=num:  # rule does not apply
                continue

            indices = [new_update.index(Y) for Y in Ys if Y in new_update]

            if indices:
                new_update.insert(min(indices), X)
                # print(f'cant add {X=}, {Y=} already part of {validnums}!')
                skip = True
                break
        if not skip:
            new_update += [num]
    middle_pages += [new_update[len(new_update)//2]]
    new_updates.append(new_update)


print('middle_pages sum part 2', sum(middle_pages))

# 123 too low
