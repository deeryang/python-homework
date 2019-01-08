#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:26:25 2019

@author: yang
"""

import math

n = eval(input("Enter the number of the sides:"))
s = eval(input("Enter the side:"))
area = n * s ** 2 / (4 * math.tan(math.pi / n))

print("The area of the polygon is", area)