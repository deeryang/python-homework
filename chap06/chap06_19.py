#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:50:25 2019

@author: yang
"""

# return true if point (x2, y2) is on the left side of the
#  directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    
    return True if (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0) > 0 else False

# return true if point (x2, y2) is on the same
#  line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    
    return True if (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0) == 0 else False
# return true if point (x2, y2) is on the right side of the
#  directed line from (x0, y0) to (x1, y1)
def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    
    return True if (x1 - x0) * (y2 - y0) - (x2 - x0)*(y1 - y0) < 0 else False

def main():
    x0, y0, x1, y1, x2, y2 = eval(input("Enter coordinates for the three points p0, p1, and p2:\n"))
    if leftOfTheLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the left side of the line from p0 to p1")
    elif onTheSameLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the same line from p0 to p1")
    elif rightOfTheLine(x0, y0, x1, y1, x2, y2):
        print("p2 is on the right side of the line from p0 to p1")
        
main()

