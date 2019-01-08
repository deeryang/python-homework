#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:31:36 2019

@author: yang
"""

x, y = eval(input("Enter a point with two coordinates: "))

if abs(x) <= 5 and abs(y) <= 2.5:
    print("Point (" + str(x) + "," + str(y) + ") is in the rectangle")
else:
    print("Point (" + str(x) + "," + str(y) + ") is not in the rectangle")