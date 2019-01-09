#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 20:27:30 2019

@author: yang
"""

total = 0
positives = 0
negatives = 0

num = int(input("Enter an integer, the input ends if it is 0: ").strip())

if num == 0:
    print("You didn't enter any number")
else:
    while num:
        if num > 0:
            positives += 1
        else:
            negatives += 1
        total += num
        num = int(input("Enter an integer, the input ends if it is 0: ").strip())
    
    print("The number of positives is", positives)
    print("The number of negatives is", negatives)
    print("The total is", total)
    print("The average is", total / (positives + negatives))

    