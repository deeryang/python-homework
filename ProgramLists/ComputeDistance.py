#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:56:07 2019

@author: yang
"""

# Enter the first point with two float values
x1, y1 = eval(input("Enter x1 and y1 for point 1: "))

# Enter the second point with two float values
x2, y2 = eval(input("Enter x2 and y2 for point 2: "))

# Compute the distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

print("The distance between the two points is", distance)