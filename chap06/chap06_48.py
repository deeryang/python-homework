#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:56:06 2019

@author: yang
"""

# rewrite the format function
def format(number, width):
    length = len(str(number))
    if length >= width:
        return str(number)
    else:
        return "0" * (width - length) + str(number)

def main():
    number = eval(input("Enter an integer: "))
    width = eval(input("Enter the width: "))
    
    print("The formatted number is "  + format(number, width))
    
main()