#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 21:35:59 2019

@author: yang
"""

import math

print(format("Number", ">10s"), "  |  ", format("Square Root", ">10"))
print("-" * 30)

for i in range(0, 21, 2):
    print(format(i, ">10d"), "  |  ", format(math.sqrt(i), ">10.4f"))