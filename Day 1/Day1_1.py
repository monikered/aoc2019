#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:59:01 2019

@author: monicaremmers
"""
def FuelCounterUpper(mass):
    return mass//3 - 2

# take input list
input_string = input('Enter a list of inputs.')
list = input_string.split()
sum = 0
for num in list:
    sum += FuelCounterUpper(int(num))
print('Sum = ',sum)
