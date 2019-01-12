#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:32:20 2019

@author: yang
"""

total = 0
for i in range(1, 98, 2):
    total += i / (i + 2)
print("1/3 + 3/5 + 5/7 + ... + 95/97 + 97/99 =", total)