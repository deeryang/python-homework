#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:05:35 2019

@author: yang
"""

from GeometricObject import GeometricObject
import math

class Circle(GeometricObject):
    
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
        
    def getArea(self):
        return math.pi * self.__radius ** 2
    
    def getDiameter(self):
        return 2 * self.__radius
    
    def getPerimeter(self):
        return 2 * math.pi * self.__radius
    
# =============================================================================
#     def printCircle(self):
#         print(self.__str__() + " radius: " + str(self.__radius))
# =============================================================================
        
    def __str__(self):
        return super().__str__() + "  radius: " + str(self.__radius)
        