#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:36:18 2019

@author: yang
"""

import math

a, b, c = eval(input("Enter a, b, c:"))
delta = b * b - 4 * a * c
if delta > 0:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print("The roots are", r1, "and", r2)
elif delta == 0:
    r = -b / (2 * a)
    print("The root is", r)
else:
    print("The equation has no real roots")
    