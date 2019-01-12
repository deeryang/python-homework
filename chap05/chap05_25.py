#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:30:05 2019

@author: yang
"""

total = 0
for i in range(50000, 0, -1):
    total += 1 / i
print("1 + 1/2 + 1/3 + ... + 1/n =", total)