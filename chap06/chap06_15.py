#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:38:42 2019

@author: yang
"""

def computeTax(status, taxableIncome):
    
    tax = 0
    
    if status == 0:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.1
        elif taxableIncome <= 33950:
            tax = 8350 * 0.1 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
            (taxableIncome - 82250) * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
            (171550 - 82250) * 0.28 + (taxableIncome - 175150) * 0.33
        else:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (82250 - 33950) * 0.25 + \
            (171550 - 82250) * 0.28 + (372950 - 171550) * 0.33 + (taxableIncome - 372950) * 0.35
    elif status == 1:
        if taxableIncome <= 16700:
            tax = taxableIncome * 0.1
        elif taxableIncome <= 67900:
            tax = 16700 * 0.1 + (taxableIncome - 16700) * 0.15
        elif taxableIncome <= 137050:
            tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (taxableIncome - 67900) * 0.25
        elif taxableIncome <= 208850:
            tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + \
            (taxableIncome - 137050) * 0.28
        elif taxableIncome <= 372950:
            tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + \
            (208850 - 137050) * 0.28 + (taxableIncome - 208850) * 0.33
        else:
            tax = 16700 * 0.1 + (67900 - 16700) * 0.15 + (137050 - 67900) * 0.25 + \
            (208850 - 137050) * 0.28 + (372950 - 208850) * 0.33 + (taxableIncome - 372950) * 0.35
    elif status == 2:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.1
        elif taxableIncome <= 33950:
            tax = 8350 * 0.1 + (taxableIncome - 8350) * 0.15
        elif taxableIncome <= 68525:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (taxableIncome - 33950) * 0.25
        elif taxableIncome <= 104425:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + \
            (taxableIncome - 68525) * 0.28
        elif taxableIncome <= 186475:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + \
            (104425 - 68525) * 0.28 + (taxableIncome - 104425) * 0.33
        else:
            tax = 8350 * 0.1 + (33950 - 8350) * 0.15 + (68525 - 33950) * 0.25 + \
            (104425 - 68525) * 0.28 + (186475 - 104425) * 0.33 + (taxableIncome - 186475) * 0.35
    elif status == 3:
        if taxableIncome <= 11950:
            tax = taxableIncome * 0.1
        elif taxableIncome <= 45500:
            tax = 11950 * 0.1 + (taxableIncome - 11950) * 0.15
        elif taxableIncome <= 117450:
            tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (taxableIncome - 45500) * 0.25
        elif taxableIncome <= 190200:
            tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + \
            (taxableIncome - 117450) * 0.28
        elif taxableIncome <= 372950:
            tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + \
            (190200 - 117450) * 0.28 + (taxableIncome - 190200) * 0.33
        else:
            tax = 11950 * 0.1 + (45500 - 11950) * 0.15 + (117450 - 45500) * 0.25 + \
            (190200 - 117450) * 0.28 + (372950 - 190200) * 0.33 + (taxableIncome - 372950) * 0.35

    return round(tax)

# print chart of four status for different income
def printChart():
    print(format("Taxable Income", ">15s"), format("Single", ">15s"), 
          format("Married Joint", ">15s"), format("Married Separate", ">15s"), 
          format("Head of a House", ">15s"))
    print("-" * 80)
    for taxableIncome in range(50000, 60001, 50):
        tax1 = computeTax(0, taxableIncome)
        tax2 = computeTax(1, taxableIncome)
        tax3 = computeTax(2, taxableIncome)
        tax4 = computeTax(3, taxableIncome)
        print(format(taxableIncome, ">15d"), format(tax1, ">15d"),
              format(tax2, ">15d"), format(tax3, ">15d"),
              format(tax4, ">15d"))
        
def main():
    printChart()
    
main()
    