#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:56:47 2019

@author: yang
"""

import math

print(format("Degrees", ">10s"), " | ", format("Sin   ", ">10s"), " | ", format("Cos   ", ">10s"))
print("-" * 40)

for i in range(0, 361, 10):
    radians = math.radians(i)
    print(format(i, ">10d"), " | ", format(math.sin(radians), ">10.4f"), " | ", format(math.cos(radians), ">10.4f"))
    