#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:26:56 2019

@author: yang
"""

# compute the sum : m(i) = 1/2 + 2/3 + ... + i/(i+1)
def computeSum(n):
    result = 0
    for i in range(n):
        result += (i + 1) / (i + 2)
        
    return result

# print the chart
def printChart():
    print(format("i", ">4s"), format("m(i) ", ">8s"))
    for i in range(20):
        print(format(i + 1, "4d"), format(computeSum(i + 1), ">8.4f"))
        
def main():
    printChart()
    
main()