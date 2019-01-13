#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:29:45 2019

@author: yang
"""

def sumDigits(n):
    total = 0
    while n:
        total += n % 10
        n = n // 10
    
    return total

def main():
    num = eval(input("Enter an integer: "))
    print("The sum of all digits is", sumDigits(num))
    
main()