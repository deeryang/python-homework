#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:47:37 2019

@author: yang
"""

# List 6-10
def sort(number1, number2):
    if number1 < number2:
        return number1, number2
    else:
        return number2, number1
    
n1, n2 = sort(3, 2)
print("n1 is", n1)
print("n2 is", n2)