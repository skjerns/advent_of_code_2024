# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 11:19:03 2024

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

disk = get_input(day)

# disk = '2333133121414131402'
#%% part 1
with stimer:
    # save in a list, most performant
    uncompressed = []

    # first decompress the disk
    for i, char in enumerate(disk):
        if i%2:
            # use -1 as free space marker, more performant than dot
            uncompressed += [-1]*int(char)
        else:
            file_id = i//2
            uncompressed += [file_id]*int(char)

    # now fragment the disk!
    # have two cursors, one walking backwards, one forward
    pos = 0
    for i, c in enumerate(uncompressed[::-1]):
        # find next empty space
        while (uncompressed[pos])!=-1:
            pos += 1
        if len(uncompressed)-i<=pos:
            break
        uncompressed[pos] = c  # shift that file part here
        uncompressed[len(uncompressed)-i-1] = -1

    # revert from our -1 marker for free space to 0.
    uncompressed  = [c if c!=-1 else 0 for c in uncompressed]

    # needs to be dtype int64, else integer overflow!
    hashsum = np.sum([x for x in (uncompressed * np.arange(len(uncompressed), dtype=np.int64))])
    print(f'{hashsum=}')

    #%% part 2

    # save in a list, most performant
    uncompressed = []

    # first decompress the disk once more
    for i, char in enumerate(disk):
        if i%2:
            # use -1 as free space marker, more performant than dot
            uncompressed += [-1]*int(char)
        else:
            file_id = i//2
            uncompressed += [file_id]*int(char)

    # next, go though
    pos_f = len(uncompressed)
    moved = set([-1])  # -1 will be ignored

    for fid, group in tqdm(itertools.groupby(uncompressed[::-1])):
        len_file = len(list(group))
        pos_f -= len_file

        if fid in moved:
            continue

        moved.add(fid)  # make sure to move each file only once

        # print(fid)
        # let's find the next slot that might fit!
        pos = 0
        # print(fid, pos_f,  ''.join([str(x) if x>=0 else '.' for x in uncompressed]) )
        # if fid==3:
            # pass
        for space, group in itertools.groupby(uncompressed):
            if pos>(pos_f):
                break
            len_slot = len(list(group))
            pos += len_slot

            if space!=-1:  # is this free real estate? no.
                continue
            if len_slot>=len_file:
                uncompressed[pos-len_slot:pos-len_slot+len_file] = [fid] * len_file
                uncompressed[pos_f:pos_f+len_file] = [-1] * len_file
                break

    uncompressed  = [c if c!=-1 else 0 for c in uncompressed]
    hashsum = np.sum([x for x in (uncompressed * np.arange(len(uncompressed), dtype=np.int64))])
    print(f'{hashsum=}')
