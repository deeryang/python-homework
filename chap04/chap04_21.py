#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:15:14 2019

@author: yang
"""

year = eval(input("Enter year: (e.g., 2008): "))
m = eval(input("Enter month: 1-12: "))
q = eval(input("Enter the day of the month: 1-31: "))

if m == 1 or m == 2:
    year = year - 1
    m = m + 12
j = year // 100
k = year % 100

h = (q + (26 * (m + 1) // 10) + k + k // 4 + j // 4 + 5 * j) % 7

if h == 0:
    print("Day of the week is Saturday")
elif h == 1:
    print("Day of the week is Sunday")
elif h == 2:
    print("Day of the week is Monday")
elif h == 3:
    print("Day of the week is Tuesday")
elif h == 4:
    print("Day of the week is Wednesday")
elif h == 5:
    print("Day of the week is Thursday")
elif h == 6:
    print("Day of the week is Friday")