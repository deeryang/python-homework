#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:42:04 2019

@author: yang
"""

temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))
speed = eval(input("Enter the wind speed in miles per hour:"))
t = 35.74 + 0.6215 * temperature - 35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16
print("The wind chill index is:", t)