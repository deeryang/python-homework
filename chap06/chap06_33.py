#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:41:24 2019

@author: yang
"""

import math

def area(s):
    
    return 5 * s ** 2 / (4 * math.tan(math.pi / 5))

def main():
    s = eval(input("Enter the side:"))
    print("The area of the pentagon is", area(s))
    
main()