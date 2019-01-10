#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 20:01:31 2019

@author: yang
"""

print(format("Miles", ">8s"), "|", format("Kilometers", ">4s"))
print("-" * 20)
for i in range(1, 11):
    print(format(i, ">8d"), "|", format(1.609 * i, ">8.3f"))