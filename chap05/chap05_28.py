#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 20:33:49 2019

@author: yang
"""

item = 1
res = 1
for i in range(1, 100001):
    item = item / i
    res = res + item
    if i % 10000 == 0:
        print("i =", i, ", e =", res)