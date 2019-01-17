#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:52:20 2019

@author: yang
"""

import random

counter = 0
times = 1000000
for i in range(times):
    x = 1 - 2 * random.random()
    y = 1 - 2 * random.random()
    if x < 0 or (x > 0 and  x < 1 and y > 0 and y < 1 and x + y < 1):
        counter += 1
        
possibility = counter / times
print("Point in the area 1 and 3 :", possibility)