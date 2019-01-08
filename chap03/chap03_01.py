#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:36:19 2019

@author: yang
"""

import math

r = eval(input("Enter the length from the center to a vertex:"))
s = 2 * r * math.sin(math.pi / 5)
area = 5 * s * s / (4 * math.tan(math.pi / 5))

print("The area of the pentagon is", round(area, 2))