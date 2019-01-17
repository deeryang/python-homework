#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:39:53 2019

@author: yang
"""

import random

head = 0
tail = 0
for i in range(1000000):
    if random.randint(0, 1):
        head += 1
    else:
        tail += 1
        
print("Head: ", head)
print("Tail: ", tail)