#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:33:48 2019

@author: yang
"""

balance, rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%):"))
interest = balance * rate / 1200

print("The interest is", interest)