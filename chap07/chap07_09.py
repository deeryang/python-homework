#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:29:09 2019

@author: yang
"""

class LinearEquation:
    
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
    
    def getC(self):
        return self.__c
    
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        return True if self.__a * self.__d - self.__b * self.__c else False
    
    def getX(self):
        return (self.__e * self.__d - self.__b * self.__f) / (
                self.__a * self.__d - self.__b * self.__c)
        
    def getY(self):
        return (self.__a * self.__f - self.__e * self.__c) / (
                self.__a * self.__d - self.__b * self.__c)

def main():
    x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))
    x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: "))
    s1 = LinearEquation(x1, 1, x2, 1, y1, y2)
    s2 = LinearEquation(x3, 1, x4, 1, y3, y4)
    
    a = s1.getX()
    b = -1
    e = -s1.getY()
    c = s2.getX()
    d = -1
    f = -s2.getY()
        
    s = LinearEquation(a, b, c, d, e, f)
    if s.isSolvable():
        print("The intersecting point is: (" + str(s.getX()) + ", " + str(s.getY()) + ")")
    else:
        print("The two lines do not intersect.")
        
main()
    