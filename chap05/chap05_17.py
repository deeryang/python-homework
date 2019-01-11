#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:02:21 2019

@author: yang
"""

for i in range(33, 127):
    if (i - 32) % 10 != 0:
        print(chr(i), end = " ")
    else:
        print(chr(i))