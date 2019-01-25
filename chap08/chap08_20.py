#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 20:22:39 2019

@author: yang
"""

from Rational import Rational

total = Rational(0, 1)
for i in range(9):
    r = Rational(i + 1, i + 2)
    total += r
    
print("sum =", total, "=", float(total))