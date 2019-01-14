#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:00:32 2019

@author: yang
"""

# return the distance of point (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    x1, y1 = eval(input("Enter the x- and y-coordinate of point1: "))
    x2, y2 = eval(input("Enter the x- and y-coordinate of point2: "))
    d = distance(x1, y1, x2, y2)
    print("The distance of point1 and point 2 is", d)
    
main()