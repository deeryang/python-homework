#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:52:10 2019

@author: yang
"""

numberOfStudents = eval(input("Enter the number of students: "))

maxScore = 0

for i in range(numberOfStudents):
    score = eval(input("Enter the score: "))
    maxScore = max(score, maxScore)
    
print("The maximum score is:", maxScore)