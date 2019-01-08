#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 19:20:44 2019

@author: yang
"""

minutes = eval(input("Enter the number of minutes:"))
days = minutes // (24 * 60)
years = days // 365
leftDays = days - years * 365
print(minutes, "minutes is approximately", years, "years and", leftDays, "days")
