#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 21:47:29 2019

@author: yang
"""

years = eval(input("Enter the number of years:"))
amount = 312032486
seconds = years * 365 * 24 * 3600
changeValue = seconds // 7 - seconds // 13 + seconds // 45
res = amount + changeValue

print("The population in", years, "years is", res)