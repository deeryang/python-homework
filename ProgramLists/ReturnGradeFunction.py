#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:15:39 2019

@author: yang
"""

# List 6-3
# Return the grade for the score
def getGrade(score):
    if score >= 90.0:
        return 'A'
    elif score >= 80.0:
        return 'B'
    elif score >= 70.0:
        return 'C'
    elif score >= 60.0:
        return 'D'
    else:
        return 'F'
    
def main():
    score = eval(input("Enter a score: "))
    print("The grade is ", getGrade(score))

main()  # Call the main function