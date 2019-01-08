#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:03:30 2019

@author: yang
"""

a, b, c, d, e, f = eval(input("Enter a, b, c, d, e, f:"))

m = a * d - b * c
if m == 0:
    print("The equation has no solution")
else:
    x = (e * d - b * f) / m
    y = (a * f - e * c) / m
    print("x is", x, "and y is", y)