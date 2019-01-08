#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:35:38 2019

@author: yang
"""

monthlyAmount = eval(input("Enter the monthly saving amount:"))
monthlyRate = 0.05 / 12
value = 0
for i in range(6):
    value += monthlyAmount
    value += value * monthlyRate

print("After the six month, the account value is", value)