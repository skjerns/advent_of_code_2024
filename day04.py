# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:46:02 2024

@author: Simon
"""
import re
import os
from aoc import get_input, get_lines, get_matrix
import stimer
import numpy as np

day = os.path.basename(__file__)[-5:-3]
matrix = get_matrix(day)

#%% day 1
from scipy.signal import convolve2d

# assign values
matrix[matrix=='X'] = 1
matrix[matrix=='M'] = 2
matrix[matrix=='A'] = 3
matrix[matrix=='S'] = 4
matrix = matrix.astype(int)


kernel = np.atleast_2d([117, -13, 19, -23])  # XMAS
kernel_rev = np.atleast_2d([117, -13, 19, -23][::-1])                   # SMAX
kernel_h = kernel.T
kernel_h_rev = kernel_rev.T
kernel_diag1 = np.zeros([4, 4])
kernel_diag1[np.eye(4, dtype=bool)] = kernel.ravel()
kernel_diag1_rev = np.zeros([4, 4])
kernel_diag1_rev[np.eye(4, dtype=bool)] = kernel_rev.ravel()
kernel_diag2 = np.zeros([4, 4])
kernel_diag2[np.eye(4, dtype=bool)[::-1]] = kernel.ravel()
kernel_diag2_rev = np.zeros([4, 4])
kernel_diag2_rev[np.eye(4, dtype=bool)[::-1]] = kernel_rev.ravel()

xmas=0
for k in [kernel, kernel_rev, kernel_h, kernel_h_rev, kernel_diag1, kernel_diag1_rev, kernel_diag2, kernel_diag2_rev]:
    res = convolve2d(matrix, k, mode='valid')
    xmas += (res==444).sum()
print(xmas)


#%%


kernel = np.zeros([3, 3])
kernel[[0, 2], 0] = 117
kernel[[0, 2], 2] = -59
kernel[[1, 1], 1] = 31

# matrix = np.zeros([3, 3])
# matrix[[0, 2], 0] = 7
# matrix[[0, 2], 2] = 21
# matrix[[1, 1], 1] = 17

# x = np.array(x)
x = get_matrix(day)
matrix = np.zeros_like(x, dtype=int)
matrix[x=='X'] = 0
matrix[x=='M'] = 7
matrix[x=='A'] = 17
matrix[x=='S'] = 21
matrix = matrix.astype(int)

# tes = np.zeros([8, 8])

xmas=0
for rot in range(4):
    print(kernel)
    kernel = np.rot90(kernel)
    res = convolve2d(matrix, kernel, mode='valid')
    # tes += res==4615
    print(res==4615)
    xmas += (res==4615).sum()
print(xmas)

# 1899 too high
# 1247 too low
