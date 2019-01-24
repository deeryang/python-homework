#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:47:46 2019

@author: yang
"""

# List 7-2
from Circle import Circle

def main():
    # Create a circle with radius 1
    circle1 = Circle()
    print("The area of the circle of radius", 
          circle1.radius, "is", circle1.getArea())
    
    # Create a circle with radius 25
    circle2 = Circle(25)
    print("The area of the circle of radius", 
          circle2.radius, "is", circle2.getArea())
    
    # Create a circle with radius 125
    circle3 = Circle(125)
    print("The area of the circle of radius", 
          circle3.radius, "is", circle3.getArea())
    
    # Modify circle radius
    circle2.radius = 100    # or circle2.setRadius(100)
    print("The area of the circle of radius", 
          circle2.radius, "is", circle2.getArea())
    
main()  # Call the main function
    