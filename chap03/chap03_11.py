#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:14:43 2019

@author: yang
"""

num = int(input("Enter an integer:"))
s = ""
while(num):
    s += str(num % 10)
    num = num // 10
print("The reversed number is", s)