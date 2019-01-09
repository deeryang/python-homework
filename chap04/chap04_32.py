#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:17:08 2019

@author: yang
"""

x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2:\n"))

d = (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0)

if d == 0 and x2 >= min(x0, x1) and x2 <= max(x0, x1):
    print("(" + str(x2) + ", " + str(y2) + ") is on the segment from (" + str(x0) + ", " 
                    + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")
else:
    print("(" + str(x2) + ", " + str(y2) + ") is not on the segment from (" + str(x0) + ", " 
                    + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ")")