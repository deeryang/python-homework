#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:35:08 2019

@author: yang
"""

# List 6-6
from GCDFunction import gcd # Import the gcd function

# Prompt the user to enter two integers
n1 = eval(input("Enter the first integer: "))
n2 = eval(input("Enter the second integer: "))

print("The greatest commom divisor for", n1, "and", 
      n2, "is", gcd(n1, n2))
