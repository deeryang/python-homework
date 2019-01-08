#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:03:51 2019

@author: yang
"""

weight = eval(input("Enter weight in pounds:"))
height = eval(input("Enter height in inches:"))
BMI = weight * 0.45359237 / (height * 0.0254) ** 2
print("BMI is", BMI)