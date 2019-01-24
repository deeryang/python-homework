#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:04:40 2019

@author: yang
"""

# List 6-9
def printArea(width = 1, height = 2):
    area = width * height
    print("width:", width, "\theight:", height, "\tarea:", area)
    
printArea() # Default arguments width = 1 and height = 2
printArea(4, 2.5)   # Positional arguments width = 4 and height = 2.5
printArea(height = 5, width = 3)    # keyword arguments width = 3 and height = 5
printArea(width = 1.2)  # Default height = 2
printArea(height = 6.2) # Default width = 1