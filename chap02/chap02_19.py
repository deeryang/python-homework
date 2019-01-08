#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:22:50 2019

@author: yang
"""

amount = eval(input("Enter investment amount:"))
annualRate = eval(input("Enter annual interest rate:"))
year = eval(input("Enter number of years:"))
monthlyRate = annualRate / 1200
months = year * 12
value = amount * (1 + monthlyRate) ** months

print("Accumulated value is", value)