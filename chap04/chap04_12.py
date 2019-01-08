#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:17:59 2019

@author: yang
"""

num = int(input("Enter an integer:"))

flag1 = bool(num % 5)
flag2 = bool(num % 6)

print("Is", num, "divisible by 5 and 6?", flag1 and flag2)
print("Is", num, "divisible by 5 or 6?", flag1 or flag2)
print("Is", num, "divisible by 5 or 6, but not both?", not flag1 or not flag2)