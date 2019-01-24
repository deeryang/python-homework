#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:27:49 2019

@author: yang
"""

class Rectangle:
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
        
    def getArea(self):
        return self.width * self.height
    
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    
def main():
    r1 = Rectangle(4, 40)
    print("Rectangle 1 :")
    print("width =", r1.width)
    print("height =", r1.height)
    print("Area =", r1.getArea())
    print("Perimeter =", r1.getPerimeter())
    r2 = Rectangle(3.5, 37.5)
    print("Rectangle 2 :")
    print("width =", r2.width)
    print("height =", r2.height)
    print("Area =", r2.getArea())
    print("Perimeter =", r2.getPerimeter())
    
    
main()