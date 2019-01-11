#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:58:16 2019

@author: yang
"""

n1 = eval(input("Enter first integer: "))
n2 = eval(input("Enter second integer: "))

d = min(n1, n2)

while d:
    if n1 % d == 0 and n2 % d == 0:
        print("The greatest common divisor for", n1, "and", n2, "is", d)
        break
    else:
        d -= 1