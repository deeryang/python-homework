#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:46:51 2019

@author: yang
"""

for i in range(1, 9):
    print("    " * (8 - i), end = "")
    for j in range(1, i):
        print(format(2 ** (j - 1), ">4d"), end = "")
    for j in range(1, i + 1):
        print(format(2 ** (i - j), ">4d"), end = "")
    print()
