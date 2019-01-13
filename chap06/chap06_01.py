#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:21:21 2019

@author: yang
"""

def getPentagonalNumber(n):
    return int(n * (3 * n - 1) / 2)

def main():
    for i in range(1, 101):
        num = getPentagonalNumber(i)
        if i % 10 != 0:
            print(format(num, "5d"), end = " ")
        else:
            print()
            
main()