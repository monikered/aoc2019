#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:16:48 2019

@author: monicaremmers
"""
# part 1
input_string = input('Enter a list of inputs. ')
Intcode = input_string.split(',') # split list into individual components
Intcode = list(map(int, Intcode)) # parse as integers


def run(noun, verb):
    Intcode[1:3] = [noun,verb]
    x = 0
    for i in Intcode:
        if Intcode[x] == 1:
            Intcode[Intcode[x+3]] = Intcode[Intcode[x+1]] + Intcode[Intcode[x+2]]
            x += 4
        elif Intcode[x] == 2:
            Intcode[Intcode[x+3]]= Intcode[Intcode[x+1]]*Intcode[Intcode[x+2]]
            x += 4
        elif Intcode[x] == 99:
            break
    return Intcode[0]

# part 2

def runsolve(out):
    for x in range(100):
        for y in range(100):
            if run(x, y) == out:
                return 100 * x + y