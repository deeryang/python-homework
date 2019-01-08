#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:20:27 2019

@author: yang
"""

print("a\t", "b\t", "a ** b")
for i in range(5):
    a = i + 1
    b = a + 1
    c = a ** b
    print(a, '\t', b, '\t', c)