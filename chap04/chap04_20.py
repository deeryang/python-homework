#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 16:21:14 2019

@author: yang
"""

temperature = eval(input("Enter the temperature in Fahrenheit between -58 and 41:"))

if temperature < -58 or temperature > 41:
    print("The temperature is invalid")
else:
    speed = eval(input("Enter the wind speed in miles per hour:"))
    if speed < 2:
        print("The win speed is invalid")
    else:
        t = 35.74 + 0.6215 * temperature - 35.75 * speed ** 0.16 + 0.4275 * temperature * speed ** 0.16
        print("The wind chill index is:", t)
        