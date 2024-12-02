# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 08:05:14 2024

@author: Simon
"""
import os
from aoc import get_input, get_lines
import stimer
import numpy as np

day = os.path.basename(__file__)[-5:-3]
lines = [[int(x) for x in line.split(' ')] for line in get_lines(day)]

# c = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
# lines = c.split('\n')

#%% part 1
with stimer:
    safe = 0
    for line in lines:
        diff = np.diff(line)
        monopos = ((diff>0) & (diff<4)).all()
        mononeg = ((-diff>0) & (-diff<4)).all()
        safe += (monopos | mononeg)

    print(safe)


    #%% part 2
    safe = 0
    for line in lines:
        diff = np.diff(line)
        monopos = ((diff>0) & (diff<4)).all()
        mononeg = ((-diff>0) & (-diff<4)).all()
        if (monopos | mononeg):
            safe += 1
            continue

        for idx in range(len(line)):
            # remove idx from line and check again
            line2 = line[:idx] + line[idx+1:]
            # print(f'{idx} {line=} {line2=}')

            diff = np.diff(np.array(line2, dtype=int))
            monopos = ((diff>0) & (diff<4)).all()
            mononeg = ((-diff>0) & (-diff<4)).all()
            if (monopos | mononeg):
                safe += 1
                break

    print(safe)
