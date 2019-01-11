#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:13:00 2019

@author: yang
"""

lines = eval(input("Enter the number of lines (1 - 15): "))

for i in range(1, lines + 1):
    counter = 1
    while counter <= 2 * lines - 1:
        if abs(lines - counter) < i:
            print(abs(lines - counter) + 1, end = " ")
        else:
            print(" ", end = " ")
        counter += 1
    print()