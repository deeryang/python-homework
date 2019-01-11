#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:43:33 2019

@author: yang
"""

counter = 1

for i in range(100, 1001):
    if i % 5 == 0 and i % 6 == 0:
        if counter % 10 != 0:
            print(i, end = " ")
        else:
            print(i)
        counter += 1