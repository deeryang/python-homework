#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:31:53 2019

@author: yang
"""

# List 7-1
import math

class Circle:
    # Construct a circle object
    def __init__(self, radius = 1):
        self.radius = radius
        
    def getPerimeter(self):
        return 2 * self.radius * math.pi
    
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def setRadius(self, radius):
        self.radius = radius
        