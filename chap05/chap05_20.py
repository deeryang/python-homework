#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:30:41 2019

@author: yang
"""

# model A
for i in range(1, 7):
    for j in range(i):
        print(j + 1, end = " ")
    print()

print("-" * 15)

# model B
for i in range(6):
    for j in range(6 - i):
        print(j + 1, end = " ")
    print()
    
print("-" * 15)

# model C
for i in range(6):
    for j in range(6):
        if j < 5 - i:
            print(" ", end = " ")
        else:
            print(6 - j, end = " ")
    print()
    
print("-" * 15)

# model D
for i in range(6):
    for j in range(6):
        if j >= i:
            print(j - i + 1, end = " ")
        else:
            print(" ", end = " ")
    print()