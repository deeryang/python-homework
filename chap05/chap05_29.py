#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:03:14 2019

@author: yang
"""

counter = 0
for year in range(2001, 2101):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        counter += 1
        if counter % 10 != 0:
            print(year, end = " ")
        else:
            print(year)