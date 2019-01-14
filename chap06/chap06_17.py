#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:04:06 2019

@author: yang
"""

import math

# return true if the sum of any two sides is greater
#  than the third side
def isValid(side1, side2, side3):
    return side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2

# returns the area of the triangle
def area(side1, side2, side3):
    p = (side1 + side2 + side3) / 2
    area = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    
    return area

def main():
    side1, side2, side3 =eval(input("Enter three sides in double: "))
    if isValid(side1, side2, side3):
        print("The area of the triangle is", area(side1, side2, side3))
    else:
        print("Input is invalid")
        
main()