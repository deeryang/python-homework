#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:04:15 2019

@author: yang
"""

import math

class Circle2D:
    
    def __init__(self, x = 0, y = 0, radius = 0):
        self.__x = x
        self.__y = y
        self.__radius = radius
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getRadius(self):
        return self.__radius
    
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def setRadius(self, radius):
        self.__radius = radius
        
    def getArea(self):
        return math.pi * self.__radius * self.__radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.__radius
    
    def containsPoint(self, x, y):
        if (x - self.__x) ** 2 + (y - self.__y) ** 2 < self.__radius ** 2:
            return True
        else:
            return False
        
    def contain(self, circle2D):
        d = math.sqrt((circle2D.getX() - self.__x) ** 2 + (circle2D.getY() - self.__y) ** 2)
        if self.__radius - circle2D.getRadius() >= d:
            return True
        else:
            return False
        
    def overlaps(self, circle2D):
        d = math.sqrt((circle2D.getX() - self.__x) ** 2 + (circle2D.getY() - self.__y) ** 2)
        if self.__radius - circle2D.getRadius() < d:
            return True
        else:
            return False
        
    def __contains__(self, another):
        d = math.sqrt((self.__x - another.getX()) ** 2 + (self.__y - another.getY()) ** 2)
        if self.__radius - another.getRadius() >= d:
            return True
        else:
            return False
        
    def __cmp__(self, another):
        if self.__radius > another.getRadius():
            return 1
        elif self.__radius < another.getRadius():
            return -1
        else:
            return 0
        
    def __lt__(self, another):
        return (self.__radius - another.getRadius()) < 0
    
    def __le__(self, another):
        return (self.__radius - another.getRadius()) <= 0
    
    def __eq__(self, another):
        return (self.__radius - another.getRadius()) == 0
    
    def __ne__(self, another):
        return (self.__radius - another.getRadius()) != 0
    
    def __gt__(self, another):
        return (self.__radius - another.getRadius()) > 0
    
    def __ge__(self, another):
        return (self.__radius - another.getRadius()) >= 0
    
def main():
    x1, y1, radius1 = eval(input("Enter x1, y1, radius1: "))
    x2, y2, radius2 = eval(input("Enter x2, y2, radius2: "))
    c1 = Circle2D(x1, y1, radius1)
    c2 = Circle2D(x2, y2, radius2)
    
    print("Area for c1 is", c1.getArea())
    print("Perimeter for c1 is", c1.getPerimeter())
    print("Area for c2 is", c2.getArea())
    print("Perimeter for c2 is", c2.getPerimeter())
    print("c1 contains the center of c2?", c1.containsPoint(c2.getX(), c2.getY()))
    print("c1 contains c2?", c1.contain(c2))
    print("c2 is in c1?", c2 in c1)
    print("c1 overlaps c2?", c1.overlaps(c2))
    
main()