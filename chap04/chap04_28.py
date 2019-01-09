#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:08:29 2019

@author: yang
"""

x1, y1, weight1, height1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: \n"))
x2, y2, weight2, height2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: \n"))

if abs(x1 - x2) <= (weight1 - weight2) / 2 and abs(y1 - y2) <= (height1 - height2) / 2:
    print("r2 is inside r1")
elif abs(x1 - x2) <= weight1 / 2 or abs(y1 - y2) <= height1 / 2:
    print("r2 overlaps r1")
else:
    print("r2 does not overlap r1")