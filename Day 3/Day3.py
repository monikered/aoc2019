#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:33:28 2019

@author: monicaremmers
"""
# define dictionaries and functions
DX = {'R': -1, 'L': 1, 'U': 0, 'D': 0}
DY = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

def wirepoints(inputlist):
    x = 0
    y = 0
    length = 0
    pos = {}
    for item in inputlist:
        d = item[0]
        n = int(item[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            pos.update({int(x):int(y)})
            print(pos)
    return pos 

def ManhattanDist(x1,y1):
    return abs(x1) + abs(y1)
    

with open('day3_input.txt', 'r') as input_file: # read input flie
    wires = input_file.read().split()
    wireA = wires[0].split(',')
    wireB = wires[1].split(',')

Apos = wirepoints(wireA)
Bpos = wirepoints(wireB)

#%%
i = dict(Apos.items() & Bpos.items())
union = dict(Apos.items() | Bpos.items())
diff = dict(Apos.items() ^ Bpos.items())

#%%
# look up how to find intersects of two dictionaries

intersects = (set(Apos) & set(Bpos))
print(intersects)
print(ManhattanDist(intersects[0]), ManhattanDist(intersects[1]))
