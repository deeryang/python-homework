#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:45:46 2019

@author: yang
"""

def displayPattern(n):
    for i in range(n):
        for j in range(n):
            if j < n - 1 - i:
                print(" ", end = " ")
            else:
                print(n - j, end = " ")
        print()
    
def main():
    n = eval(input("Enter an integer: "))
    displayPattern(n)    

main()