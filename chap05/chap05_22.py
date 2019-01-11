#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:04:12 2019

@author: yang
"""

counter = 0
print("The prime numbers between 2 and 1000 are:")

for i in range(2, 1001):
    divisor = 2
    isPrime = True
    while divisor <= i / 2:
        if i % divisor == 0:
            isPrime = False
            break
        divisor += 1
        
    if isPrime:
        counter += 1
        print(format(i, ">5d"), end = "")
        if counter % 8 == 0:
            print()
    
    