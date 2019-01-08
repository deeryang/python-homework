#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:27:08 2019

@author: yang
"""

import math

x, y = eval(input("Enter a point with two coorinates: "))
d = math.sqrt(x * x + y * y)

print("Point (" + str(x) + "," + str(y) + ") is ", end = "")

if d <= 10:
    print("in the circle")
else:
    print("not in the circle")