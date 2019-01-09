#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:23:24 2019

@author: yang
"""

value = eval(input("Enter a decimal value (0 to 15): "))

if value >= 0 and value <= 15 and isinstance(value, int):
    hexValue = hex(value)
    hexValue = hexValue.replace('0x', '').upper()
    print("The hex value is", hexValue)
else:
    print("invalid input")