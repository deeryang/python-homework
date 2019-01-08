#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:11:21 2019

@author: yang
"""

num = eval(input("Enter a number between 0 and 1000:"))
sumNum = 0
while (num):
    sumNum += num % 10
    num = num // 10

print("The sum of the digits is", sumNum)