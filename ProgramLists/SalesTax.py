#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:31:47 2019

@author: yang
"""

# Prompt the user for input
purchaseAmount = eval(input("Enter purchase amount: "))

# Compute sales tax
tax = purchaseAmount * 0.06

# Display tax amount with two digits after decimal point
print("Sales tax is", int(tax * 100) / 100.0)