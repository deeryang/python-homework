#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:11:03 2019

@author: yang
"""

import random
# print a n*n matrix
def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0, 1), end = " ")
        print()
        
def main():
    n = eval(input("Enter n: "))
    printMatrix(n)
    
main()