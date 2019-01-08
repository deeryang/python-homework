#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:26:43 2019

@author: yang
"""

amount = eval(input("Enter a amount:"))

remainingAmount = amount * 100
numberOfDollars = remainingAmount // 100

remainingAmount = remainingAmount % 100

if numberOfDollars > 1:
    print("Your amount", amount, "consists of", int(numberOfDollars), "dollars", end = "")
elif numberOfDollars == 1:
    print("Your amount", amount, "consists of", int(numberOfDollars), "dollar", end = "")
else:
    pass

if remainingAmount > 1:
    print(" and", int(remainingAmount), "pennies")
elif remainingAmount == 1:
    print(" and", int(remainingAmount), "penny")
else:
    pass