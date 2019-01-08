#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:19:41 2019

@author: yang
"""

weight = eval(input("Enter weight in pounds:"))
feet = eval(input("Enter feet:"))
inches = eval(input("Enter inches:"))

BMI = weight * 0.4535924 / (feet * 0.3048 + inches * 0.0254) ** 2

print("BMI is", BMI)

if BMI < 18.5:
    print("You are Underweight")
elif BMI < 25:
    print("You are Normal")
elif BMI < 30:
    print("You are Overweight")
else:
    print("You are Obese")