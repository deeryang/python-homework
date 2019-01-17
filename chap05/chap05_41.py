#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:42:43 2019

@author: yang
"""

num = eval(input("Enter a number (0: for end of input): "))
maxNumber = num
maxCount = 0
while num:
    if num > maxNumber:
        maxNumber = num
        maxCount = 0
    if num == maxNumber:
        maxCount += 1
    num = eval(input("Enter a number (0: for end of input): "))
    
print("The largest number is", maxNumber)
print("The occurrence count of the largest number is", maxCount)