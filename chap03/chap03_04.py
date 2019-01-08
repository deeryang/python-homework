#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 21:23:53 2019

@author: yang
"""

import math

s = eval(input("Enter the side:"))
area = 5 * s ** 2 / (4 * math.tan(math.pi / 5))

print("The area of the pentagon is", area)