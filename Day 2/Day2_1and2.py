#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:16:48 2019

@author: monicaremmers
"""

# read input
with open('day2_input.txt') as input_file:
    inputcode = [int(integer) for integer in input_file.read().split(',')]     

# run function in terms of noun, verb, and intcode
def run(noun, verb, Intcode):
    Intcode[1] = noun
    Intcode[2] = verb

    i = 0
    for element in Intcode:
        if Intcode[i] == 1: # addition opcode
            Intcode[Intcode[i+3]] = Intcode[Intcode[i+1]] + Intcode[Intcode[i+2]]
            i += 4
        elif Intcode[i] == 2: # multiplication opcode
            Intcode[Intcode[i+3]]= Intcode[Intcode[i+1]]*Intcode[Intcode[i+2]]
            i += 4
        elif Intcode[i] == 99: # halt opcode
            break
    return Intcode[0] # return address 0
 
print(run(12, 2, inputcode[:])) # part 1

for x in range(99): # part 2
    for y in range(99):
        if run(x, y, inputcode[:]) == 19690720:
            print(100 * x + y)
            break
        