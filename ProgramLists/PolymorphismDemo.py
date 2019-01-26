#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:34:51 2019

@author: yang
"""

from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    displayObject(c)
    displayObject(r)
    print("Are the circle and rectangle the same size?", isSameArea(c, r))
   
# Display geometric object properties
def displayObject(g):
    print(g.__str__())
    
# Compare the areas of two geometric object
def isSameArea(g1, g2):
    return g1.getArea() == g2.getArea()

main()