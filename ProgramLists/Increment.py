#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 10:21:48 2019

@author: yang
"""

# List 6-4
def main():
    x = 1
    print("Before the call, x is", x)
    increment(x)
    print("After the call, x is", x)
    
def increment(n):
    n += 1
    print("\tn inside the function is", n)
    
main() # Call the main function