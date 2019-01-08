#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 20:54:33 2019

@author: yang
"""

import math

x1, y1 = eval(input("Enter point 1 (latitude and longitude) in degrees:"))
x2, y2 = eval(input("Enter point 2 (latitude and longitude) in degrees:"))
r = 6371.01
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)
d = r * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("The distance between the two points is", d, "km")