#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:52:10 2019

@author: yang
"""

# =============================================================================
# read the data from in.txt
# use the console window
# command: python3 chap05_10.py < in.txt
# =============================================================================
numberOfStudents = eval(input("Enter the number of students: "))
print()

maxScore = 0

for i in range(numberOfStudents):
    score = eval(input("Enter the score: "))
    print()
    maxScore = max(score, maxScore)
    
print("The maximum score is:", maxScore)