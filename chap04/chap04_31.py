#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:11:16 2019

@author: yang
"""

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2:\n"))

d = (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0)

if d > 0:
    print("p2 is on the left side of the line from p0 to p1")
elif d == 0:
    print("p2 is on the same line from p0 to p1")
else:
    print("p2 is on the right side of the line from p0 to p1")