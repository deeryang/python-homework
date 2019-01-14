#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:57:54 2019

@author: yang
"""

def computeCommossion(salesAmount):
    if salesAmount >= 0.01 and salesAmount <= 5000:
        earnAmount = salesAmount * 0.08
    elif salesAmount >= 5000.01 and salesAmount <= 10000:
        earnAmount = 5000 * 0.08 + (salesAmount - 5000) * 0.1
    else:
        earnAmount = 5000 * 0.08 + (10000 - 5000) * 0.1 + (salesAmount - 10000) * 0.12
    
    return earnAmount

def main():
    salesAmount = 1
    earnAmount = computeCommossion(salesAmount)
    while earnAmount < 30000:
        salesAmount += 1
        earnAmount = computeCommossion(salesAmount)
    print("The minimun sales amount is", salesAmount)
    
main()
        