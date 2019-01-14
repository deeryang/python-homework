#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:32:18 2019

@author: yang
"""

# estimate the value of pi
def estimatePi(n):
    result = 0
    for i in range(n):
        result += (-1) ** i / (2 * i + 1)
        
    return 4 * result

# print chart
def printChart():
    print(format("i", ">4s"), format("m(i) ", ">8s"))
    for i in range(1, 902, 100):
        print(format(i, "4d"), format(estimatePi(i), ">8.4f"))
   
def main():
    printChart()
    
main()