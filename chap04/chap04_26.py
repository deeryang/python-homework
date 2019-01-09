#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:59:18 2019

@author: yang
"""

num = int(input("Enter a three-digit integer: "))

integer = num
res = 0
while num:
    res = (num % 10 + res) * 10
    num = num // 10
    
if integer == res // 10:
    print(integer, "is a palindrome")
else:
    print(integer, "is not a palindrome")