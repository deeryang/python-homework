#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:36:47 2019

@author: yang
"""

numberOfStudents = eval(input("Enter the number of students: "))
print()

maxScore1 = 0
maxScore2 = 0

for i in range(numberOfStudents):
    score = eval(input("Enter the score: "))
    if maxScore1 < score:
        maxScore1, score = score, maxScore1
    if maxScore2 < score and maxScore2 < maxScore1:
        maxScore2, score = score, maxScore2
    
print("The first maximum score is:", maxScore1)
print("The second maximum score is:", maxScore2)