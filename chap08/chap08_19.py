#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 19:41:44 2019

@author: yang
"""

class Rectangle2D:
    
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        
    def getX(self):
        return self.__x
    
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__y
    
    def setY(self, y):
        self.__y = y
        
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width
        
    def getHeight(self):
        return self.__height
    
    def setHeight(self, height):
        self.__height = height
        
    def getArea(self):
        return self.__width * self.__height
    
    def getPerimeter(self):
        return 2 * (self.__width + self.__height)
    
    def containsPoint(self, x, y):
        return (abs(x - self.__x) <= self.__width / 2 and (abs(y - self.__y) <= self.__height / 2))
    
    def contain(self, Rectangle2D):
        if (abs(self.__x - Rectangle2D.getX()) < (self.__width - Rectangle2D.getWidth()) / 2 and
            abs(self.__y - Rectangle2D.getY()) < (self.__height - Rectangle2D.getHeight()) / 2):
            return True
        else:
            return False
        
    def overlaps(self, Rectangle2D):
        if (abs(self.__x - Rectangle2D.getX()) < (self.__width + Rectangle2D.getWidth()) / 2 and
            abs(self.__y - Rectangle2D.getY()) < (self.__height + Rectangle2D.getHeight()) / 2):
            return True
        else:
            return False
        
    def __contain__(self, another):
        return self.contain(another)
    
    def __cmp__(self, another):
        temp = self.getArea() - another.getArea()
        if temp > 0:
            return 1
        elif temp < 0:
            return -1
        else:
            return 0
        
    def __lt__(self, another):
        return self.__cmp__(another) < 0
    
    def __le__(self, another):
        return self.__cmp__(another) <= 0
    
    def __eq__(self, another):
        return self.__cmp__(another) == 0
    
    def __ne__(self, another):
        return self.__cmp__(another) != 0
    
    def __gt__(self, another):
        return self.__cmp__(another) > 0
    
    def __ge__(self, another):
        return self.__cmp__(another) >= 0
    
def main():
    x1, y1, width1, height1 = eval(input("Enter x1, y1, width1, height1: "))
    x2, y2, width2, height2 = eval(input("Enter x2, y2, width2, height2: "))
    
    r1 = Rectangle2D(x1, y1, width1, height1)
    r2 = Rectangle2D(x2, y2, width2, height2)
# =============================================================================
#     r1 = Rectangle2D(9,1.3,10,35.3)
#     r2 = Rectangle2D(1.3,4.3,4,5.3)
# =============================================================================

    print("Area for r1 is", r1.getArea())
    print("Perimeter for r1 is", r1.getPerimeter())
    print("Area for r2 is", r2.getArea())
    print("Perimeter for r2 is", r2.getPerimeter())
    print("r1 contains the center of r2?", r1.containsPoint(r2.getX(), r2.getY()))
    print("r1 contains r2?", r1.contain(r2))
    print("r1 overlaps r2?", r1.overlaps(r2))
    
main()