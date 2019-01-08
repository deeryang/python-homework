#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:53:38 2019

@author: yang
"""

v, a = eval(input("Enter speed and acceleration:"))
length = v ** 2 / (2 * a)
print("The minimum runway length for this airplane is", length, "meters")