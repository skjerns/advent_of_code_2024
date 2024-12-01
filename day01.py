# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 17:06:01 2024

@author: Simon
"""
import stimer

with open(__file__.replace('day', 'input')[:-2]+'txt', 'r') as f:
    c = f.read().strip()
    f.seek(0)
    lines = [l.strip() for l in f.readlines()]

#%% part 1
with stimer:
    column1 = [int(x.split('   ')[0]) for x in lines]
    column2 = [int(x.split('   ')[1]) for x in lines]

    column1 = sorted(column1)
    column2 = sorted(column2)

    s = 0
    for x,y in zip(column1, column2):
        s += abs(x-y)

    print(s)


    #%% part 2

    s = 0
    for num in column1:
        s += num * column2.count(num)

    print(s)
