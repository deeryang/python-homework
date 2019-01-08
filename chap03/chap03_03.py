#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:05:21 2019

@author: yang
"""

#import math

x1, y1 = eval(input("Enter the coordinate of point1:"))
x2, y2 = eval(input("Enter the coordinate of point2:"))
x3, y3 = eval(input("Enter the coordinate of point3:"))
x4, y4 = eval(input("Enter the coordinate of point4:"))

# =============================================================================
# s1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# s2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
# s3 = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
# s4 = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
# s = math.sqrt((x1 - x3) ** 2 + (y1- y3) ** 2)
# =============================================================================

area123 = 1 / 2 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x2 * y1 - x3 * y2)
area234 = 1 / 2 * abs(x2 * y3 + x3 * y4 + x4 * y2 - x2 * y4 - x3 * y2 - x4 * y3)

print("The total area made by the four points:", area123 + area234)
