#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:00:02 2019

@author: yang
"""

def numberOfDaysInAYear(year):
    if (year % 4 == 0 or year % 100 == 0) and year % 400 != 0:
        days = 366
    else:
        days = 365
        
    return days

def main():
    for year in range(2010, 2021):
        print("The year of", year, "has", numberOfDaysInAYear(year), "days")
        
main()