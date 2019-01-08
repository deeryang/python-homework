#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:44:44 2019

@author: yang
"""

x1, y1, x2, y2, x3, y3, x4, y4 = eval(input("Enter x1, y1, x2, y2, x3, y3, x4, y4:\n"))

a = y1 - y2
b = -(x1 - x2)
c = y3 - y4
d = -(x3 - x4)
e = (y1 - y2) * x1 - (x1 - x2) * y1
f = (y3 - y4) * x3 - (x3 - x4) * y3

m = a * d - b * c

if m == 0:
    print("The two lines are parallel")
else:
    x = (e * d - b * f) / m
    y = (a * f - e * c) / m
    print("The intersecting point is at (" + format(x, ".4f") + ", " + format(y, ".4f") + ")")