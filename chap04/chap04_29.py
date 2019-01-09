#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:55:52 2019

@author: yang
"""

import math

x1, y1, r1 = eval(input("Enter circle1's center x-, y-coordinates, and radius: \n"))
x2, y2, r2 = eval(input("Enter circle1's center x-, y-coordinates, and radius: \n"))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d <= abs(r1 - r2):
    if r1 > r2:
        print("circle2 is inside circle1")
    else:
        print("circle1 is inside circle2")
elif d <= r1 + r2:
    print("circle2 overlaps circle1")
else:
    print("circle2 does not overlap circle1")