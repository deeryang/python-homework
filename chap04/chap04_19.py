#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:18:30 2019

@author: yang
"""

a, b, c = eval(input("Enter three edges:"))

arr = sorted([a, b, c])
if arr[0] > 0 and arr[0] + arr[1] > arr[2]:
    print("The perimeter is", a + b + c)
else:
    print("The input is invalid")