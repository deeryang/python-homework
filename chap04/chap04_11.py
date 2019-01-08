#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:07:02 2019

@author: yang
"""

month, year = eval(input("Enter the month and the year:"))

if (not (year % 4) or not (year % 100)) and (year % 400):
    flag = 1
else:
    flag = 0
    
monthA = [1, 3, 5, 7, 8, 10, 12]
monthB = [4, 6, 9, 11]

if month in monthA:
    print("year", year, "month", month, "has 31 days")
elif month in monthB:
    print("year", year, "month", month, "has 30 days")
elif flag:
    print("year", year, "month", month, "has 29 days")
else:
    print("year", year, "month", month, "has 28 days")