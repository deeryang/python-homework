#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:33:54 2019

@author: yang
"""

for n in range(10000, 100001, 10000):
    total = 0
    for i in range(n, 0, -1):
        total += 4 * ((-1) ** (i - 1) / (2 * i - 1))
    print("if i =", n, ", pi =", total)
