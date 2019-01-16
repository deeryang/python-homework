#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:42:55 2019

@author: yang
"""

import math

def area(n, side):
    return n * side ** 2 / (4 * math.tan(math.pi / n))

def main():
    n = eval(input("Enter the number of the sides:"))
    side = eval(input("Enter the side:"))
    print("The area of the polygon is", area(n, side))
    
main()