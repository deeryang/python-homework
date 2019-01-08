#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:44:36 2019

@author: yang
"""

num1, num2, num3 = eval(input("Enter three numbers:"))

if num1 > num2:
    num1, num2 = num2, num1
    
if num2 > num3:
    num2, num3 = num3, num2
    
if num1 > num3:
    num1, num3 = num3, num1
    
print(num1, num2, num3)
