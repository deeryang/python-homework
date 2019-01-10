#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:10:05 2019

@author: yang
"""

print(format("Kilograms", ">10s"), format("Pounds", ">10s"), "  |  ", format("Kilograms", ">10s"), format("Pounds", ">10s"))
print("-"*50)
for i in range(1, 200, 2):
    pounds = int(20 + (i - 1) / 2 * 5)    
    print(format(i, ">10d"), format(2.2 * i, ">10.1f"), "  |  ", format(9.09 / 20 * pounds, ">10.2f"), format(pounds, ">10d"))
