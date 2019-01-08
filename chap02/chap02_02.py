#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:15:14 2019

@author: yang
"""

import math

radius, length = eval(input("Enter the radius and length of a cylinder:"))
area = radius * radius * math.pi
volume = area * length

print("The area is", area)
print("The volume is", volume)