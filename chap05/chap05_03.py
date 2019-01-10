#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 19:54:26 2019

@author: yang
"""

print(format("Kilograms", ">10s"), '  |', format("Pounds", ">8s"))
print("-" * 25)
for i in range(1, 200, 2):
    print(format(i, ">10d"), '  |', format(2.2 * i, ">8.1f"))