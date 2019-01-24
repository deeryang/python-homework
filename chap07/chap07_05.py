#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 17:11:55 2019

@author: yang
"""

import math

class RegularPolygon:
    
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    def getN(self):
        return self.__n
    
    def getSide(self):
        return self.__side
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def setN(self, n):
        self.__n = n
        
    def setSide(self, side):
        self.__side = side
        
    def setX(self, x):
        self.__x = x
        
    def setY(self, y):
        self.__y = y
        
    def getPerimeter(self):
        return self.__n * self.__side
    
    def getArea(self):
        return self.__n * self.__side ** 2 / (4 * math.tan(math.pi / self.__n))
    
def display(r):
    print("Perimeter =", r.getPerimeter(), "and Area =", r.getArea())
    
    
def main():
    r1 = RegularPolygon()
    display(r1)
    r2 = RegularPolygon(6, 4)
    display(r2)
    r3 = RegularPolygon(10, 4, 5.6, 7.8)
    display(r3)
    
main()
    