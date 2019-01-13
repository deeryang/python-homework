#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:40:22 2019

@author: yang
"""

cost = 10000
total = 0
for i in range(10):
    cost = cost * (1 + 0.05)
    
for i in range(4):
    total += cost
    cost = cost * (1 + 0.05)

print("The cost of ten years later: " + format(cost, ".2f"))
print("The total cost of four years ten years later: " + format(total, ".2f"))