#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:06:35 2019

@author: yang
"""

num = eval(input("Enter an integer: "))

print("The factors for", num, "is", end = " ")
factor = 2
while factor <= num:
    if num % factor == 0:
        print(factor, end = " ")
        num = num / factor
    else:
        factor += 1