#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:41:42 2019

@author: yang
"""

# sorting three numbers by ascending order
def displaySortedNumber(num1, num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num3:
        num1, num3 = num3, num1
    print("The sorted numbers are", num1, num2, num3)
    
def main():
    num1, num2, num3 = eval(input("Enter three numbers: "))
    displaySortedNumber(num1, num2, num3)
    
main()