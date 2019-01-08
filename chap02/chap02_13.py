#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:23:37 2019

@author: yang
"""

num = eval(input("Enter an integer:"))
while (num):
    res = num % 10
    print(res)
    num = num // 10