#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:52:17 2019

@author: yang
"""

print(format("Miles", ">10s"), format("Kilometers", ">15s"), " |", format("Miles", ">10s"), format("Kilometers", ">15s"))
print("-"*50)
for i in range(1, 11):
    pounds = int(20 + (i - 1) * 5)    
    print(format(i, ">10d"), format(1.609 * i, ">15.3f"), " |", format(12.430 / 20 * pounds, ">10.3f"), format(pounds, ">15d"))
