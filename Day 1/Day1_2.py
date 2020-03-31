#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:28:44 2019

@author: monicaremmers
"""
def FuelCounterUpperLoop(mass):
    fuelsum = 0
    fuel = mass//3 - 2
    while fuel > 0:
        fuelsum += fuel
        fuel = fuel//3 - 2
    return fuelsum

# take input list
input_string = input('Enter a list of inputs.')
list = input_string.split()
sum = 0
for num in list:
    sum += FuelCounterUpperLoop(int(num))
print('Sum = ',sum)