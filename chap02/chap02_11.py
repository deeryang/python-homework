#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:14:19 2019

@author: yang
"""

finalValue = eval(input("Enter final account value:"))
rate = eval(input("Enter annual interest rate in percent:"))
year = eval(input("Enter number of years:"))
monthlyRate = rate / 1200
months = 12 * year
initialValue = finalValue / ((1 + monthlyRate) ** months)

print("Initial deposit value is", initialValue)