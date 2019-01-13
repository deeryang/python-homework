#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 16:38:18 2019

@author: yang
"""

# return the reversal of an integer
def reverse(number):
    res = number % 10
    number = number // 10
    while number:
        res = res * 10 + number % 10
        number = number // 10
        
    return res

def main():
    number = eval(input("Enter an integer: "))
    print("The reversal of number", number, "is", reverse(number))
    
main()