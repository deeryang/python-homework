#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 11:01:04 2019

@author: yang
"""

x, y = eval(input("Enter a point's x- and y-coordinates: "))

if x > 0 and x < 200 and y > 0 and y < 100:
    b = y + 100 / 200 * x
    if b > 0 and b < 100:
        print("The point is in the triangle")
    else:
        print("The point is not in the triangle")
else:
    print("The point is not in the triangle")